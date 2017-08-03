def draw_stars(arg):
    for value in arg:
        star = ''
        for val in range(0,value):
            star += '* '
        print star

draw_stars([4, 6, 1, 3, 5, 7, 25])

def draw_stars2(arg):
    for value in arg:
        if type(value) is int:
            star = ''
            for val in range(0,value):
                star += '*'
            print star
        else:
            first = ''
            for val in range(len(value)):
                first += value[0].lower()
            print first

draw_stars2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
