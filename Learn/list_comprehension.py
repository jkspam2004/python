"""
list comprehension
"""


dict = { 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e' }
print(dict)

keys = [x for x in dict]
values = [dict[x] for x in dict]
print(keys, values)

gt2 = [x for x in dict if x > 2]
print(gt2)
