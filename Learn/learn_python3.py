#!/usr/bin/python3
## python 3
#

my_int = 7
my_int2 = 8
my_float = 1.23
my_bool = True
spam = True
eggs = False
my_str = "foo"

print("1. my int variables are %s and %s" % (my_int, my_int2))
print("2. my string variable is " + my_str)

# integer division in python 2.7
first = 5
second = 2

int_result = 5/2
int_result2 = 5//2
float_result = 5.0/2
float_result2 = float(5)/2
remainder = 5%2

print("3. integer division of 5/2 is %s" % (int_result))
print("4. integer division of 5//2 is %s" % (int_result2))
print("5. float division of 5.0/2.0 is %s" %(float_result))
print("6. float division of float(5)/2 is %s\n" %(float_result2))
print("7. remainder division of 5%%2 is %s\n" %(remainder))

# indent four spaces
def spam():
    eggs = 12
    return eggs
        
print("8. return from spam function is %s" % spam())

""" multi line
comment
end here """

# total meal cost
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + (meal * tip)

print("9. total meal cost is %.2f" % total)


# The string below is broken. Fix it using the escape backslash!

print('This isn\'t flying, this is falling with style!')



"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print("10. fifth letter in monty with index 4 is " + fifth_letter)


# string functions
string = "Norwegian Blue"
length = len(string)
small = string.lower()
big = string.upper()

print("11. string=" + string) 
print("12. length=%s" % (length))
print("13. lowered=" + small)
print("14. uppered=" + big)

# turn non-string to string
pi = 3.14
print("15. ", str(pi))

# printing variables
the_machine_goes = "Ping!"
print("16. ", the_machine_goes)

# string concatenation
print("17. ", "Spam " + "and " + "eggs")

# string formatting with %
string_1 = "Camelot"
string_2 = "place"

print("18. Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

# datetime
from datetime import datetime
now = datetime.now()

print('19. %s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))


"""
     Boolean Operators
------------------------      
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""


# Make me true!
bool_three = 10 + 5 >= 5 + 10

# if statements
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print("21. ", greater_less_equal_5(4))
print("22. ", greater_less_equal_5(5))
print("23. ", greater_less_equal_5(6))




# slice
s = "Charlie"

print("24. orig=" + s)
# will print "C"
print("25. ", s[0])

# will print "har
print("26. ", s[1:4])

# will print "Char"
print("27. ", s[0:-2])

# will print "ie"
print("28. ", s[-2:])


""" more slice
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array

a[start:end:step] # start through not past end, by step

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

"""


# lists
for i in [5, 4, 3, 2, 1] :
    print(i)
print('29. Blastoff')

friends = [ "Joseph", "Sally", "Glen" ]
print("30. friends are", friends)
print("31. my friend at index 1 is", friends[1])

# length of list, len()
print("32. i have this many friends (using len()) =", len(friends))

# assignment to list
friends[1] = "Boo"
print("33. now my new friend is", friends[1])

# appending to list
friends.append('Mike')
print("34. added one more friend", friends)

# insert into a list
animals = ["ant", "bat", "cat"]
print("35. ", animals.index("bat"))
animals.insert(1, "dog")
print("36. ", animals)

# list slice
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first  = suitcase[0:2]  # The first and second items (index zero and one)
print("37. ", first)

# split string into an array of chars
string = 'hippo'
string_list = list(string)
print("38. my string hippo expanded to an array of chars with 'list'", string_list)

# range function returns a list of numbers that range from zero to one less than the parameter
print("39. range of 4 is", range(4))
print("40. range of length of friends is", range(len(friends)))

for friend in friends :
    print("41. looping through friends:", friend)

for i in range(len(friends)) :
    print("42. looping with range and index at %s:" %(i), friends[i])

nums_to_counts = [0] * 3
print("43. ", nums_to_counts)

for i in range(1,5):
    print(i)

# range()
range(6)     # => [0,1,2,3,4,5]
range(1,6)   # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
"""
range(stop)
range(start,stop)
range(start,stop,step)
Each item increases by step (step defaults to 1)
"""

# type
sval = '123'
print("44. ", type(sval))

# function and type
def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"
print("45. ", distance_from_zero(-10))

# importing module
import math
print("46. ", math.sqrt(25))

# importing just the sqrt function
from math import sqrt
print("47. ", sqrt(25))

# breaking out of a loop
i = 0
while i < 5:
    if i == 3:
        print('48. done and break')
        break
    i += 1
    print('49. while', i)


# converting list to string

#By using ''.join

list1 = ['1', '2', '3']
str1 = ''.join(list1)

#Or if the list is of integers, convert the elements before joining them.

list1 = [1, 2, 3]
str1 = ''.join(str(e) for e in list1)


# formatting decimal precision
print("50. formatting to 3 decimal places", format(2.5, '.3f'))

# sort function. sort() modifies list rather than returning new list
animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
    print("51. ", animal)


# if statements
x=3
if x > 0 :
    print('52. x is a positive number')
elif x < 0 :
    print('53. x is a negative number')
else :
    print('54. x is 0')

# try and except
# if the code in the 'try' works, then the 'except' is skipped
# if the code in the 'try' fails, then it jumps to the 'except' block
test = input("Enter an integer: ")
try:  
   test = int(test)  
except:  
   print("55. Invalid entry.")
   quit()  
result = test * 2  
print("56. ", result) 

astr = 'Bob'
try:
    print('57. Hello')
    istr = int(astr)
    print('58. There')
except:
    istr = -1
print('59. Done', istr)


# importing module
import math
print(math.sqrt(25))

# pig latin
pyg = 'ay'
original = input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print("pig latin=",  new_word)
else:
    print('empty')


# dictionaries aka "hash"
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print(residents['Puffin']) # Prints Puffin's room number

# dictionaries and list are mutable (can be changed after they are created)
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print(menu['Chicken Alfredo'])

# Add some dish-price pairs to menu!
menu['Spaghetti'] = 12.30
menu['Penne with Bolognese'] = 16.50
menu['Cheese pizza'] = 13.75

print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

# removing item from hash
del menu['Cheese pizza']
print(menu)

# removing item from a list
backpack = ['xylophone', 'candy', 'tent', 'bread loaf']
backpack.remove('candy')
print("items in backpack", backpack)


# more hash stuff
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
# Sorting the list found under the key 'pouch'
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pouch'].sort() 

# remove dagger from backpack
inventory['backpack'].remove('dagger')

# add 50 to gold
inventory['gold'] += 50

print("printing the hash")
print(inventory)

# loop through items in a hash
print("looping through inventory hash")
for key in inventory:
    print("key=",key, ", values=", inventory[key])


# more hashes
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for item in prices:
    print(item)
    print("price: %s" % prices[item])
    print("stock: %s" % stock[item])

# more practice with hashes
# While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero.
# if item is in stock, add price to total and subtract one from item's stock count
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(food):
    total = 0

    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1

    return total

print("bill for banana", compute_bill(['banana']))
print("bill for apple", compute_bill(['apple']))
print("final stock is", stock)

# strip() method
# returns a copy of the string in which all chars have been stripped from the beginning and the end of the string (default whitespace characters)
str = "0000000this is string example....wow!!!0000000";
print(str.strip( '0' ))

print('concat' + 'me')
print('comma', 'me')

# enumerate produces the index and the element of each loop
fruits = [ 'apples', 'oranges', 'bananas', 'strawberries']
for index, item in enumerate(fruits):
    print(index, item)
