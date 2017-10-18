#!/usr/bin/python

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter = '\t')
    writer = csv.writer(sys.stdout, delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_ALL)
    
    firstLine = True
    for line in reader:       
        if firstLine:
            firstLine = False
        elif len(line) >= 8:
            postId = line[0]
            postType = line[5]
            parentId = line[7]
            if postId != None and postType != None:
                if parentId != "\N":
                    print "{0}\t{1}\t{2}".format(parentId, postType, len(line[4]))
                else:
                    print "{0}\t{1}\t{2}".format(postId, postType, len(line[4]))                    
    
def main():
    mapper()
if __name__ == "__main__":
    main()
