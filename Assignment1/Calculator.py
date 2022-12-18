
import math

print("welcome to my calculator")
print("in my calculator you can select following operators")
print("+:summation")
print("-:subtraction")
print("*:multiplication")
print("/:division")
print("sqrt:square root")
print("log:logarithm")
print("sin:sinus")
print("cos:cosine")
print("tan:tangent")
print("cot:cotangent")
print("factorial")
op=input("please enter your target operator: ")

if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("please enter first number: "))
    b = float(input("please enter second number: "))

elif op == "factorial":
    a = int(input("please enter integer number: "))

elif op == "sin" or op == "cos" or op == "tan" or op == "cot":
    aa = float(input("please enter a number(degree): "))
    a = aa*math.pi/180

else:
    a = float(input("please enter a number: "))

if op == "+":
    result = a+b

elif op == "-":
    result = a-b

elif op == "*":
    result = a*b

elif op == "/":   
    result = a/b

elif op == "sqrt":
    if a < 0:
        result = "this operation for negetive number is unavalable"
    else:
        result = math.sqrt(a)
    
elif op == "log":   
    result = math.log(a)

elif op == "sin":   
    result = math.sin(a)

elif op == "cos":   
    result = math.cos(a)

elif op == "tan":   
    result = math.tan(a)

elif op == "cot":   
    result = math.cot(a)

elif op == "factorial":
    if a < 0:
        resut = "this operation for negetive number is unavalable"
    else:
        result = math.factorial(a)

print(result)
