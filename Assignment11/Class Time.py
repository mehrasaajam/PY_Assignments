class Time:

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        self.fix()

    def add(self, other):
        hour = self.h + other.h
        minute = self.m + other.m
        second = self.s + other.s
        result = Time(hour, minute, second)
        return result
    
    def sub(self, other):
        hour = self.h - other.h
        minute = self.m - other.m
        second = self.s - other.s
        result = Time(hour, minute, second)
        return result

    def time_to_sec(self):
        result = (self.h*3600) + (self.m*60) + self.s
        return result

    def gmt_to_tehran(self):
        hour = self.h + 3
        minute = self.m + 30
        second = self.s
        result = Time(hour, minute, second)
        return result

    def fix(self):
        
        if self.s >= 60:
            self.s -= 60
            self.m += 1

        if self.m >= 60:
            self.m -= 60
            self.h += 1

        if self.s < 0:
            self.s += 60
            self.m -= 1

        if self.m < 0:
            self.m += 60
            self.h -= 1

    def show(self):
        print(self.h, ":", self.m, ":", self.s)

def sec_to_time():
    s = int(input("Please enter seconds: "))
    hour = int(s/3600)
    minute = int((s-(hour*3600))/60)
    second = int(s-(hour*3600)-(minute*60))
    result = Time(hour, minute, second)
    result.show()

t1 = Time(6, 18, 8)
t1.show()

t2 = Time(4, 49, 53)
t2.show()

t3 = t1.add(t2)
t3.show()

t4 = t1.sub(t2)
t4.show()

print(t1.time_to_sec())

sec_to_time()
