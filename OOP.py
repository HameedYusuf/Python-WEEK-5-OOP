# 1. Defining the Smartphone class
class Smartphone:
    def __init__(self, brand, model, battery_percentage):
        """Constructor to initialize attributes."""
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def charge(self, amount):
        """Charges the phone by the specified amount."""
        self.battery_percentage = min(100, self.battery_percentage + amount)
        print(f"Charging... Battery is now at {self.battery_percentage}%")

    def make_call(self, number):
        """Simulates making a call."""
        if self.battery_percentage > 0:
            print(f"Calling {number}...")
        else:
            print("Battery is too low to make a call.")

# 2. Inheriting from Smartphone and adding a special feature for a GamingPhone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_percentage, ram_size):
        """Constructor for GamingPhone that adds a new attribute (ram_size)."""
        super().__init__(brand, model, battery_percentage)
        self.ram_size = ram_size

    def play_game(self, game_name):
        """Simulates playing a game and drains battery."""
        if self.battery_percentage > 10:
            print(f"Playing {game_name} with {self.ram_size}GB RAM...")
            self.battery_percentage -= 10  # Playing a game drains the battery
        else:
            print("Battery too low to play games.")

# Example usage
print("Smartphone example:")
phone = Smartphone("Samsung", "Galaxy S23", 50)
phone.charge(30)
phone.make_call("123-456-7890")

print("\nGamingPhone example:")
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 80, 16)
gaming_phone.play_game("PUBG Mobile")





# 2 Assignment
# 1. Base class for vehicles
class Vehicle:
    def move(self):
        """Generic move method for vehicles."""
        pass

# 2. Car class inheriting from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# 3. Plane class inheriting from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# 4. Bicycle class inheriting from Vehicle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# 5. Function that demonstrates polymorphism
def vehicle_move(vehicle):
    vehicle.move()

# 6. Create instances of each vehicle
car = Car()
plane = Plane()
bicycle = Bicycle()

# 7. Polymorphism in action: Call move() on different vehicles
print("Polymorphism example:")
vehicle_move(car)        # Output: Driving 🚗
vehicle_move(plane)      # Output: Flying ✈️
vehicle_move(bicycle)    # Output: Pedaling 🚲
