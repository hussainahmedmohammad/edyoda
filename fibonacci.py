#fibonacci problem 

# Write a Python program to get the Fibonacci series between 0 to 50

# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

a = 0
b = 1
while a <= 50:
    print (a, end = " ")
    c = a+b
    a=b
    b=c
    
    
    
# fibonacci program with user input

# num = int(input("entre a number : "))
# a = 0
# b = 1
# c = a + b
# print(a)
# print(b)
# print(c)
# while num != 0:
#     a,b = b,c
#     num = num - 1
#     print(b)
    
