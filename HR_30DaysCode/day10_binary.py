#!/usr/bin/python3
#
# Binary
#
# convert decimal integer into binary
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-10-binary-numbers

T = int(input().strip())

for index in range(T):
    num = int(input().strip())    
    result = ''

    # keep dividing by 2 until the dividend is zero
    # remainder will be the binary number
    while num != 0:
        mod = num % 2  # get the remainder
        num = num // 2 # get the dividend
        
        result = str(mod) + result
        
    print(result)


"""
input:
2
4
5

The first line contains a single integer, T, the number of test cases. The T subsequent lines of test cases each contain a single value, n, the base 10 positive integer to be converted.

output:
100
101

4
2, 0
1, 0
0, 1

5
2, 1
1, 0
0, 1

6
3, 0
1, 1
0, 1

7
3, 1
1, 1
0, 1
"""
