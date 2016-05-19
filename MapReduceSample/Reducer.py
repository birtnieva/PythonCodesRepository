# Reducer.py
# Run on Python3

import sys

# Intialize the following variables
wordCounted = None
wordCounter = 0
word = None

# Loops through input key-values to mapper
for input in sys.stdin:

    # Strip off spaces in beggining and end of input line
    input = input.strip()
    
    # Parse the input from the mapper
    word, count = input.split("\t", 1)
    count = int(count)
    
    # Test if next key equals key
    if wordCounted == word:
        wordCounter += count
    else:
        if wordCounted:
            print( "%s\t%d" % (wordCounted, wordCounter) )
        wordCounter = count
        wordCounted = word

# Outputs the last word in the loop
if wordCounted == word:
    print( "%s\t%d" % (wordCounted, wordCounter) )
