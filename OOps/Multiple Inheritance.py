class Product:
    c= "hello world"
    def product(self,a,b):
        print(f"Product of {a} and {b} is :", a*b)

class Sum:
    d = "Hello everyone"
    def sum(self,a,b):
        print(f"Sum of {a} and {b} is :", a+b)
    

class Operation(Product,Sum):# <-- this syntax is used for Multiple Inheritance in Python.

    def printstring(self):
        print(self.c)
        print(self.d)


myOperation = Operation()

myOperation.product(9,10)
myOperation.sum(23,43)
myOperation.printstring()
