my_list = [1,2,3,4,5]

# Shallow Copy

# my_list2 = my_list

# print("my_list:", my_list)
# print("my_list2:", my_list2)

# my_list2[2] = 99
# print("Assigning 99...")
# print("my_list:", my_list)
# print("my_list2:", my_list2)

# # Deep copy
# my_list2 = my_list.copy()

# print("my_list:", my_list)
# print("my_list2:", my_list2)

# my_list[2] = 99
# print("Assigning 99...")
# print("my_list:", my_list)
# print("my_list2:", my_list2)

# Slicing can also make deep copy of list
my_list2 = my_list[:]

print("my_list:", my_list)
print("my_list2:", my_list2)

my_list[2] = 99
print("Assigning 99...")
print("my_list:", my_list)
print("my_list2:", my_list2)