
def Cubic_equation(a, b, c, d):
    
    if a == 0:
        print("'a' must ne non-zero")
    elif b == 0 and c == 0 and d == 0:
        print("0")
    else:
        delta0 = (b**2) - (3*a*c)
        delta1 = (2*b**3) - (9*a*b*c) + (27*a**2*d)
        C = ((delta1 + ((delta1**2)-(4*delta0**3))**0.5)/2)**(1/3)
        co1 = complex(-1, (3**0.5))
        co2 = complex(-1, -(3**0.5))
        u = [1, co1/2, co2/2]

        for k in range(3):
            x = (-1/(3*a))*(b + C*u[k] + (delta0/(C*u[k])))
            print(x)

a = float(input("please enter a: "))
b = float(input("please enter b: "))
c = float(input("please enter c: "))
d = float(input("please enter d: "))
Cubic_equation(a, b, c, d)
    