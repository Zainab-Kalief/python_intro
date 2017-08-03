myList = ['magical unicorns',19,'hello',98.98,'world']
word = 'String: '
total = 0
listType = ''

for value in myList:
    if type(value) is str:
        word += value + ' '
    else:
        total += value

if all(isinstance(x, str) for x in myList):
    listType = "The array you entered is of string type"
elif all(isinstance(x, int) for x in myList):
    listType = "The array you entered is of integer type"
else:
    listType = "The array you entered is of mixed type"

print word
print total
print listType
