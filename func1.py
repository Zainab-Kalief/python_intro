#1
def numbers():
    for value in range(1,2000):
        if value % 2 == 0:
            print 'Number is ' + str(value) + '.' + 'This is an even number.'
        else:
            print 'Number is ' + str(value) + '.' + 'This is an odd number.'

numbers()

#2
def multiply(numbers, val):
    for value in range(len(numbers)):
        numbers[value] *= val
    return numbers

print multiply([1,2,3],2)

#3
def layered(arr):
]
    multiArry = []
    for val in arr:
        newArr = []
        for value in range(0,val):
            newArr.append(1)
        # print newArr
        multiArry.append(newArr)
    print multiArry

layered(multiply([1,2,3],2))
