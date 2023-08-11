#complete food ordering app

#menu driven  program

from admin import *
from user import *
import sys

dummy_admin = admin()
dummy_user = user()
while True:
    print('welocme for food ordering application ')
    print('select 1 for admin')
    print('select 2 for user')
    print('select 3 for exit')
    option = int(input('entre the option :'))

        
    
    if option == 1:
        print('press 1 for ordering food items ')
        print('press 2 for edit food items ')
        print('press 3 for remove food ')
        print('press 4 for view food items ')
        option = int(input('press any number between 1-4 : '))
        
        if option == 1:
            dummy_admin.food_items()
        elif option ==2 :
            dummy_admin.edit_food_items()
        elif option == 3 :
            dummy_admin.remove_id()
        elif option == 4 :
            dummy_admin.view_food_items()
        else:
            print ('entre valid number')
    
    
    elif option == 2:
           
                  
        
        print('press 1 for register ')
        print('press 2 for login ')
        print('press 3 for options ')
        print('press 4 for place_order ')
        print('press 5 for history ')
        print('press 6 for update profile ')
        option = int(input('entre a number between 1- 6 : '))
        
        if option == 1:
            print(dummy_user.Register())
        elif option == 2:
            print(dummy_user.login())
        elif option == 3:
            print(dummy_user.options())
        elif option == 4:
            print(dummy_user.place_order())
        elif option == 5:
            print(dummy_user.history())
        elif option == 6:
            print(dummy_user.update_profile())
        else :
            print('please entre valid number')
        
    elif option == 3:
        print('********* thank you for visiting this application **********')
        sys.exit()
    else:
        print('entre valid credentials')
        
            




                