# two methods of performing the average of input numbers.

# method 1

total=0
count=0

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total/count
print('Average:', average)



# method 2