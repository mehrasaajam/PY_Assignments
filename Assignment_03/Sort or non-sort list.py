
list = []

n=int(input("please enter number of list: "))

for i in range(n):
    list.append(input("please enter a number: "))

for i in range(1, n):
    if list[i] < list [i-1]:
        print("list is non-sorted")
        break
    else:
        continue

print("list is sorted")
