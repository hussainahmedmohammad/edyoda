# Write a Python program to square the elements 
# of a list using map() function.

# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]

# objectives:
# must have a list as input


#******************************************************************#

#with map function

# def square(x):
#     return x**2   # --> x*x also possible

# a = input('entre a number: ').split(',')
# b = []
# for i in a:
#     i = int(i)
#     b.append(i)
    
# new = list(map(square , b))
# print(new)

#*****************************************************************#
# def square(x):
#     return x**2

# a = input('entre a value: ').split(',')
# b = list(map(int,a))
# new = list(map(square , b))
# print(new)

#*****************************************************************#
def square(x):
    return x**2  
    
a = input('entre a values: ').split(' ') #use space
b = [int(i) for i in a ]
new = list(map(square , b))
print(new)