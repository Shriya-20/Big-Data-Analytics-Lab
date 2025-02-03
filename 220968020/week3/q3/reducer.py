'''
#!usr/bin/env python3
import sys
import heapq
#using a min-heap to store and efficiently retrieve the top N highest scores.

N = 3
top_n = []

for line in sys.stdin:
	line = line.strip()
	name, score = line.split("\t")
	score = int(score)
	heapq.heappush(top_n, (score, name))
	if(len(top_n) > N):
		heapq.heappop(top_n)

for name, score in top_n:
	print(f"{name}\t{score}")
	
'''

import sys

# List to store all the scores
scores = []

# Read each line from standard input (mapper output)
for line in sys.stdin:
    # Remove leading and trailing whitespaces
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Parse the input from the mapper (expected format: 'key\tscore')
    key, score = line.split('\t')

    
    score = float(score)

    # Add the score to the list
    scores.append(score)

# Sort the scores in descending order
scores.sort(reverse=True)

# Specify N (top N scores you want)
N = 3

# Output the top N scores
for i in range(min(N, len(scores))):
    print(f"Top {i + 1} Score: {scores[i]}")

