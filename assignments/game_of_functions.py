#Assignment-3

# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# Explanation:
# Summation should like 8+2+3+0+7 = 20

def total(list):
    count = 0
    for i in list:
        count += i
    return count

list = (8,2,3,0,7)
print(total(list))

# without function:

# list = (8,2,3,0,7)
# count = 0
# for i in list:
#     count += i
# print(count)