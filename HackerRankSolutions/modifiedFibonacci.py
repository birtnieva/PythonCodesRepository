#!/bin/python3

a, b, n = input().strip().split()
a, b, n = int(a),int(b),int(n)

def modfib(n):
    global x
    global y
    if n == 0:
        return x
    elif n == 1:
        return x
    elif n == 2:
        return y
    else:
        return modfib(n - 1)**2 + modfib(n-2)

x = a
y = b

print(modfib(n))
