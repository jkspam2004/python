#!/usr/bin/python3
#
# Arithmetic
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-2-arithmetic


M=float(input())
T=float(input())
X=float(input())


tip = (T * M)/100
tax = (X * M)/100
final = tip + tax + M

print("The final price of the meal is $%s." %round(final))

