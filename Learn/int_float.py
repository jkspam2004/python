confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1.0] = 4 # if two numbers compare, they can be used interchangeably.  1 and 1.0 are the same here.  hask key of 1 overwritten with value 4

sum = 0
for k in confusion:
    print "b4: %s %s %s" % (k, type(k), sum)
    sum += confusion[k]
    print "after: %s %s" % (k, sum)
    

print sum
