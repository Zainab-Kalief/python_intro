#1
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
newWord = words.replace('day', 'month')
print newWord

#2
x = [2,54,-2,7,12,98]
print max(x)
print min(x)

#3
y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]
newX = [y[0], y[len(y)-1]]
print newX

#4
z = [19,2,54,-2,7,12,98,32,10,-3,6]
zSorted = sorted(z)
count = len(zSorted)

half1 = [zSorted[0:count/2]]

half2 = zSorted[count/2:count-1]

half2.insert(0, half1)
print half2
