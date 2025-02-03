#!usr/bin/env python3
import sys

for line in sys.stdin:
	line = line.strip()
	fields = line.split(",")
	if len(fields) == 2:
		var, val = fields[0], fields[1]
		print(f"{var}\t{val}")
