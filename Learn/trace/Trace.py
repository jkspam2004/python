import inspect

class StackTrace(object):
    def __init__(self):
        pass

    # returns the input value, file, line number, and function of running program
    def trace(self, value):
        #return value, inspect.stack()[1][1], inspect.stack()[1][2], inspect.stack()[1][3]
        return value.__class__.__name__, __file__


'''
return value.__class__.__name__, __file__
'''
