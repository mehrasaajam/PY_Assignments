
from math import factorial 

a = int(input("please enter your number: "))

for i in range(a):

    if factorial(i) == a:
        print("OK")
        break
    elif factorial(i) > a:
        print("NO")
        break
    elif factorial(i) < a:
        continue
