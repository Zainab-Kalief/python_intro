#1
def filterNumbers(value):
    if value >= 100:
        print "That's a big number!"
    else:
        print "That's a small number"

filterNumbers(value = 45)

#2
def filterWords(value):
    if len(value) >= 50:
        print "Long sentence"
    else:
        print "Short sentence"

filterWords(value = "Tell me and I forget. Teach me and I remember. Involve me and I learn.")

#3
def filterList(value):
    if len(value) >= 10:
        print "Big list!"
    else:
        print "Short list."

filterList(value = [3,5,7,34,3])
