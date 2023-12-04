class Cat():
  def __init__(self, name, age=0):
    self.name = name
    self.age = age

  def meow(self):
    print(f"{self.name} says meow!")

  def __str__(self):
    return f"{self.name} is {self.age} years old!"

bug = Cat("Bug", 2)
print(bug)
bug.meow()


class Vehicle():
  def __init__(self, make, model, running=False):
    self.make = make
    self.model = model
    self.running = running
  
  def start(self):
    self.running = True
    print("Running...")

  def stop(self):
    self.running = False
    print("Stopped...")

  def __str__(self):
    return f"Vehicle is a {self.make} {self.model}."

car = Vehicle("Toyota", "Solara")
print(car)
print(car.running)
car.start()
print(car.running)
car.stop()
print(car.running)
