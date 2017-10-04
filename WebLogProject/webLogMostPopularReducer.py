#!/usr/bin/python

import sys

totalNumOfOccu = 0
mostOccurences = 0
mostPopularKey = None
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, occur = data_mapped
    if oldKey and oldKey != thisKey:
        if totalNumOfOccu > mostOccurences:
            mostPopularKey = oldKey
            mostOccurences = totalNumOfOccu
        totalNumOfOccu = 0
    oldKey = thisKey
    totalNumOfOccu = totalNumOfOccu + int(occur)

if oldKey != None:
    if totalNumOfOccu > mostOccurences:
        mostPopularKey = oldKey
        mostOccurences = totalNumOfOccu  

print "{0}\t{1}".format(mostPopularKey, mostOccurences)  