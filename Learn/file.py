fr = open('data.txt', 'r')

for line in fr:
    print(line, end='')

fw= open('data.txt', 'w')
fw.write("This is a test\n")
print(fr.read())
