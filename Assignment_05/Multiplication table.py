
def Multiplication_table(n, m):
   
    m_t = []
    for i in range(n+1):
        m_t.append([i]*(m+1))
    print(m_t)

    for i in range(0, n+1):

        for j in range(1, m+1):

            if i == 0:
                m_t[i][j] = j
            else:
                m_t[i][j] = m_t[0][j] * m_t[i][0]

    for x in m_t:
        print(x)
 
row = int(input("please enter n: "))
col = int(input("please enter m: "))
Multiplication_table(row, col)
