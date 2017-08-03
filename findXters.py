word_list = ['hello','world','my','name','is','Anna']
char = 'o'
word = 'name'
newList = []

for value in word_list:
    if value.find('o') > -1:
        newList.append(value)

print newList
