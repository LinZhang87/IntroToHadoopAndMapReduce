#!/usr/bin/python

import sys

totalNumOfHits = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, hit = data_mapped
    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, totalNumOfHits)
        totalNumOfHits = 0
    oldKey = thisKey
    totalNumOfHits = totalNumOfHits + int(hit)

if oldKey != None:
    print "{0}\t{1}".format(oldKey, totalNumOfHits)