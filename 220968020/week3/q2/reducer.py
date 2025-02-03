#!usr/bin/env python3
import sys

current_year = None
max_temp = None

for line in sys.stdin:
    # Strip leading/trailing whitespaces
    line = line.strip()

    # Split the input line into year and temperature
    year, temp = line.split()
    temp = int(temp)

    # Check if we're still processing the same year
    if current_year == year:
        # Keep track of the maximum temperature for this year
        if temp > max_temp:
            max_temp = temp
    else:
        # If the year has changed, output the max temperature for the previous year
        if current_year:
            print(f"{current_year}\t{max_temp}")
        
        # Set the new year and reset max temperature
        current_year = year
        max_temp = temp

# Output the result for the last year processed
if current_year == year:
    print(f"{current_year}\t{max_temp}")
