# -*- coding: utf-8 -*-
import jieba
import sys
import codecs
import os
from collections import Counter
import heapq

#1) workaround, for setting the encoding for the python script
#sys.stdout should be set UTF-8 explicitly
sys.stdout=codecs.getwriter('utf-8')(sys.stdout)

#2) export PYTHONIOENCODING='utf8'
# It is a way by environment setteing to change the encoding
#Overrides the encoding used for stdin/stdout/stderr

#3) change default encoding, it is not a suggestion, worst usage
#if sys.getdefaultencoding() != 'utf-8':
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
"""
# all modes for chinese segmentation
fullMode = jieba.cut(contentstring, cut_all=True)  # 全模式
defaultMode = jieba.cut(contentstring, cut_all=False)  # 精确模式
searchMode = jieba.cut_for_search(contentstring)  # 搜索引擎模式
"""
def getfeature(contentstring):
    words=jieba.cut(contentstring, cut_all=False)
    wordlist = list(words)
    counts = Counter(wordlist)

    top3tf_num = sum(heapq.nlargest(3,counts.values()))
    totalwords_num = len(contentstring)

    stopwords_num = 0
    for k in counts.keys():
        if k in stoplist:
            stopwords_num += counts[k]

    return top3tf_num, totalwords_num, stopwords_num

"""
def debug():
    print u"中文偵錯訊息"
    print "sys.getdefaultencoding():",sys.getdefaultencoding()
    print "sys.stdout.encoding:",sys.stdout.encoding
    print "sys.stderr.encoding:",sys.stderr.encoding

usage_help_str="[usage] python "+sys.argv[0]+" filename "+"output.report"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print usage_help_str
        exit(0)
    try:
        infilename = sys.argv[1]
        outfilename = sys.argv[2]
        tmpfilename = "tmpfile.txt"
        infilehandle = codecs.open(infilename, 'rb','utf-8')
        tmpfilehandle = codecs.open(tmpfilename, 'wb+','utf-8')
        outfilehandle = codecs.open(outfilename, 'wb+','utf-8')

        #print "Output 精確模式 Full Mode："
        with infilehandle:
            words = jieba.cut(infilehandle.read(), cut_all=False)
        with tmpfilehandle:
            for word in words:
                if not word.isspace():
                    tmpfilehandle.write(word + u"\n")
    except Exception as e:
        print str(e)
    finally:
        #sort output and put lines into target output file
        reopen_tmpfilehandle =  codecs.open(tmpfilename,"r+",'utf-8')
        with reopen_tmpfilehandle:
            with outfilehandle:
                sorted_lines = sorted(reopen_tmpfilehandle.readlines())
                word_occurrence_pair = Counter(sorted_lines)
                for word, occurrence in word_occurrence_pair.items():
                    # save result into outfilehandle
                    print >>outfilehandle, word.rstrip(),occurrence
                    # show result in stdout
                    print word.rstrip(),occurrence
"""
