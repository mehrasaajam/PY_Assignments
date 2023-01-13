
n = int(input("please enter n (the number of algorithm sentences): "))

if n < 0:
    print("your select must be positive and non-zero")

f1 = 1
f2 = 1

if n == 1:
    print(f1)

elif n == 2:
    print(f1, end = ", ")
    print(f2)

else:

    for i in range (1, n+1):
        f3 = f1+f2
        print(f1, end = ", ")
        f1 = f2
        f2 = f3
