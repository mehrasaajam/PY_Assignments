
def chess(n, m):

    for i in range(0, n):

        for j in range(0, m):

            if i % 2 == 0 and j % 2 == 0:
                print("# ", end = "")
            elif i % 2 != 0 and j % 2 != 0:
                print("# ", end = "")
            else:
                print("* ", end = "")
        print()
 
row = int(input("please enter n: "))
col = int(input("please enter m: "))
chess(row, col)
