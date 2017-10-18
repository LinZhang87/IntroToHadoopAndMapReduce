#!/usr/bin/python

import sys

def reducer():
    prevWord = None
    occurences = 0
    nodes = set()
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue
        currWord, nodeId = data_mapped
        if prevWord and prevWord != currWord:
            print "{0}\t{1}\t{2}".format(prevWord, occurences, printNodes(nodes))
            occurences = 0
            nodes.clear()
        prevWord = currWord
        occurences += 1
        nodes.add(int(nodeId))
    if prevWord != None:
        print "{0}\t{1}\t{2}".format(prevWord, occurences, printNodes(nodes))
        occurences = 0
        nodes.clear()        
    
def printNodes(nodes):
    nodeList = list(nodes)
    if len(nodeList) > 0:
        nodeList.sort()
        nodeStr = str(nodeList[0])
        idx = 1
        while idx < len(nodeList):
            nodeStr += ("," + str(nodeList[idx]))
            idx += 1
        return nodeStr
        
def main():
    reducer()
if __name__ == "__main__":
    main()