#person

#dni: int
#name: str
#lastname: int
#role:int
#-----------------------

class Person:
    def __init__(self,dni: int, name: str, lastname: str, role: int):
        self.dni = dni
        self.name = name 
        self.lastname = lastname
        self.role = role


    def __repr__(self):
        return f"name={self.name}"



person3 = Person(dni=4546, name="sara", lastname="lopez", role=5)
person2 = Person(dni=2002, name="carla", lastname="jurado", role=4)
person1 = Person(dni=123, name="luisito", lastname="velez",role=1)

print(person1)
print(person2)
print(person3)
