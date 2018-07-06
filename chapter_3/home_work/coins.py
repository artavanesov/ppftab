# Coins

import random

tries = 0
tails = 0
eagle = 0

while tries != 100:
    tries += 1
    side = random.randint(1, 2)

    if side == 1:
        eagle += 1
    else:
        tails += 1

print("Eagle: ", eagle)
print("Tails: ", tails)
