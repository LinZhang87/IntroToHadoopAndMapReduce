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
            print "{0}\t{1}".format(path, 1)
                                                                                                                                                                                              14,13         All
