# Mapper.py
# Run on Python3

import sys
import re

count = 1

# Loops through input lines of text
for input in sys.stdin:
    
    # Strip off spaces in beggining and end of input line
    input = input.strip()
    
    # Remove characters (.,!?) and convert text to lower case
    input = re.sub('[^a-zA-Z\-]+', ' ', input).lower()
    
    # Split input into words
    words = input.split()
    
    # Words are output as keys with count value to 1
    for word in words:
        print( "%s\t%d" % (word, count) )
