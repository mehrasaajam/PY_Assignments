
name=input("please enter student's name: ")
family=input("please enter student's family: ")

grade1=float(input("please enter first grade: "))
grade2=float(input("please enter second grade: "))
grade3=float(input("please enter third grade: "))

average=(grade1+grade2+grade3)/3

print("average is equal to ", average)

if average>=17:
    print ("student's status is great")

elif average<17 and average>=12:
    print("student's status is normal")

elif average<12:
    print ("student's status is fail")
