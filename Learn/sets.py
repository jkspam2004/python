""" Python sets: unordered unique elements  """
#!/usr/bin/python3

set1 = set()                    # initialize
set1.add("cat")                 # {'cat'} - adds one by one
set1.update(["dog", "elephant"])# {'cat', 'dog', 'elephant'} - adds a group of elements
set3 = set1.copy()              # {'cat', 'dog', 'elephant'} - copy the set

for item in set1:               # iterating over set
    print(item)                 # cat elephant dog

if "cat" in set1:               # check if item in set
    set1.remove("cat")          # {'dog', 'elephant'}

print("Item count:", len(set1)) # Item count: 2 
set1.discard("elephant")        # {'dog'} - removes an item
set1.remove("dog")              # set() - removes an item. throws error if item does not exist
isEmpty = len(set1) == 0        # True
print(isEmpty)
print(set1)

set2 = set([0, 1, 2, 3])        # {0, 1, 2, 3} - initialize
set2 = set(["elephant"])        # {'elephant'} - initialize

set2 = set("elephant")          # {'l', 'a', 'e', 'n', 't', 'h', 'p'}
isSubset = set2.issubset(set("elephanttrunk"))  # True
isSuperset = set2.issuperset(set("ant"))        # True
set2.remove("e")                # removes specified element
set2.pop()                      # removes any one (random) element
set2.clear()                    # clears set
print(set2)

# https://en.wikibooks.org/wiki/Python_Programming/Sets


