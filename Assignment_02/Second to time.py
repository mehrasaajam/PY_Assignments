
s = int(input("please enter the time according to second: "))

hour = int(s/3600)
minute = int((s-(hour*3600))/60)
second = int(s-(hour*3600)-(minute*60))

print("hour=", hour)
print("minute=", minute)
print("second=", second)
