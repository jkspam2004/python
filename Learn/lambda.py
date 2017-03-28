"""
lambda
"""

squared = lambda x: x**2
print squared(8) # 64

def increment(x):
    x += 2
    return lambda n: x * n


f = increment(10) # f = lambda function returned
print f(6) # 72, invoke lambda function 
print increment(5)(4) # 28

items = [2, 18, 9, 22, 17, 24, 8, 12, 27]

# returns elements to new list for which lambda function returned True (like Perl's grep)
filtered_list = filter(lambda x: x % 3 == 0, items)
print filtered_list # [18, 9, 24, 12, 27]

# returns elements to new list for which lambda function converted
mapped_list = map(lambda x: x * 2 + 10, items)
print mapped_list # [14, 46, 28, 54, 44, 58, 26, 34, 64] 

reduced = reduce(lambda x, y: x + y, items)
print reduced # 139


""" http://www.secnetix.de/olli/Python/lambda_functions.hawk """
