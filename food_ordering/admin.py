# Add new food items. Food Item will have the following details:
# 1 .FoodID //It should be generated automatically 
# by the application.
#     Name
#     Quantity. For eg, 100ml, 250gm, 4pieces etc
#     Price
#     Discount
#     Stock. Amount left in stock in the restaurant.

# 2. Edit food items using FoodID.
# 3. View the list of all food items.
# 4. Remove a food item from the menu using FoodID.



import json

class admin:
    
    def __init__(self):
        self.food_id = 1000   
        self.list_of_items = {}

       
    def food_items(self):
        self.food_id +=1 
        self.food_name = input('entre food name : ')
        self.food_quantity = input('entre food quantity : ')
        self.food_price = float(input('entre price of food item : '))
        self.food_discount = float(input('entre discount : '))
        self.food_stock = float(input('entre food stock : '))
        
        self.items = {'food_id':self.food_id,
                      'food_name':self.food_name,
                      'food_quantity': self.food_quantity,
                      'food_price':self.food_price,
                      'food_discount': self.food_discount,
                      'food_stock':self.food_stock
                      }
        self.list_of_items[self.food_id] = self.items
        
        with open('admin_food_items.json','w') as f:
            json.dump(self.list_of_items,f,indent= 4)
            return self.list_of_items
  
        
    def edit_food_items(self):
    
        id = int(input('entre food id to edit items in that : '))       
        item = input('entre the item to update : ')
        update_value = input('entre the updated value ')
        self.list_of_items[id][item] = update_value 
        
        with open('admin_food_items.json','w') as f:
            json.dump(self.list_of_items,f,indent= 4)
            return self.list_of_items     
         
              
    def view_food_items(self):
        
            with open('admin_food_items.json','r') as f:
                view = json.load(f)
                return view
                
            
    def remove_id(self):
               
        id = int(input("entre a id to remove : "))
        del self.list_of_items[id]
        
        with open('admin_food_items.json','w') as f:
            json.dump(self.list_of_items,f,indent= 4)
            return self.list_of_items
    
        
            
# x = admin()
# print(x.food_items())
# print('*'*100)
# print(x.food_items())
# print('*'*100)
# print(x.food_items())
# print('*'*100)



# print(f'to edit food items :{x.edit_food_items()}')
# print('*'*100)
# print(f'list of items after removing : {x.remove_id()}')
# print('*'*100)
# print(f'to view all food items : {x.view_food_items()}')
