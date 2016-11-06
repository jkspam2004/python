#!/usr/bin/python3
#
# Binary Search Trees
# You are given a pointer root pointing to the root of a binary search tree. Return the height of the tree. 
#
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-22-binary-search-trees

"""
      3  
     /  \
    2    5
   /    /  \
  1    4    6
             \
              7
"""
import pprint
#import Dumper

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root == None:
            print("root is none, data is", data)
            return Node(data)
        else:
            cur = Node(data)
            if data <= root.data:
                print("data %s is less than root %s" %(data, root.data))
                cur = self.insert(root.left, data)
                root.left = cur
            elif data > root.data:
                print("data %s is greater than root %s" %(data, root.data))
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root == None:
            return 0
        else:
            if self.getHeight(root.right) > self.getHeight(root.left):
                return 1 + self.getHeight(root.right)
            else:
                return 1 + self.getHeight(root.left)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
    print("root.data=", root.data)

#print(root.right)
print("final", root.data)
#print(Dumper.dump(root))

#height = myTree.getHeight(root)
#print(height)

"""
input: 
7
3
5
2
1
4
6
7

output:
4

explanation:
tree formed with give inputs

      3  
     /  \
    2    5
   /    /  \
  1    4    6
             \
              7

The maximum length root to leaf path is 3->5->6->7. There are 4 nodes in this path. Therefore the height of the binary tree = 4.


"""

