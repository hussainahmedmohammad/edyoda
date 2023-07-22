# Write a Python program to triple all numbers of a given list of integers.
# Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]


#********************************************************************#
# with map function


# def triple(x):
#    return x*3

# a = [1, 2, 3, 4, 5, 6, 7]
# new_list = list(map(triple,a))
# print(new_list)

#********************************************************************#

# def triple(x):
#    return x*3

# a = input('entre a number: ').split(' ')
# b = []
# for i in a:
#    i = int(i)
#    b.append(i)
# new = list(map(triple , b))
# print(new)
 

#********************************************************************#
# without map function

# list = [1, 2, 3, 4, 5, 6, 7]
# new_list = []
# for i in list:
#     new_list.append(triple(i))
    
# print(new_list,end = '')






