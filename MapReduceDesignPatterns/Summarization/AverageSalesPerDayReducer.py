#!/usr/bin/python

import sys

def reducer():
    prevDay = None
    salesNum = 0
    salesTotal = 0
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue
        currDay, sale = data_mapped
        if prevDay and prevDay != currDay:
            if salesNum == 0:
                print "{0}\t{1}".format(prevDay, 0)       
            else:
                print "{0}\t{1}".format(prevDay, salesTotal / salesNum)
            salesNum = 0
            salesTotal = 0
        prevDay = currDay
        salesNum += 1
        salesTotal += float(sale)
    if prevDay != None:
        if salesNum == 0:
            print "{0}\t{1}".format(prevDay, 0)       
        else:
            print "{0}\t{1}".format(prevDay, salesTotal / salesNum)
        salesNum = 0
        salesTotal = 0     
        
def main():
    reducer()
if __name__ == "__main__":
    main()