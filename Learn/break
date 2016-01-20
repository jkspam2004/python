#!/usr/bin/python3
# The break statement breaks out of the smallest enclosing for or while loop:

for n in range(2, 10):
     for x in range(2, n):
         print(n,x)
         if n % x == 0:
             print(n, 'equals', x, '*', n/x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')


"""
The else clause belongs to the for loop, not the if statement

Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the 
list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a 
break statement.

"""


# The continue statement, also borrowed from C, continues with the next iteration of the loop:
for num in range(2, 10):
     if num % 2 == 0:
         print("Found an even number", num)
         continue
     print("Found a number", num)


# The pass statement does nothing. It can be used when a statement is required syntactically but the program 
# requires no action. For example:

while True:
     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
