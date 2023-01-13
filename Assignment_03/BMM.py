
a = int(input("please enter first number: "))
b = int(input("please enter second number: "))

if a>b:

    for i in range(b, 0, -1):

        if a % i == 0 and b % i == 0:
            print("BMM =", i)
            break
        else:
            continue

else:
    
    for i in range(a, 0, -1):
        
        if a % i == 0 and b % i == 0:
            print("BMM =", i)
            break
        else:
            continue
