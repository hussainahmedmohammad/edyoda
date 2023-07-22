# Write a Python program to create a lambda function that adds 25 to a 
# given number passed in as an argument.

# objectives:
# use lambda function 
# should print the output


# a = float(input('entre a number : '))
x = lambda a :  a+25
print(x(float(input('entre a number : ')))) #float value


x = lambda a :  a+25
print(x(int(input('entre a number : ')))) #int value-

x = lambda a :  a+25
print(x(int(10)))
