import random

def randomVal():
    for val in range(0,10):
        randNum = random.randint(60,100)
        result = 'Score: {}: Your grade is '.format(randNum)
        if randNum > 60 and randNum < 70:
            grade = 'D'
            print result + grade
        elif randNum > 70 and randNum < 80:
            grade = 'C'
            print result  + grade
        elif randNum > 80 and randNum < 90:
            grade = 'B'
            print result  + grade
        else:
            grade = 'A'
            print result  + grade

randomVal()
