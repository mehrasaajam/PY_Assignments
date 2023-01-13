
list = []

n=int(input("please enter number of list: "))

for i in range(n):
    list.append(input("please enter a number: "))

for i in range(n-1, -1, -1):
    print(list[i], end = ", ")
   