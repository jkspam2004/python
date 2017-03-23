def fun(a, deleted="Any", notEqual=True):
    print "a is {}".format(a)
    print "deleted is {}".format(deleted)
    print "notEqual is {}".format(notEqual)

    operator = "$ne" if notEqual else "$eq"
    print "operator is {}".format(operator)
    print 


fun(6, 5) # notEqual is default
fun("one arg") # one positional arg, rest are defaults
fun("test 3", notEqual=False) # leave out deleted argument, passed keyword argument for notEqual
#fun("test 4", deleted=False, False) # SyntaxError: non-keyword arg after keyword arg
fun("test 4", deleted=False, notEqual=False) 
fun("test 5", notEqual=False, deleted=True) # switch ordering of keyword args 
