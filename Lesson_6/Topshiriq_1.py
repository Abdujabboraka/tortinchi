class Person:
    def get_info(self):
        return f"Student:\n    ismi: {self.name}\n    surname: {self.surname}\n    phone: {self.phone}\n    faculty: {self.fakultet}\n    rating: {self.rating}"


class Student(Person):
    def __init__(self,  name,surname,phone, fakultet, rating):
      self.name= name
      self.surname = surname
      self.phone =phone
      self.fakultet = fakultet
      self.rating = rating

Po =Student(name="Po",surname="Panda",phone=6663629,fakultet="kung-fu",rating=100)
print(Po.get_info())