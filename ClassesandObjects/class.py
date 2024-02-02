class MyClass:
    
    x = 5
    

p1 = MyClass()
# print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
name = input('Enter you name: ')
age = int(input('Enter you age: '))  
p2 = Person(name, age)
print(p2.name, p2.age)

class d:
    pass