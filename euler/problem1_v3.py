#!/usr/bin/env python3

def div_sum(max_n, div_n):
    n = max_n//div_n
    return div_n*(1+n)*n//2

print(div_sum(999,3)+div_sum(999,5)-div_sum(999,15))
