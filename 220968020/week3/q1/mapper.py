#!/usr/bin/env python3
import sys

for line in sys.stdin:
	line = line.strip()
	for char in line:
		if char != ' ':
			print(f"{char}\t1")#(character	1)
