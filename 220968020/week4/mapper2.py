#!/usr/bin/env python3
import sys
STOP_WORDS = {'is', 'the', 'and', 'a', 'of', 'in', 'to', 'for', 'on', 'with', 'by'}
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower().strip('.,!?":;()[]{}')
        if word not in STOP_WORDS:
            print(f"{word}\t1")

