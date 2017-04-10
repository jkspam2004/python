# Docstring comments

```
>>> import mymodule
>>> help(mymodule)
```
 
Assuming this is file mymodule.py then this string, being the first statement in 
the file will become the mymodule modules docstring when the file is imported.    

The class's docstring
```
>>> help(mymodule.MyClass)
```

The method's docstring
```
>>> help(mymodule.MyClass.my_method)
```

The function's docstring
```
>>> help(mymodule.my_function)
```


```
This is an example of Google style docstring.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
```
