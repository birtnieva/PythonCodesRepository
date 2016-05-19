# Example MapReduce code for Hadoop Streaming

A simple MapReduce program written in Python3 for testing Hadoop Streaming feature.

###### Mapper.py
1. For each input line of text, remove leading and trailing spaces
2. Remove characters (.,!?)
3. Split line into words
4. Attach the value of 1 to each word
5. Output word-value pair (key-value)

###### Reduce.py
1. Intialize variables for counting words
2. For each word-value pair, remove leading and trailing spaces.
3. Parse word and value for evaluation
4. Count similar words
5. Print output of the count of words

###### To test the command
1. Open windows command line.
2. type GreenEggsAndHam.txt | .\Mapper.py | sort | .\Reducer.py
