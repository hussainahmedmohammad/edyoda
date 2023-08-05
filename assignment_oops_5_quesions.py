# challenge 1: you need to implement a method that squares passing variables and returns their sum.

# Problem statement: Implement a class Point that has three properties and a method. All these attributes 
# (properties and methods) should be public.This problem can be broken down into two tasks:

# Task 1:  Implement a constructor to initialize the values of three properties: x, y, and z.

# Task 2:  Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.

# Sample properties 1, 3, 5
# Sample method output 35

class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def sqSum(self): 
        value = self.x**2 +self.y**2 +self.z**2   
        return value
        
ref_var = point(1,3,5)
print(ref_var.sqSum())

# ******************************************************************************************************##

# Challenge 2: Implement a Calculator Class In this exercise, you have to implement a calculator 
# that can perform addition, subtraction, multiplication, and division.

# Problem statement Write a Python class called Calculator by completing the tasks below:

# Task 1
# Implement an initializer to initialize the values of num1 and num2. 
# Properties
# num1
# num2

# Task 2
# Methods

# • add() is a method that returns the sum of num1 and num2.
# • subtract() is a method that returns the subtraction of num1 from num2.
# • multiply() is a method that returns the product of num1 and num2.
# • divide() is a method that returns the division of num2 by num1.


class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num2 / self.num1
    
obj = Calculator(10,94)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())

# ******************************************************************************************************##

# Challenge 3: Implement the complete Student class by completing the tasks below
# Implement the following properties as private:
# • name
# • rollNumber

# Include the following methods to get and set the private properties above:
# • getName()
# • setName()
# • getRollNumber()
# • setRollNumber()

# Implement this class according to the rules of encapsulation.

# Input - Checking all the properties and methods
# Output - Expecting perfectly defined fields and getter/setters

# If the setter is not defined properly, the corresponding
# getter will also generate an error even if the getter is defined properly.

# Note: Do not use initializers to initialize the properties.Use the set methods to do so.

class Student:   
    def setName(self,__name ):
        self.__name = __name  
          
    def getName(self):
        return self.__name 
      
    def setrollnumber(self,__rollnumber):
        self.__rollnumber = __rollnumber  
         
    def getrollnumber(self):
        return self.__rollnumber  
    
student1 = Student()
student2 = Student()

student1.setName('hussain ahmed')
student1.setrollnumber(29)

print(student1.getName())
print(student1.getrollnumber())

student2.setName('shiva sai')
student2.setrollnumber(20)

print(student2.getName())
print(student2.getrollnumber())

# ******************************************************************************************************##

# Challenge 4: Implement a Banking Account In this challenge, you will implement a banking account using 
# the concepts of inheritance.

# Implement the basic structure of a parent class Account and a child class SavingsAccount.

# Task 1: Implement properties as instance variables, and set them to None or 0.
# Account has the following properties:
# • title
# • Balance

# SavingsAccount has the following properties:
# • interestRate


# Task 2: Create an initializer for Account class. The order of parameters should be the following, where Ashish is 
# the title, and 5000 is the account balance:
# Account("Ashish", 5000)

# Task 3: Implement properties as instance variables, and set them to None or 0. Create an initializer for 
# the SavingsAccount class using the initializer of the Account class in the order below:
# Account("Ashish", 5000, 5)

# Here, Ashish is the title and 5000 is the balance and 5 is the interestRate.

class Account:
    
    def __init__(self,title = None, balance = 0):
         self.title = title
         self.balance = balance
        
                
class SavingsAccount(Account):
    
    def __init__(self,title,balance,interestRate):
        super().__init__(title,balance)
        
        # self.title = title
        # self.balance = balance
        self.interestRate = interestRate
        
    def SA_details(self):
        return (f'title is {self.title} & bal is {self.balance} & intrest is {self.interestRate}')
        
    
obj_SA = SavingsAccount('ashish',5000,5)
obj = SavingsAccount('hussain',2000,2)

print(obj_SA.SA_details())
print(obj.SA_details())

# ******************************************************************************************************##

# Challenge 5: Handling a Bank Account

# In this challenge, we will be extending the previous challenge and implementing methods in the parent class
# and its corresponding child class.The initializers for both classes have been defined for you.

# Task 1
# In the Account class, implement the getBalance() method that returns balance.

# Task 2
# In the Account class, implement the deposit(amount) method that adds amount to the balance.
# It does not return anything.

# Sample input:
#     balance = 2000
#     deposit(500)
#     getbalance()
# Sample output:
#     2500

# Task 3
# In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance.
# Sample input:
#   balance = 2000
#   withdrawal(500)
#   getbalance()
# Sample output:
    # 1500
    
#task 4
# In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance.
# Sample input:
# balance = 2000
# interestRate = 5
# interestAmount()
#sample output:
    # 100

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        return (f'amount withdrawal {self.amount} remaining balance {self.balance}')

    def deposit(self, amount):
        self.amount = amount 
        self.balance = self.balance + self.amount
        return (f'amount deposited {self.amount} now total balance is {self.balance}')
    
    def getBalance(self):
        return (f'reamining balance = {self.balance}')
    

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):       
        return (f'for {self.balance} intrest is {(self.interestRate * self.balance)/100}')

obj = SavingsAccount('ashish',5000,5)
print(obj.title)
print(obj.balance)
print(obj.withdrawal(500))
print(obj.deposit(10000))
print(obj.getBalance())
print(obj.interestAmount())
