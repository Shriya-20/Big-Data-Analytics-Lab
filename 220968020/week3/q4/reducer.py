#!usr/bin/env python3
import sys

curr_var = None
curr_sum = 0
curr_count = 0

for line in sys.stdin:
	line = line.strip()
	var, val = line.split("\t")
	val = int(val)
	
	if(var == curr_var):
		curr_sum += val
		curr_count += 1
	else:
		if curr_var:
			print(f"{curr_var}\t{curr_sum/curr_count}")
		curr_var = var
		curr_sum = val
		curr_count = 1
if curr_var:
	print(f"{curr_var}\t{curr_sum/curr_count}")
	
