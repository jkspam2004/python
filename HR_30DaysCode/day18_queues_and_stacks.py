#!/usr/bin/python3
#
# Queues and Stacks 
#
# Determine if given string is a palindrome
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-18-queues-stacks/copy-from/4694328

class Palindrome:
    #Write your code here
    def __init__(self):
        self.queue = []
        self.stack = []
    def pushCharacter(self, c):
        self.stack.append(c)
    def enqueueCharacter(self, c):
        self.queue.append(c)
    def popCharacter(self):
        return self.stack[-1]
        #return self.stack[len(self.stack)-1]
    def dequeueCharacter(self):
        return self.queue[0]
        #return self.queue.pop(0)


# Read the string
w = input()

# Create the Palindrome class object
p = Palindrome()

for i in range(len(w)):
    # Push all the characters of string to stack
    p.pushCharacter(w[i])
    # Enqueue all the characters of string to queue
    p.enqueueCharacter(w[i])

f = True

"""
Pop the top character from stack
Dequeue the first character from queue
Compare both the characters
"""

for i in range(len(w)):
    if p.popCharacter() != p.dequeueCharacter():
        f = False
        break

# Finally print whether string is palindrome
if f:
    print("The word, " + w + ", is a palindrome.")
else:
    print("The word, " + w + ", is not a palindrome.")


"""
input:
racecar

output:
palindrome

problem:
# A palindrome is a "word, phrase, number, or other sequence of characters which reads the same backwards 
 and forwards." Can you determine if a given string, s, is a palindrome?

To solve this challenge, we must first take each character in s, enqueue it in a queue, and also push it onto 
a stack. Once that's done, we must dequeue the first character from the queue and pop the top character off 
the stack, then compare the two characters to see if they are the same; as long as the characters match, we 
continue dequeueing, popping, and comparing each character until our containers are empty (a non-match 
means s isn't a palindrome). 
"""
