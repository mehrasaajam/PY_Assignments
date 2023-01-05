
import numpy as np 

def generate_rug():
    
    n = int(input("Please enter n: ")) 
    m = np.zeros((n,n)) 
    x = []
        
    if n % 2 == 0:
        print("Error: Please enter an odd number")
    else: 

        for ii in range(n, 0, -2):
            x.append((ii-1)//2)
        for jj in range(2, n, 2):
            x.append((jj)//2)

        for i in range(n):
            for j in range(i, n-i): 
                m[i,j] = x[i]
                m[n-1-i,j] = x[i]

        for j in range(n):
            for i in range(j, n-j): 
                m[i,j] = x[j]
                m[i,n-1-j] = x[j]
        print(m)

generate_rug()
