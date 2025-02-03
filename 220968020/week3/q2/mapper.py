#!usr/bin/env python3
import sys


#note: format of dataset-> year temperature
for line in sys.stdin:
    # Strip leading/trailing whitespaces
    line = line.strip()
    
    # Split the line by whitespace
    tokens = line.split()
    
    # Check if there are enough tokens (Year and Temperature)
    if len(tokens) >= 2:
        year = tokens[0]
        temperature = int(tokens[1].strip())
        
        # Emit the year as the key and the temperature as the value
        print(f"{year}\t{temperature}")
