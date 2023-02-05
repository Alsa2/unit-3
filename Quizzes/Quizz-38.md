# Quizz 38

## Code:
    
```python
import random
import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def  __repr__(self) -> str:
        return f"Coordinate(x={self.x}, y={self.y})"


class City:
    def __init__(self, name:str, location:Coordinate):
        self.name = name
        self.location = location

    def __repr__(self) -> str:
        return f"City(name={self.name}, location={self.location})"



class Country:
    def __init__(self, name:str):
        self.cities = []
        self.name = name

    def add_city(self, city:City):
        if isinstance(city, City):
            self.cities.append(city)
        else:
            raise TypeError("City expected")
        self.cities.append(city)
    def remove_cities(self, city:City):
        self.cities.remove(city)
    def distance_cities(self, city1:City, city2:City):
        return abs(city1.location.x - city2.location.x) + abs(city1.location.y - city2.location.y)
    def plot_cities(self):
        x = []
        y = []
        for i in self.cities:
            x.append(i.location.x)
            y.append(i.location.y)
            plt.text(i.location.x + 2, i.location.y, i.name)        
        plt.plot(x, y, 'ro')
        plt.show()
    def __repr__(self) -> str:
        return f"Country(cities={self.cities})"


city_name = ["Moscow", "Vladivostok", "Krasnoyarsk", "Kazan", "Khabarovsk", "Novosibirsk", "Yekaterinburg", "Samara", "Omsk", "Rostov-on-Don", "Ufa", "Chelyabinsk", "Voronezh", "Perm", "Krasnodar", "Volgograd", "Saratov", "Tyumen"]
country = Country("Russia")
for i in range(len(city_name)):
    country.add_city(City(city_name[i], Coordinate(random.randint(0, 100), random.randint(0, 100))))
print(country)

country.plot_cities()
```
## Proof:

![](/Images/quizz38-proof.png)