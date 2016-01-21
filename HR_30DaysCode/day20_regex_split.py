#!/usr/bin/python3
#
# Regular expression and split
#
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-20-review-plus-more-string-methods

import re

str = input().strip()

arr = re.split("[!\[,?.\\\\_'\@\+\] ]+", str)
# use filter funtion to remove trailing empty string from split()
arr = list(filter(None, arr))

print(len(arr))
for i in range(len(arr)):
    print(arr[i])


"""
input:
He is a very very good boy, isn't he?

output:
10
He
is
a
very
very
good
boy
isn
t
he

problem:
Given a string S, find number of words in that string. For this problem a word is defined by a string of one or 
more English letters.
Note: Space or any of the special characters like ![,?.\_'@+] will act as a delimiter. 

references:
https://docs.python.org/2/library/re.html
http://stackoverflow.com/questions/2197451/why-are-empty-strings-returned-in-split-results
http://stackoverflow.com/questions/30933216/split-by-regex-without-resulting-empty-strings-in-python?lq=1
"""
