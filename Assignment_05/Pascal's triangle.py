
def khp_triangle(n):

    kh_p = []
    for i in range(n):
        kh_p.append([1]*(i+1))

    for i in range(2, n):

        for j in range(1, i):
            kh_p[i][j] = kh_p[i-1][j-1] + kh_p[i-1][j]

    for x in kh_p:
        print(x)

khp_triangle(int(input("please enter n: ")))
