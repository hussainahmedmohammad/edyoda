# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform
# the following operations:

#  a. It should have a function ‘description()’ which prints the name and age of the dog.
 
#  b. It should have a function ‘get_info()’ which prints the coat color of the dog.
 
#  c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’  which is inherited from the class ‘Dog’. 
#  It should have at least two methods of its own.
 
#  d. Create objects and implement the above functionalities.

class Dog:
    
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    def description(self):
        return  (f"parent dog name is {self.name} and parent age is {self.age} years")
        
    def get_info(self):
        return (f'coat color is {self.coat_color}')
    
    
class JackRussellTerrier(Dog):
#     def __init__(self,name,age,coat_color):
#         super().__init__(name,age,coat_color)
        
    def dog_details(self):
        return (f'child 1 name is {self.name} age is {self.age} years and coat color is {self.coat_color}')
    
    def eating(self):
        return 'silent and sleep'
    
    def barking(self):
        return 'hungry'
        
    
class Bulldog(Dog):
#     def __init__(self,name,age,coat_color):
#         super().__init__(name,age,coat_color)
        
    def dog_details(self):
        return (f'child 2 name is {self.name} age is {self.age} years and coat color is {self.coat_color}')
        
    def run(self):
        return 'running'
    
    def bite(self):
        return 'biting'

parent_dog1 = Dog('tommy', 5 , 'white')
print(parent_dog1.description())
print(parent_dog1.get_info())
print('*'*60)

child_dog1 = JackRussellTerrier('germanshefard',2,'brown')
print(child_dog1.dog_details())
print(child_dog1.barking())
print(child_dog1.eating())
print('*'*60)

child_dog2 = Bulldog('blackdog', 3 , 'black')
print(child_dog2.dog_details())
print(child_dog2.bite())
print(child_dog2.run())
 
