def multipleTable():

    for value in range(1,13):
        mult = 1
        table = ''
        while mult < 13:
            table += ' ' + str(value * mult)
            mult += 1
        print table

multipleTable()
