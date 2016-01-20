#!/usr/bin/python3
#
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-6-lets-review 

n = int(input())

print('123456')
for i in range(1,n+1):
    print(' '*(n-i) + '#' * i)

"""
Print a staircase of height N that consists of # symbols and spaces as given in Sample Output.

     #
    ##
   ###
  ####
 #####
######

"""
