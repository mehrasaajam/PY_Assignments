class Complex:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        a_new = self.a + other.a
        b_new = self.b + other.b
        x = Complex(a_new, b_new)
        return x
        
    def mul(self, other):
        a_new = (self.a * other.a) - (self.b * other.b)
        b_new = (self.a * other.b) + (self.b * other.a)
        x = Complex(a_new, b_new)
        return x
            
    def sub(self, other):
        a_new = self.a - other.a
        b_new = self.b - other.b
        x = Complex(a_new, b_new)
        return x

    def show(self):

        if self.b >= 0:
            print(self.a, "+", self.b, "i")
        else:
            print(self.a, self.b, "i")

x1 = Complex(3, 4)
x1.show()

x2 = Complex(2, -7)
x2.show()

x3 = x1.add(x2)
x3.show()

x4 = x1.sub(x2)
x4.show()

x5 = x1.mul(x2)
x5.show()
