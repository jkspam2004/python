#!/usr/bin/python3
fr = open('file_read.txt', 'r')

for line in fr:
    print(line, end='')

fw= open('file_write.txt', 'w')
fw.write("This is a test\n")
print(fr.read())
