#!/bin/python3
#
# If-Else statements
#
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-3-if-statements

import sys


N = int(input().strip())

if N % 2 == 0 and ((N >= 2 and N <= 5) or N > 20):
    print("Not Weird")
else:
    print("Weird")
   

"""
Problem:
Given an integer N as input, check the following:

    If N is odd, print "Weird".
    If N is even and, in between the range of 2 and 5(inclusive), print "Not Weird".
    If N is even and, in between the range of 6 and 20(inclusive), print "Weird".
    If N is even and N>20, print "Not Weird".

""" 
