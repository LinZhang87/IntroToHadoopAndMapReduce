#!/usr/bin/python

import sys
import Queue as Q

def reducer():
    prevTag = None
    totalCount = 0
    minPq = Q.PriorityQueue()
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if(len(data_mapped) != 2):
            continue
        currTag, count = data_mapped 
        if prevTag and prevTag != currTag:
            addToMinPq(minPq, totalCount, prevTag)
            totalCount = 0
        prevTag = currTag
        totalCount = totalCount + int(count)
    if prevTag != None:
        addToMinPq(minPq, totalCount, prevTag)
        totalCount = 0  
    printTopTenTags(minPq)
    
def addToMinPq(minPq, totalCount, tag):
    if minPq.qsize() < 10:
        minPq.put((totalCount, tag))
    elif totalCount > minPq.queue[0][0]:
        minPq.get()
        minPq.put((totalCount, tag))

def printTopTenTags(minPq):
    topTenTags = []
    while not minPq.empty():
        entry = minPq.get()
        topTenTags.append((entry[1], entry[0]))
    topTenTags.reverse()
    for e in topTenTags:
        print "{0}\t{1}".format(e[0], e[1])
    
def main():
    reducer()
if __name__ == "__main__":
    main()