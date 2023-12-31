class Maths:
    a = 0
    b = 0

    def sum(self):
        c = self.a+ self.b
        print("Sum is: ",c)

class Maths2(Maths):
    def product(self):
        prd = self.a * self.b
        print("Product is: ",prd)

mycls = Maths2(Maths)

mycls.a = 23
mycls.b = 7

mycls.sum()
mycls.product()