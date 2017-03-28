#!/usr/bin/python3

# lists

n = [1, 3, 15]
n[1] *= 2
print(n)

# append
n.append(4)
print(n)

# pop:  n.pop(index) - remove item at index and return item
popped = n.pop(1)

print("list after pop", n)
print("popped", popped)

# remove: n.remove(item) - remove the item if it is found
n.remove(1) # removes 1 from the list
print(n)

# del: del(n[index]) - like pop, removes item at index, but doesn't return item 
del(n[1])
print(n)

# functions
n = "Hello"
def string_function(s):
    return s + 'world'

print(string_function(n))

# concatenating lists
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
# prints [1, 2, 3, 4, 5, 6]

# list of lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
    results = []
    for numbers in lists:
        for num in numbers:
            results.append(num)

    return results


print(flatten(n))

# for loop

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(arr)

# input
#6
#1 2 3 4 10 11

