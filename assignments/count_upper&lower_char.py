# Write a Python function that accepts a string and calculate the number of 
# upper case letters and lower case letters.

# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


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
# print ("No. of Upper case characters :",uc) #3
# print ("No. of Lower case Characters :",lc) #12


# with function:

# def count(string):
#     uc = 0
#     lc = 0
#     for i in string:
#         if i.isupper() == True:
#             uc += 1
#         elif i.islower() == True:
#             lc += 1
#     return (uc,lc)

# string = 'The quick Brow Fox'#input("entre a string : ")
# print("No. of Upper case characters :",count(string))
# print("No. of Lower case Characters :",count(string))