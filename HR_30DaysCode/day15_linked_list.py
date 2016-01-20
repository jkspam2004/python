#!/usr/bin/python3
#
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-15-linked-list/copy-from/4669493
#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self,head,data): 
        # complete insert function
        new_node = Node(data)
        
        if head == None:
            head = new_node
        else:
            current = head
            print("current.next=", current.next, end= ' ') 
            while current.next != None:
                current = current.next
                
            current.next = new_node
            print("current.data=", current.data, end= ' ') 
        print("head.data=", head.data, "new_node.data=", new_node.data)
        return head

mylist = Solution()
T = int(input())
head = None

for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

mylist.display(head)
print()


"""
input:
4
2
3
4
1

output:
2 3 4 1

problem:
You are given a class Node in the editor which has one instance pointer next pointing to next node and an integer data to store the data in Node.

You are also given a pointer head pointing to the head node of a linked list and an integer data to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node. The given head pointer may be null, meaning that the initial list is empty.

"""

