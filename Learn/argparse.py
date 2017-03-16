import argparse
import sys

parser = argparse.ArgumentParser()
#parser.add_argument('classname')
#parser.add_argument('-x', action="store_true")
parser.add_argument('-x')

args = parser.parse_args()
#print args.classname
argStrings = sys.argv
print "argStrings", argStrings
opts = argStrings[1:len(argStrings)]
print "opts", opts
