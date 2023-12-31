
class Maths:
    a = 0
    b = 0
    def Product(self):
        prd = self.a * self.b
        print("Product is 1st is: ", prd)# this line is not going to execute because it is Override method.
    
    def Sum(self):
        sum = self.a + self.b
        print("Sum is: ",sum)# this is also Override mthod but by using Super class in their inherit class we can acces it.



class Maths1(Maths):

    def Product(self):
        print("Product of second is: ", self.a *self.b)

    def Sum(self):
        super().Sum()# Super() -- method is helps in Overriding Process.
        print(f"Sum of {self.a} and {self.b} is : ", self.a+self.b)

Operation = Maths1()

Operation.a = 32
Operation.b = 23

Operation.Sum()
Operation.Product()



