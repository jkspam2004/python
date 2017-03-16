""" splat operators
    * or star args, varargs, gather parameter (in function definition), scatter operator (function invocation), positional expansion
    ** or **kwargs, keyword args, keyword expansion

    http://agiliq.com/blog/2012/06/understanding-args-and-kwargs/
"""

""" what '*' means from inside a function call 
pass in a list of values to function call
fun_call(*values) 
"""
def fun1(a, b, c):
    print a, b, c

list1 = [1, 2, 3]

# function call with '*' as argument 
fun1(*list1) # 1, 2, 3
# list1 gets unpacked as positional arguments and passed to function

list1 = [5,7]
# positional argument and star arg
fun1(1, *list1) # 1, 5, 7

""" what '*args' means inside a function definition 
input: positional argument values
def fun_def(*args):
    args will be a tuple
"""
def fun2(*myargs):
    print myargs # myargs is a tuple

# receives a tuple containing positional arguments
fun2(1) # (1,)
fun2(1, 2, 3) # (1, 2, 3)

# formal parameter and star arg
def fun3(a, *myargs):
    print "a is {}".format(a)
    print "myargs is {}".format(myargs)

fun3(1, 2, 3, 4) # a is 1 
                 # myargs is (2, 3, 4)

def calculate_sum(*args):
    print "sum args {}".format(args)
    return sum(args)

def ignore_firstargs_calculate_sum(a, *iargs):
    print "iargs {}".format(iargs)
    required_sum = calculate_sum(*iargs)
    print "sum is", required_sum

ignore_firstargs_calculate_sum(3,1,2,6) # iargs (1, 2, 6)
                                        # sum args (1, 2, 6)
                                        # sum is 9

""" what '**' does from inside a function call 
pass a dictionary to function call
fun_call(**dict_values) 
"""

def funfun(a, b, c):
    print a, b, c

funfun(7, c=9, b=8) # 7, 8, 9
d = {'c': 21, 'b': 20}

# unpacked the dictionary and passed the items in the dictionary as keyword arguments to the function
funfun(7, **d) # 7, 20, 21

""" what '**kwargs' means inside a function definition
input: key, value pairs 
def fun_def(**kwargs) 
"""

def fun(a, **myargs): # myargs receives a dictionary
    print a, myargs 

fun(1, b=4, c=5)      # 1, {'c': 5, 'b': 4} 
fun(2, b=6, c=7, d=8) # 2, {'c': 7, 'b': 6, 'd': 8}


def funargs(a, **kwargs):
    print "a is", a
    if kwargs:
        print "We expect kwargs 'b' and 'c' in this function"
        print "b is", kwargs['b']
        print "c is", kwargs['c']

    print

funargs(1, b=3, c=5) # 1 is a positional argument, b and c are keyword arguments
# a is 1                  
# We expect kwargs 'b' and 'c' in this function
# b is 3
# c is 5

d = {'b': 100, 'c': 102}
funargs(2, **d)
# a is 2
# We expect kwargs 'b' and 'c' in this function
# b is 100
# c is 102

funargs(17) # a is 17


""" more practice """

def funstuff(*args, **kwargs):
    print "args is {}".format(args)
    print "kwargs is {}".format(kwargs)

funstuff(71, 72) # args is (71, 72) 
                 # kwargs is {}
funstuff(35, 57, b=7, c=10) # args is (35, 57)
                            # kwargs is {'c': 10, 'b': 7}
