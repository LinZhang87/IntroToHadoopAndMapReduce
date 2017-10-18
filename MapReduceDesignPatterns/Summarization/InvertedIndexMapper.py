#!/usr/bin/python
import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    lineNum = 0
    for line in reader:
        if lineNum > 0 and len(line) >= 5:
            nodeId = line[0].strip()
            words = re.split('\s+|[:\.,!\?;"\(\)<>\[\]#\$=\-\/]{1}', line[4].strip())
            for word in words:
                word = word.lower()
                print "{0}\t{1}".format(word, nodeId)
        lineNum += 1
    
def main():
    mapper()
if __name__ == "__main__":
    main()