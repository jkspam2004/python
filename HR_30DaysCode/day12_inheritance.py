#!/usr/bin/python3
#
# Inheritance
# You are given two classes, Student and Grade, 
# where Student is the base class and Grade is the derived class. 
# Note that Grade inherits all the properties of Student.
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-12-inheritance

class Student:
    def __init__(self, firstName, lastName, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
    def display(self):
        print("First Name:", self.firstName)
        print("Last Name:", self.lastName)
        print("Phone:", self.phone)

class Grade(Student):
    def __init__(self, firstName, lastName, phone, score):
        Student.__init__(self, firstName, lastName, phone)
        self.score = score
    def calculate(self):
        print("Calculating grade for", self.firstName)
        if self.score < 40:
            return 'D'
        elif self.score >= 40 and self.score < 60:
            return 'B'
        elif self.score >= 60 and self.score < 75:
            return 'A'
        elif self.score >= 75 and self.score < 90:
            return 'E'
        elif self.score >= 90 and self.score <= 100:
            return 'O'


firstName = input().strip()
lastName = input().strip()
phone = int(input())
score = int(input())
stu = Grade(firstName, lastName, phone, score)
stu.display()
print("Grade:", stu.calculate())

"""
input:
 Heraldo
 Memelli
 8135627
 90

output:
 First Name: Heraldo
 Last Name: Memelli
 Phone: 8135627
 Grade: O

"""
