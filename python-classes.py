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