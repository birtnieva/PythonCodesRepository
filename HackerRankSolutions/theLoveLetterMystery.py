#!/bin/python3

import string

abcs = string.ascii_lowercase

t = int(input().strip())

for x in range(0,t):
    instr = input().strip()

    s = [i for i in instr]

    shift_cnt = 0

    for i in range(0,int(len(s)/2)):
        if s[-1-i] > s[i]:
            while s[i] != s[-1-i]:
                s[-1-i] = abcs[abcs.index(s[-1-i])-1]
                shift_cnt = shift_cnt + 1
        else:
            while s[i] != s[-1-i]:
                s[i] = abcs[abcs.index(s[i]) - 1]
                shift_cnt = shift_cnt + 1
            
    print(shift_cnt)
