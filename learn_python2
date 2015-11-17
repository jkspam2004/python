
my_int = 7
my_int2 = 8
my_float = 1.23
my_bool = True
spam = True
eggs = False
my_str = "foo"

print "my int variables are %s and %s" % (my_int, my_int2)
print "my string variable is " + my_str

# integer division in python 2.7
first = 5
second = 2

int_result = 5/2
int_result2 = 5//2
float_result = 5.0/2
float_result2 = float(5)/2
remainder = 5%2

print "integer division of 5/2 is %s" % (int_result)
print "integer division of 5//2 is %s" % (int_result2)
print "float division of 5.0/2.0 is %s" %(float_result)
print "float division of float(5)/2 is %s" %(float_result2)
print "remainder division of 5%%2 is %r\n" %(remainder)

# indent four spaces
def spam():
    eggs = 12
    return eggs
        
print "return from spam function is %s" % spam()

""" multi line
comment
end here """

# total meal cost
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + (meal * tip)

print "total meal cost is %.2f" % total 


# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'



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

print "fifth letter in monty with index 4 is " + fifth_letter


# string functions
string = "Norwegian Blue"
length = len(string)
small = string.lower()
big = string.upper()

print "string=" + string 
print "length=%s" % (length)
print "lowered=" + small 
print "uppered=" + big

# turn non-string to string
pi = 3.14
print str(pi)

# printing variables
the_machine_goes = "Ping!"
print the_machine_goes

# string concatenation
print "Spam " + "and " + "eggs"

# string formatting with %
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

# datetime
from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)


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
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)




# slice
s = "Charlie"

print "orig=" + s
print s[0]
# will print "C"

print s[1:4]
# will print "har

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
    print i
print 'Blastoff'

friends = [ "Joseph", "Sally", "Glen" ]
print "friends are", friends
print "my friend at index 1 is", friends[1]

# length of list, len()
print "i have this many friends (using len()) =", len(friends)

# assignment to list
friends[1] = "Boo"
print "now my new friend is", friends[1]

# range function returns a list of numbers that range from zero to one less than the parameter
print "range of 4 is", range(4)
print "range of length of friends is", range(len(friends))

for friend in friends :
    print "looping through friends:", friend

for i in range(len(friends)) :
    print "looping with range and index at %s:" %(i), friends[i]

nums_to_counts = [0] * 3
print nums_to_counts

# type
sval = '123'
print(type(sval))


# pig latin
pyg = 'ay'
original = raw_input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print "pig latin=",  new_word
else:
    print 'empty'

