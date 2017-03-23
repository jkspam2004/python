import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(
        #prog = "PROG", # program name, sys.argv[0] by default
        description = "A simple argument parser",
        epilog = "This is where you might put example usage"
    )

    """ positional argument. required """
    parser.add_argument('classname')

    """ optional arguments """
    # short option (1 character long with '-' as prefix)
    parser.add_argument('-a', action="store_true")
    parser.add_argument('-b', action="store_false")
    parser.add_argument('-x')
    parser.add_argument('-y', action="append") # stores values in list. -y 6 -y 7
                                               # y=['6', '7']
    # long option (more than one char long with '--' as prefix)
    parser.add_argument('-f', '--foo', action="store_true") # store default True
    parser.add_argument('-g', '--bar', action="store_false") # store default False
    parser.add_argument('-d', '--baz', action="store_const", const=35) # store default const 
    parser.add_argument('--new', help="new help")

    if len(sys.argv) == 1:
        #parser.print_usage()
        parser.print_help()
        #pass

    #parser.parse_args(['--help'])
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    print
    print "args: ", args

    argStrings = sys.argv
    opts = argStrings[1:len(argStrings)] # 0 is the filename
    print "classname: ", args.classname
    print "argStrings:", argStrings
    print "opts:", opts

    print "len argStrings:", len(argStrings)


"""
$ python argparsey.py hello  -x 5 -y 6 -y 7 -ab --new 10
args:  Namespace(a=True, b=False, bar=True, baz=None, classname='hello', foo=False, new='10', x='5', y=['6', '7'])
classname:  hello
argStrings: ['argparsey.py', 'hello', '-x', '5', '-y', '6', '-y', '7', '-ab', '--new', '10']
opts: ['hello', '-x', '5', '-y', '6', '-y', '7', '-ab', '--new', '10']
len argStrings: 11

~~~

$ python argparsey.py hello  -x5 --foo --bar --baz --new=10
args:  Namespace(a=False, b=True, bar=False, baz=35, classname='hello', foo=True, new='10', x='5', y=None)
classname:  hello
argStrings: ['argparsey.py', 'hello', '-x5', '--foo', '--bar', '--baz', '--new=10']
opts: ['hello', '-x5', '--foo', '--bar', '--baz', '--new=10']
len argStrings: 7

~~~

For short options (options only one character long), the option and its value can be concatenated
-x5

For long options (options with names longer than a single character), the option and value can also be passed as a single command-line argument, using = to separate them
--new=10

Several short options can be joined together, using only a single - prefix, as long as only the last option (or none of them) requires a value
-abx7
"""
