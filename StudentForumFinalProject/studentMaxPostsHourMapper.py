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
        elif len(line) >= 9:
            authorId = line[3]
            if authorId != None:
                postTime = re.match('([^\s]+)\s+([^:]+):([^:]+):([^\+]+)\+', line[8])
                if postTime != None:
                    postDate, postHour, postMinute, postSecond = postTime.groups()
                    print "{0}\t{1}".format(authorId, postHour)
    

def main():
    mapper()
if __name__ == "__main__":
    main()
