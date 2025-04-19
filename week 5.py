
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength
    
    def introduce(self):
        print(f"I am {self.name} and my power is {self.power}!")
    
    def fight(self):
        print(f"{self.name} fights with strength {self.strength}!")


class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength, flying_speed):
        super().__init__(name, power, strength)  
        self.flying_speed = flying_speed
    
    def fly(self):
        print(f"{self.name} flies at {self.flying_speed} km/h!")


hero1 = Superhero("Shadow Knight", "Invisibility", 90)
hero2 = FlyingSuperhero("Sky Guardian", "Flight", 85, 300)

hero1.introduce()
hero1.fight()

print("---")

hero2.introduce()
hero2.fight()
hero2.fly()
