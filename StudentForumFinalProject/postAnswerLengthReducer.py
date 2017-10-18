#!/usr/bin/python

import sys

def reducer():
    prevPostId = None
    numOfAnswerPosts = 0
    questionLen = 0
    totalLenOfAnswerPosts = 0
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if(len(data_mapped) != 3):
            continue
        currPostId, postType, postLen = data_mapped 
        if prevPostId and prevPostId != currPostId:
            if questionLen != 0:
                if numOfAnswerPosts == 0:
                    print "{0}\t{1}\t{2}".format(prevPostId, questionLen, 0)                
                else:
                    print "{0}\t{1}\t{2}".format(prevPostId, questionLen, totalLenOfAnswerPosts / numOfAnswerPosts)
            questionLen = 0
            numOfAnswerPosts = 0
            totalLenOfAnswerPosts = 0
        prevPostId = currPostId
        if postType == "question":
            questionLen = postLen
        elif postType == "answer":            
            numOfAnswerPosts = numOfAnswerPosts + 1
            totalLenOfAnswerPosts = totalLenOfAnswerPosts + float(postLen)
    if prevPostId != None:
        if questionLen != 0:
            if numOfAnswerPosts == 0:
                print "{0}\t{1}\t{2}".format(prevPostId, questionLen, 0)                
            else:
                print "{0}\t{1}\t{2}".format(prevPostId, questionLen, totalLenOfAnswerPosts / numOfAnswerPosts)
        questionLen = 0
        numOfAnswerPosts = 0
        totalLenOfAnswerPosts = 0     
   
def main():
    reducer()
if __name__ == "__main__":
    main()