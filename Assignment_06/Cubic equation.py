
def Cubic_equation(a, b, c, d):
    
    if a == 0:
        print("'a' must ne non-zero")
    elif b == 0 and c == 0 and d == 0:
        print("0")
    else:
        delta0 = (b**2) - (3*a*c)
        delta1 = (2*b**3) - (9*a*b*c) + (27*a**2*d)
        c = ((delta1 + ((delta1**2)-(4*delta0**3))**0.5)/2)**(1/3)
        co1 = complex(-1, (3**0.5))
        co2 = complex(-1, -(3**0.5))
        u = [1, co1/2, co2/2]
        
        for k in range(3):
            x = (-1/(3*a))*(b + c*u[k] + (delta0/(c*u[k])))
            print(x)

a = int(input("please enter a: "))
b = int(input("please enter b: "))
c = int(input("please enter c: "))
d = int(input("please enter d: "))
Cubic_equation(a, b, c, d)
    