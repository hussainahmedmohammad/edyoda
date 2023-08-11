# The user will have the following functionalities: 
# 1. Register on the application. Following to be entered
# for registration:
#          Full Name
#          Phone Number
#          Email
#          Address
#          Password

# 2. Log in to the application

# 3. The user will see 3 options:
#          Place New Order
#          Order History
#          Update Profile

# 4. Place New Order: The user can place a new order at 
# the restaurant.
#     Show list of food. The list item should as follows:
#     Tandoori Chicken (4 pieces) [INR 240]
#      Vegan Burger (1 Piece) [INR 320]
#      Truffle Cake (500gm) [INR 900]

# 5. Users should be able to select food by entering an array
# of numbers. For example, if the user wants to order Vegan
# Burger and Truffle Cake they should enter [2, 3]

# 6. Once the items are selected user should see the list
# of all the items selected. The user will also get an option
# to place an order.

# 7.Order History should show a list of all the previous orders

# 8.Update Profile: the user should be able to update their
# profile.

import json

class user:
    def __init__(self):
        self.user_details = {}
        self.items = {}
    
    def Register(self):
        self.fullname = input('entre fullname : ')
        self.phone_number = int(input('entre phone number : '))
        self.email = input('entre email_id : ')
        self.address = input('entre your address : ')
        self.pasword = input('entre your password : ')
        
        self.details = {'name': self.fullname,
                        'phone':self.phone_number,
                        'email':self.email,
                        'address':self.address,
                        'password':self.pasword}
        self.user_details[self.email] = self.details
        
        with open('user_info.json','w') as p:
            json.dump(self.user_details,p,indent = 4)
            return self.user_details
        
    def login(self):  
        with open('user_info.json','r') as f:
            c = json.load(f)
            print([c])
        print('****** to verify entre credentials :  ******')
        
    
        while True:
            email = input('entre the email : ')
            password = input('entre the password : ')
            if email in c:
                if password == c[email]['password']:
                    return 'logging in'
                else:
                    return 'entre valid email and pasword'
            else:
                return 'entre valid email and pasword'
       
        
    def options(self):
        
        self.place_new_order = "place new order"
        self.order_history = 'order history'
        self.update_profile = 'update_profile'
        return [self.place_new_order,self.order_history, self.update_profile]
    
    def place_order(self):
        count = 0
        self.order_history = {}
        self.ordered_items = []
        list_items = [{1:'Tandori chiken - 4p : 240/- only'} ,
                      {2: 'vegan burger - 1p : 320/- only'},
                      {3:'truffle cake - 500gm : 900/- only'}]
        
        
        print('********* your food items in list is *********')
        print(list_items)
            
        order = int(input('entre the number to order food : '))
        if order == 1:
            self.ordered_items.append(list_items[0])
            print('your order is : ')
            count +=1
            self.order_history[count] = list_items[0]
            return self.ordered_items
        elif order == 2:
            self.ordered_items.append(list_items[1])
            print('your order is : ')
            count +=1
            self.order_history[count] = list_items[1]
            return self.ordered_items
        elif order == 3:
            self.ordered_items.append(list_items[2])
            print('your order is : ')
            count +=1
            self.order_history[count] = list_items[2]
            return self.ordered_items
                
        else:
            return (f'please select items from th list : {list_items}')
            
     
        
        
    def history(self):
        print("******* your ordered history is *******")
        try:
            with open ('order_history.json','w') as f:
                json.dump(self.order_history,f,indent = 4)
            return self.order_history
        except:
            return 'history is empty'
        
        
    def update_profile(self):
        with open ('user_info.json','r') as f:
            c = json.load(f)
            print(c)
        mail_id = input('entre a mail id to edit details : ')
        field = input('entre the field to update : ')
        update = input('entre value to update : ')
        self.user_details[mail_id][field] = update
        
        with open ('user_info.json','w') as f:
            json.dump(self.user_details,f,indent = 4)
            return self.user_details        
    
    
   
        
# user1 = user()
# print(user1.Register())
# print(user1.Register())

# print('*'*100)  
# print(user1.login())
# print('*'*100)
# print(user1.options())
# print('*'*100)

# print(user1.place_order())
# print(user1.update_profile())
# print(user1.history())

        
        