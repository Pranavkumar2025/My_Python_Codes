class Car:
    def __init__(self, make, model, year, color="Unknown"):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}, Color: {self.color}, Mileage: {self.mileage} miles")

    def drive(self, miles):
        print(f"Driving {miles} miles...")
        self.mileage += miles

# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Honda", "Accord", 2023, "Red")
print("Name of Car1 is: ",car1.make)
print("Model of Car2 is: ",car2.model)

# Displaying information about the cars
car1.display_info()
car2.display_info()

# Driving the cars and updating mileage
car1.drive(100)
car2.drive(150)

# Displaying updated information
car1.display_info()
car2.display_info()


