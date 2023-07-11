# Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters.

# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

#objectives:
# 1> code must be implemented by using function
# 2> fun must be accept the string
# 3> count of upper case must be printed
# 4> count of lower case must be printed

# with function method 1:

# def count(string):
#     uc = 0
#     lc = 0
#     for i in string:
#         if i.isupper() == True:
#             uc += 1
#         elif i.islower() == True:
#             lc += 1
#     print ("No. of Upper case characters :",uc ) 
#     print ("No. of Lower case Characters :",lc) 
#     return
# string = input("entre a string : ")
# count(string)



#with function method-2
# string = input("entre a string : ")#'The quick Brow Fox'
# def words():
#      return string
# def count(string):
#     uc = 0
#     lc = 0
#     for i in words():
#         if i.isupper() == True:
#             uc += 1
#         elif i.islower() == True:
#             lc += 1
#     print ("No. of Upper case characters :",uc) #3
#     print ("No. of Lower case Characters :",lc)
#     return
# count(words())
    

#without function

# string = input("entre a string : ")
# uc = 0
# lc = 0
# total = 0
# for i in string:
#     if i.isupper() == True:
#         uc += 1
#     elif i.islower() == True:
#         lc += 1   
# print ("No. of Upper case characters :",uc) 
# print ("No. of Lower case Characters :",lc) 

