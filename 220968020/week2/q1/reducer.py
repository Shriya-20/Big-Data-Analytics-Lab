#!/usr/bin/python3
"reducer.py"
import sys

current_word = None
current_count = 0

# Read input from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split the line into word and count
    word, count = line.split('\t')

    # Convert the count to an integer
    count = int(count)

    # If the current word is the same as the previous word, add the count
    if current_word == word:
        current_count += count
    else:
        # If we are moving to a new word, output the result for the previous word
        if current_word:
            print ('%s\t%s' % (current_word, current_count))

        # Update the current word and reset the count
        current_word = word
        current_count = count

# Output the last word and its count
if current_word == word:
    print ('%s\t%s' % (current_word, current_count))

