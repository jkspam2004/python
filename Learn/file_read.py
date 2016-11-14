#!/usr/bin/python
# an example of seek()

# Open a file
fh = open("foo.txt", "r")
print ("Name of the file: ", fh.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fh.readline() # This is 1st line
print("Read Line: %s" % (line))

# Again set the pointer to the beginning
#fh.seek(-17, 2) # This is 5th line
#fh.seek(-51, 2) # This is 3rd line
#fh.seek(-85, 2) # This is 1st line
#fh.seek(0, 0) # This is 1st line
#fh.seek(5, 0) # is 1st line
fh.seek(5, 1) # is 2nd line
line = fh.readline()
print("Read Line: %s" % (line))

# Close opened file
fh.close()


"""
fileObject.seek(offset[, whence])

offset -- This is the position of the read/write pointer within the file.

whence -- This is optional and defaults to 0 which means absolute file positioning, 
other values are 1 which means seek relative to the current position and 
2 means seek relative to the file's end.

"""
