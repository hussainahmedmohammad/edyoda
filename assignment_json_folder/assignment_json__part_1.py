#  1. Create a JSON file (employee.json) containing employee
#  information of minimum 5 employees. Each employee
#  information consists of Name, DOB, Height, City, State.
#  Write a python program that reads this information from
#  the JSON file and saves the information into a list of
#  objects of Employee class. Finally print the list
#  of the Employee objects.

import json

emp_info = {
    
    "employee 1":{'name': 'sai',
          'dob': '10/10/2010',
          'height': '5.5 feets',
          'city': 'hyderabad',
          'state': 'telangana'},
    
    "employee 2":{'name': 'ram',
          'dob': '11/11/2011',
          'height': '5.8 feets',
          'city': 'warangal',
          'state': 'telangana'},
    
    "employee 3":{'name': 'shyam',
          'dob': '12/12/2012',
          'height': '6.2 feets',
          'city': 'panaji',
          'state': 'goa'},
    
    "employee 4":{'name': 'veena',
          'dob': '09/09/2009',
          'height': '5.6 feets',
          'city': 'pune',
          'state': 'maharastra'},
    
    "employee 5":{'name': 'varun',
          'dob': '08/08/2008',
          'height': '5.11 feets',
          'city': 'chennai',
          'state': 'tamilnadu'}
}

with open('employee.json','w') as f:
    json.dump(emp_info,f,indent = 4)
    
