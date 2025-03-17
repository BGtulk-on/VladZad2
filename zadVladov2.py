class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
    def eat(self):
        print(f"{self.name} is eating.")



class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")



class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps.")
        
budito = Dog("Buddy")
wishekrs = Cat("Whiskers")

twiiky = Bird("Twiiky")




budito.speak()
wishekrs.speak()
twiiky.speak()
budito.eat()
