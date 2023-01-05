class Fraction:

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def add(self, other):
        new_n = (self.n * other.d) + (other.n * self.d)
        new_d = (self.d * other.d)
        result = Fraction(new_n, new_d)
        return result 
        
    
    def sub(self, other):
        new_n = (self.n * other.d) - (other.n * self.d)
        new_d = (self.d * other.d)
        result = Fraction(new_n, new_d)
        return result 
            
    def mul(self, other):
        new_n = self.n * other.n
        new_d = self.d * other.d
        result = Fraction(new_n, new_d)
        return result 
            
    def div(self, other):
        new_n = self.n * other.d
        new_d = self.d * other.n
        result = Fraction(new_n, new_d)
        return result 

    def frac_to_num(self):
        result = self.n / self.d
        return result

    def simplification(self):

        for i in range(min(self.n, self.d), 1, -1):
            if self.n % i == 0 and self.d % i == 0:
                new_n = self.n / i
                new_d = self.d / i
                break
        else:
            new_n = self.n
            new_d = self.d
        
        result = Fraction(new_n, new_d)
        return result         

    def show(self):
        print(self.n , "/" , self.d)

f1 = Fraction(18, 5)
f1.show()

f2 = Fraction(13, 2)
f2.show()

f3 = f1.add(f2)
f3.show()

f4 = f1.sub(f2)
f4.show()

f5 = f1.mul(f2)
f5.show()

f6 = f1.div(f2)
f6.show()

print(f1.frac_to_num())

f8 = f1.simplification()
f8.show()
