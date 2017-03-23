# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")
print "__name__:", __name__

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

"""
Now, if you invoke the interpreter as

python one.py
The output will be

top-level in one.py
one.py is being run directly
If you run two.py instead:

python two.py
You get

top-level in one.py
one.py is being imported into another module
top-level in two.py
func() in one.py
two.py is being run directly
Thus, when module one gets loaded, its __name__ equals "one" instead of __main__.

http://stackoverflow.com/questions/419163/what-does-if-name-main-do


When the Python interpreter reads a source file, it executes all of the code found in it.

Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
"""
