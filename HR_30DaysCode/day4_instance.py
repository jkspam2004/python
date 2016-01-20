#!/usr/bin/python3
#
# Instance
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-4-boolean-operators-class-vs-instance

class Person:
        def __init__(self,initial_Age):
       		# Add some more code to run some checks on initial_Age
            if initial_Age < 0:
                self.age = 0
                print("This person is not valid, setting age to 0.")
            else:
                self.age = initial_Age
                
        def amIOld(self):
            # Do some computations in here and print out the correct statement to the console
            if self.age < 13:
                print("You are young.")
            elif self.age >= 13 and self.age < 18:
                print("You are a teenager.")
            else:
                print("You are old.")
                
        def yearPasses(self):
            # Increment the age of the person in here   
            self.age += 1

T=int(input())
for i in range(0,T):
    age=int(input())         
    p=Person(age)
    p.amIOld()
    for j in range(0,3):
        p.yearPasses();        
    p.amIOld();
    print ("")


"""
Input:
4
-1
10
16
18

Output:
This person is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
"""
