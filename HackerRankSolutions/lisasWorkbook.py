#!/bin/python3

import math

n, k = [int(a) for a in input().strip().split()]

t = [int(a) for a in input().strip().split()]


def spages(probpc, probpp, lastp):
    count = 0
    lastp = lastp + 1
    tc = list(range(1, probpc + 1))
    for i in range(0, len(tc), probpp):
        if lastp in tc[i:i + probpp]:
            count = count + 1
        lastp = lastp + 1
    return count

lastpg = 0
scount = 0
for ti in t:
    scount = scount + spages(ti,k,lastpg)
    lastpg = lastpg + math.ceil(ti/k)

print(scount)
