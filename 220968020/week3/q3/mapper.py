#!usr/bin/env python3
import sys

for line in sys.stdin:
	line = line.strip()
	fields = line.split(",")
	if len(fields) == 2:
		name = fields[0]
		score = fields[1]
		print(f"{name}\t{score}")
