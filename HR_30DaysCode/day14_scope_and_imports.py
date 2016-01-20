#!/usr/bin/python3
# 
# Scope and Imports
#
# find the maximum absolute difference between two integers
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-14-scope-and-imports

class Difference:
    def __init__(self, a):
        self.__elements = a

    # O(n)
    def computeDifference(self):
        length = int(_)
        arr = self.__elements
        min_num = arr[0]
        max_num = arr[0]
        for i in range(length):
            if arr[i] < min_num:
                min_num = arr[i]
            elif arr[i] > max_num:
                max_num = arr[i]
                
        self.maximumDifference = abs(max_num - min_num)

    # O(n^2) first attempt
    def computeDifferenceBrute(self):
        arr = self.__elements
        self.maximumDifference = abs(arr[0] - arr[-1])
        for i in range(int(_)):
            for j in range(int(_)):
                if i == j:
                    continue
                    
                diff = abs(arr[i] - arr[j])
                self.maximumDifference = max(self.maximumDifference, diff)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

"""
input:
5
8 19 3 2 7

output:
17
"""
