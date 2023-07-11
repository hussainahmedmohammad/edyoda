# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"


# without function:
    
# string = "1234abcd"
# rev = ''
# index = len(string)-1
# while index >= 0:
#     rev += string[index]
#     index -= 1
# print(rev)        #output: dcba4321


# with function:

# def reverse(string):
#     index = len(string)-1
#     rev = ''
#     while index >= 0:
#         rev += string[index]
#         index -= 1
#     return rev

# string = '1234abcd'
# print(reverse(string))   #output: dcba4321




# def reverse(a):
#     return(a[::-1])

# a = '1234abcd'
# print(reverse(a))   #output: dcba4321