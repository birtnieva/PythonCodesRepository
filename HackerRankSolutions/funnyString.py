#!/bin/python3

import string

t = int(input().strip())

for i in range(0,t):
    str = input().strip()

    ltr = list(string.ascii_lowercase)
    
    ctr = 0
    state = 'Not Funny'
    while ctr < len(str)-1:
        if (abs(ltr.index(str[ctr+1]) - ltr.index(str[ctr])) != abs(ltr.index(str[-2-ctr]) - ltr.index(str[-1-ctr]))):
            state = 'Not Funny'
            break
        else:
            state = 'Funny'
            ctr = ctr + 1
    print(state) 
