#!/usr/bin/python

import sys

def reducer():
    prevAuthorId = None
    numOfPostsEachHour = {}
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if(len(data_mapped) != 2):
            continue
        currAuthorId, postHour = data_mapped 
        if prevAuthorId and prevAuthorId != currAuthorId:
            for hour in getHourOfMostPosts(numOfPostsEachHour):
                print "{0}\t{1}".format(prevAuthorId, hour)
            numOfPostsEachHour.clear()
        prevAuthorId = currAuthorId
        if numOfPostsEachHour.has_key(postHour):
            numOfPostsEachHour[postHour] = numOfPostsEachHour[postHour] + 1
        else:
            numOfPostsEachHour[postHour] = 1  
    if prevAuthorId != None:
        for hour in getHourOfMostPosts(numOfPostsEachHour):
            print "{0}\t{1}".format(prevAuthorId, hour)
        numOfPostsEachHour.clear()      

def getHourOfMostPosts(numOfPostsEachHour):
    mostPosts = -1
    hoursWithMostPosts = []
    for hour in numOfPostsEachHour.keys():
        if numOfPostsEachHour[hour] > mostPosts:
            mostPosts = numOfPostsEachHour[hour]
    for hour in numOfPostsEachHour.keys():
        if numOfPostsEachHour[hour] == mostPosts:
            hoursWithMostPosts.append(hour)
    return hoursWithMostPosts
    
def main():
    reducer()
if __name__ == "__main__":
    main()