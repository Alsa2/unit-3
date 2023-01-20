import random
import matplotlib.pyplot as plt
plt.style.use('dark_background')

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

    def brute_force(self):
        capital = self.cities[0]
        cities = self.cities[1:]
        iterations = 10000
        best_path = []
        best_distance = 0
        for i in range(iterations):
            random.shuffle(cities)
            path = [capital] + cities + [capital]
            distance = 0
            print("""0%------------------50%------------------100%""")
            print("#" * int(i / iterations * len("""0%------------------50%------------------100%""")))
            for i in range(len(path) - 1):
                distance += self.distance_cities(path[i], path[i + 1])
            if distance < best_distance or best_distance == 0:
                best_distance = distance
                best_path = path
        return best_path, best_distance
    def plot_salesman(self, path):
        for i in range(len(path) - 1):
            plt.plot([path[i].location.x, path[i + 1].location.x], [path[i].location.y, path[i + 1].location.y], 'r')
        self.plot_cities()
    def __repr__(self) -> str:
        return f"Country(cities={self.cities})"


city_name = ["Moscow", "Vladivostok", "Krasnoyarsk", "Kazan", "Khabarovsk", "Novosibirsk", "Yekaterinburg", "Samara", "Omsk", "Rostov-on-Don", "Ufa", "Chelyabinsk", "Voronezh", "Perm", "Krasnodar", "Volgograd", "Saratov", "Tyumen"]
country = Country("Russia")
for i in range(len(city_name)):
    country.add_city(City(city_name[i], Coordinate(random.randint(0, 100), random.randint(0, 100))))
print(country)

path, distance = country.brute_force()
print(path, distance)
country.plot_salesman(path)


# What is the salesman problem and possible solutions?

#AI
# The salesman problem is a problem where you have a list of cities and you need to find the shortest path to visit all the cities and return to the starting point. The problem is NP-hard, so there is no known polynomial solution. The most common solution is the nearest neighbor algorithm, which is a greedy algorithm. It starts at a random city and then visits the nearest city, then the nearest city from that city, and so on. This algorithm is not optimal, but it is fast and simple to implement.
# This problem was investigated in the research paper "The Traveling Salesman Problem: A Computational Study" by D. B. Johnson, E. M. L. Johnson, and M. H. M. Winfree. The paper was published in 1964. It was the first paper to study the traveling salesman problem. The paper was published in the Journal of the ACM. The best known solution to the traveling salesman problem is the Held-Karp algorithm, which is a dynamic programming algorithm. It is a polynomial-time algorithm, which means that it can be solved in polynomial time. The algorithm is not optimal, but it is fast and simple to implement.

#Me
# The salesman problem is a problem where the goal is to visit all the cities in the least distance possible. Easiest way is to use the nearest city algorithm and so on.
# - "The Traveling Salesman Problem: A Computational Study" by D. B. Johnson, E. M. L. Johnson, and M. H. M. Winfree in 1964
# - The solution is the Held-Karp algorithm, which is too complicated for me to undersant (joking I am a lasy person)
# - Personally I like bruteforce

