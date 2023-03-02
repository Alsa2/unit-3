import math

class Wheel:
    """Represent a wheel with size and material attributes"""
    
    def __init__(self, size, material):
        self.size = size
        self.material = material

    def get_size(self):
        """Returns the size of the wheel"""
        return self.size
    
    def get_material(self):
        """Returns the material of the wheel"""
        return self.material
    
    def get_perimeter(self):
        """Calculates the perimeter of the wheel"""
        return 2 * math.pi * self.size

    def get_km_per_rotation(self):
        """Calculates how many kilometers the wheel can do in one rotation"""
        return self.get_perimeter() / 100000

    def __repr__(self):
        return f"Wheel({self.size})"
        
        
class Bicycle:
    """Defines a bicycle revolved around a wheel""" 

    def __init__(self, wheel):
        self.wheel = wheel

    def ride(self):
        """Ride the bicycle with given wheel attributes"""
        print(f"Riding a bicycle with a {self.wheel.get_size()} wheel")
        print(f"Riding a bicycle with a {self.wheel.get_material()} frame")
        print(f"Riding a bicycle with a {self.wheel.get_perimeter()} perimeter")
        print(f"Riding a bicycle with a {self.wheel.get_km_per_rotation()} km per rotation")

    def __repr__(self):
        return f"Bicycle({self.wheel})"

wheel = Wheel(26, "aluminum")
bicycle = Bicycle(wheel)
bicycle.ride()
