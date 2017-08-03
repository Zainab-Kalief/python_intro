import random

def coinToss():
    head = 0
    tail = 0
    for attempt in range(1,10):
        side = round(random.random())
        if side == 1:
            head += 1
            if head > 1:
                print "Attempt #{} Throwing a coin. It's a head! Got {} heads so far & {} tails".format(attempt,head,tail)
            else:
                print "Attempt #{} Throwing a coin. It's a head! Got {} head so far & {} tails".format(attempt,head,tail)
        else:
            tail += 1
            if tail > 1:
                print "Attempt #{} Throwing a coin. It's a tail! Got {} heads so far & {} tails".format(attempt,head,tail)
            else:
                print "Attempt #{} Throwing a coin. It's a tail! Got {} head so far & {} tail".format(attempt,head,tail)

coinToss()
