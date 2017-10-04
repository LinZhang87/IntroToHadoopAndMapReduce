#!/usr/bin/python

import sys
import re
			
for line in sys.stdin:
    line = line.strip()
    matchData = re.match('([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+\[([^\]]+)\]\s+"([^"]+)"\s+([^\s]+)\s+([^\s]+)', line)
    if matchData != None:
        host, ident, authuser, date, request, status, bytes = matchData.groups()
        print "{0}\t{1}".format(host, 1)