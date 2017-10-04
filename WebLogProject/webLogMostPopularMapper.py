#!/usr/bin/python

import sys
import re
			
for line in sys.stdin:
    line = line.strip()
    matchData = re.match('([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+\[([^\]]+)\]\s+"([^"]+)"\s+([^\s]+)\s+([^\s]+)', line)
    if matchData != None:
        host, ident, authuser, date, request, status, bytes = matchData.groups()
        requestData = request.split(" ")
        if(len(requestData) == 3):
            method, path, protocol = requestData
            path = path.replace("http://www.the-associates.co.uk", "")
            print "{0}\t{1}".format(path, 1)
