
num_list = []

while True:
    a = input("Enter a number od list: ")

    if a == "finish":
        break
    else:
        num_list.append(int(a))

for i in range((len(num_list)//2)):
    if num_list[i] != num_list[(len(num_list)-1-i)] :
        state = "false"
        print("This list is unsymmetric")
        break
    else:
        state = "true"

if state == "true":
    print("This list is symmetric")
