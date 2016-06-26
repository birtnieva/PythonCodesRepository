import collections

n = int(input().strip())
A = [int(i) for i in input().strip().split()]

y = collections.Counter(A)

dups = [val for val,cnt in y.items() if cnt > 1]


if (len(dups)>0):
    dist = []

    for i in dups:
        index = [j for j,k in list(enumerate(A)) if i == k]
        dist.append(abs(index[0]-index[1]))

    print(min(dist))
else:
    print(-1)
