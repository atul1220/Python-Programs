fhand = open('test.txt')
for line in fhand:
    if line.startswith('From'):
        print(line)
