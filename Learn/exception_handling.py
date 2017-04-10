#!/usr/bin/python3
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    except:
        print("Unexpected error")
        raise
    else:
        """ this gets executed if try clause does not raise an exception """
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
    finally:
        """ always executed before leaving try statement whether exception raised or not """
        print("Goodbye, world")


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
