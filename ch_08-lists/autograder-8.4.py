filename = input('Enter file name: ')
file = open(filename)

li = list()
for line in file:
    words = line.split()
    for each in words:
        if not each in li:
            li.append(each)
li.sort()
print(li)