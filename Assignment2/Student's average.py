
n = 0
sum = 0

while True:

    x = (input("please inter student's grade (you can enter 'exit' to see student's average): "))

    if x == "exit":
        break

    else:
        y = float(x)
        sum = sum+y
        n = n+1
        average = sum/n

print("student's average is: ", average)
    

