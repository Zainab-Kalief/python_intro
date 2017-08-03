#1
for value in range(1,1000):
    if value % 2 != 0:
        print value

#2
for value in range(5,1000000):
    if value % 5 == 0:
        print value

#3
a = [1, 2, 5, 10, 255, 3]
sum = 0

for value in a:
    sum += value

print sum

#4
b = [1, 2, 5, 10, 255, 3]
sum = 0

for value in b:
    sum += value

avg = sum / len(b)

print avg
