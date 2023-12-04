class Cat():
  #class attribute
  next_id = 1

  def __init__(self, name, age=0):
    self.name = name
    self.age = age
    self.id = Cat.next_id
    Cat.next_id += 1

  def meow(self):
    print(f"{self.name} says meow!")

  def __str__(self):
    return f"Cat {self.id} named {self.name} is {self.age} years old!"

  # decorator
  @classmethod
  def get_total_cats(cls):
    return cls.next_id - 1


# class inheritance
class dumbCat(Cat):
  # add additional parameters AFTER the ones in the superclass
  def __init__(self, name, age=0, iq=0):
    # always call the superclass' __init__ first
    Cat.__init__(self, name, age)
    # now add any new attributes
    self.iq = iq
  # new methods
  def lower_iq(self, amount):
    self.iq -= amount
    print(f"{self.name}'s iq is now {self.iq}.")

bug = dumbCat("Bug", 2, 4)
pooka = Cat("Pooka", 8)
print(bug)
bug.meow()
print(pooka)
pooka.meow()
print(Cat.get_total_cats())
bug.lower_iq(35)
print(bug.iq)

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
