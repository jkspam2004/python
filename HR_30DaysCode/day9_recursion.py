#!/usr/bin/python3
#
# Recursion
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-9-recursion

# needed to increase the recursion limit and stack size as some test cases produced runtime error
import resource
import sys

sys.setrecursionlimit(1000000000)
#resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

def find_gcd(a,b):
   #Write base condition
    if a == b:
        return a
    else:
        max_num = max(a,b)
        min_num = min(a,b)
    return find_gcd(max_num - min_num, min_num)

#Take input
a,b = map(int, input().split())
gcd=find_gcd(a,b)
print (gcd)

"""
input:
1 5

output:
1

problem:
Given two integers, x and y, their GCD (greatest common divisor) can be calculated recursively using Euclid's Algorithm, which essentially says that if x equals y, then GCD(x,y)=x; otherwise, GCD(x,y)=GCD(x−y,y) if x>y. Note that this logic can be further optimized for a more efficient implementation.

Euclid's algorithm:
http://people.cis.ksu.edu/~schmidt/301s12/Exercises/euclid_alg.html

int GCD(x,y): 
    If x equals y, return x; 
    Else, return GCD(x',y'), where x' = MAX(x,y) - MIN(x,y) and y' = MIN(x,y).

"""

# modulo
def find_gcd2(a, b):
    if b == 0:
        return a
    return find_gcd2(b, a % b)
a, b = [int(i) for i in next(sys.stdin).split()]
gcd = find_gcd2(a, b)
print (gcd)


