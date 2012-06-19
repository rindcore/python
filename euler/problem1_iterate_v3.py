#!/usr/bin/env python3

n = []

for i in range(1,1000):
    if i%3 == 0 or i%5 == 0: n.append(i)

print(sum(n))

print(sum(range(3,1000,3))+sum(range(5,1000,5))-sum(range(15,1000,15)))
