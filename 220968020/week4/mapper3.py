#!/usr/bin/env python3
import sys
for line in sys.stdin:
    line = line.strip()
    fields = line.split(' ', 1)
    if len(fields) == 2:
        doc_id, content = fields
        words = content.split()
        for word in words:
            word = word.lower().strip('.,!?":;()[]{}')
            print(f"{word}\t{doc_id}")

