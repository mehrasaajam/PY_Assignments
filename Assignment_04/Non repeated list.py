
list1 = []
list2 = []

n=int(input("please enter number of list: "))

for i in range(n):
    list1.append(input("please enter a number: "))

for i in range(n):

    if list1[i] not in list2:
        list2.append(list1[i])
        print(list2[i], end = ", ")
        