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
        elif len(line) >= 6:
            tags = line[2].strip().split()
            postType = line[5]
            if postType == "question":
                for tag in tags:
                    print "{0}\t{1}".format(tag, 1)                                   
    
def main():
    mapper()
if __name__ == "__main__":
    main()
