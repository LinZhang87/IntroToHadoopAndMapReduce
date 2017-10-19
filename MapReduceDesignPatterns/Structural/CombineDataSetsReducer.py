#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

def reducer():
    prevUserId = None
    reputation = "0" 
    gold = "0"
    silver = "0"
    bronze = "0"
    currList = []
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 6 and len(data_mapped) != 10:
            continue
        currUserId = data_mapped[0]
        type = data_mapped[1]
        if prevUserId and prevUserId != currUserId:
            for postList in currList:
                printFormatStr(postList, reputation, gold, silver, bronze)
            currList = []
        prevUserId = currUserId
        if type == "user":
            reputation = data_mapped[2]
            gold = data_mapped[3]
            silver = data_mapped[4]
            bronze = data_mapped[5]
        else:
            currList.append(data_mapped)

    if prevUserId != None:
        for postList in currList:
            printFormatStr(postList, reputation, gold, silver, bronze)
        currList = []      
        
def printFormatStr(postList, reputation, gold, silver, bronze):
    postList.append(postList.pop(0))
    postList.pop(0)
    postList.append(reputation)
    postList.append(gold)
    postList.append(silver)
    postList.append(bronze)
    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(postList[0],postList[1],postList[2],postList[3],postList[4],postList[5],postList[6],postList[7],postList[8],postList[9],postList[10],postList[11],postList[12])
    
def main():
    reducer()
if __name__ == "__main__":
    main()          