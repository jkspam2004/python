#!/usr/bin/python3

# Arrays
#
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-7-arrays

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

i = n - 1
while(i >= 0):
    print(arr[i], end=' ')
    i -= 1


"""
The first line of input contains N, the number of integers. The next line contains N integers separated by a space.
input:
4
1 4 3 2


output:
2 3 4 1

problem:
Print the array of integers in reverse order
"""

