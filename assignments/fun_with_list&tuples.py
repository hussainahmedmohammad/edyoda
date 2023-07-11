# assignment- 2

# write a python progrtam to get a list, sorted increasing order by the last element in each 
# tuple from a given list of non empty list. 

# sample list : [(2,5),(1,2),(4,4),(2,3),(2,1)]
# expected output: [(2,1),(1,2),(2,3),(4,4),(2,5)]

# grading points : no
# Example list containing tuples

list = [(2,5),(1,2),(4,4),(2,3),(2,1)]

new_list = []
rev = []

for i in list:
     a = i[::-1]
     new_list.append(a)
     
b = sorted(new_list)
for i in b:
    c = i[::-1]
    rev.append(c)
print(rev)       # output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]



# logic implemented:

# ---> sorted () with a tuple will sort by first element so 
# ---> by using slicing  concept on each element of tuple inside a list gives reverse elements 
# ---> then sort it and again reverse thee tuple inside a list


