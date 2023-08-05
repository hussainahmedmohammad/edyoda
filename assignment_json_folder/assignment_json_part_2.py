# 1. Create a JSON file (employee.json) containing employee 
# information of minimum 5 employees. Each employee 
# information consists of Name, DOB, Height, City, State.
# Write a python program that reads this information from 
# the JSON file and saves the information into a list of 
# objects of Employee class. Finally print the list of the 
# Employee objects.

# created employee.json file with assignment_json_1.py 

import json

class Employee:
   
    def convert(self):
     
        with open('employee.json','r') as f:
            self.jfile = json.load(f)
            x= [self.jfile]
            print(type(x))
            return x
             
demo = Employee()
print(demo.convert())
            