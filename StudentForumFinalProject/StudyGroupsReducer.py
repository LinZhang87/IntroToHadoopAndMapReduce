#!/usr/bin/python

import sys

def reducer():
    prevPostId = None
    authorList = []
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if(len(data_mapped) != 2):
            continue
        currPostId, authorId = data_mapped 
        if prevPostId and prevPostId != currPostId:
            printAuthorIds(prevPostId, authorList)
            authorList = []
        prevPostId = currPostId
        authorList.append(authorId)
    if prevPostId != None:
        printAuthorIds(prevPostId, authorList)
        authorList = [] 

def printAuthorIds(postId, authorList):
    if authorList != None and len(authorList) > 0:
        authors = "[" + authorList[0]   
        idx = 1
        while idx < len(authorList):
            authors += ("," + authorList[idx])
            idx += 1
        authors += "]"
        print "{0}\t{1}".format(postId, authors)
        
def main():
    reducer()
if __name__ == "__main__":
    main()