class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def work(self):
        print(f"{self.name} is working.")
        
    def take_break(self):
        print(f"{self.name} is taking a break.")

class Manager(Employee):
    def work(self):
        print(f"{self.name} (Manager) is managing the team.")

class Developer(Employee):
    def work(self):
        print(f"{self.name} (Developer) is writing code.")

class Intern(Employee):
    def work(self):
        print(f"{self.name} (Intern) is learning.")

if __name__ == "__main__":
    john = Manager("John Wick", 50000)
    alice = Developer("Alice Waine", 3000000)
    bob = Intern("Bob Marti", 5)
    
    john.work()
    john.take_break()
    alice.work()
    bob.work()
