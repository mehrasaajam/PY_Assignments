
a = int(input("please enter first number: "))
b = int(input("please enter second number: "))


for i in range(1000):
    ii = i + 1
    aa = a * ii

    for j in range(1000):
        jj = j +1
        bb = b * jj
        
        if aa == bb:
            print("KMM =", aa)
            break
        else:
            continue

    if aa == bb:
        break
