# file main_one.py
def func():
    print("func() in main_one.py")

print("top-level in main_one.py")

if __name__ == "__main__":
    print("main_one.py is being run directly")
else:
    print("main_one.py is being imported into another module")

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
"""
