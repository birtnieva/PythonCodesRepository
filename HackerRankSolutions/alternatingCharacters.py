#!/bin/python3

t = int(input().strip())

for i in range(0,t):
    str = input().strip()

    c = [s for s in str]

    curr = 0
    deletion = 0

    while curr != len(c)-1:
        if c[curr] == c[curr+1]:
            del c[curr+1]
            deletion = deletion + 1
        else:
            curr = curr+1
    print(deletion)

    print(c)
