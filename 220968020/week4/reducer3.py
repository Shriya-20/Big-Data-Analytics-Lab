#!/usr/bin/env python3
import sys
from collections import defaultdict

word_to_docs = defaultdict(set)

for line in sys.stdin:
    line = line.strip()
    word, doc_id = line.split('\t')
    word_to_docs[word].add(doc_id)

for word, docs in word_to_docs.items():
    print(f"{word}\t{','.join(sorted(docs))}")

