# insert a value to a list in a certain index
my_list = [10, 20, 30, 40]
my_list.insert(1, 15)
print(my_list)

# extend my_list 
my_list2 = [50,60,70]
my_list.extend(my_list2)
print(my_list)

# remove last element from my list
my_list.pop()
print(my_list)

# sort my-list in ascending order
my_list.sort()
print(my_list)

# find and print index of the value 30
value = 30
index = my_list.index(value)
print("The index of", value, "is", index)