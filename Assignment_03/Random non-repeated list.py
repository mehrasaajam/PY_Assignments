
import random

list = []

n = int(input("please enter integer number of list: "))

a = int(input("please enter integer number of lower bound: "))
b = int(input("please enter integer number of upper bound: "))

if n>b-a:
    print("there are'nt exist 'n' non-repeated integer numbers in [a, b]!")

else:
    while len(list)<n:
        x = random.randint(0, 1000)

        if x in list:
            continue

        else:
            list.append(x)

    print(list)
    