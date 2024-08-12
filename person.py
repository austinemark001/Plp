class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
    def introduce (self):
      print("hello", self.name, ", of age",self.age,"years and gender" self.gender)

Person("Austine",20,"male").introduce()


