
import random

dice1 = random.randint(1, 6)
print(dice1)

while dice1 == 6:
    dice2 = random.randint(0, 6)
    print(dice2)
    dice1 = dice2
 