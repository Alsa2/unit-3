class Pet:
    def __init__(self, name:str, price:int, type:str):
        self.name = name
        self.price = price
        self.type = type
    
    def get_price_tax(self):
        # 10 % tax
        return self.price * 1.1

class Goldfish(Pet):
    def __init__(self, brain:bool, name:str, price:int):
        super().__init__(name = name , price = price, type="Fish")
        self.brain = brain
        print("Goldfish created")

    def swim(self):
        return "I'm swimming straight" if self.brain else "I'm swimming upside down"
    
class Worm(Pet):
    def __init__(self, name:str, price:int):
        super().__init__(name = name , price = price, type="Worm")
        print("Worm created")

    def crawl(self):
        return "I'm crawling"
    

bob = Pet(name="Bob", price=3, type="Dog")
print(bob.get_price_tax())
carl = Goldfish(name="Carl", price=5, brain=True)
print(carl.get_price_tax())
print(carl.swim())

    
