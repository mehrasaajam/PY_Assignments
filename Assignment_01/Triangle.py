
a=float(input("please enter first dimension of the triangle: "))
b=float(input("please enter second dimension of the triangle: "))
c=float(input("please enter third dimension of the triangle: "))

if a<b+c and b<a+c and c<a+b:
    print("drawing this triangle is possible")

else :
    print("drawing this triangle is impossible") 
