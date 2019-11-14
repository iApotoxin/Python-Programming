import random

def rollDice():
    return (1 + random.randrange(5), 1 + random.randrange(5))

d1, d2 = rollDice()
print (d1," ",d2)