# You use break when you want to exit the loop
# You use continue when you want to exit an iteration


a = [1,2,1,3,4,5]
b = [3838383838,2819,4,3,2]

# Method 1
# lst = a + b
# out = []
# for num in range(min(lst), max(lst)+1):
#     if num in a and num in b:
#         out.append(num)

# print(out)

# Method 2: Remove duplicate before comparing
new_lst = []
for num in a:
    if num not in new_lst:
        new_lst.append(num)

print(new_lst)

out = []
for num in new_lst:
    if num in b:
        out.append(num)

print(out)

# Method 3: Remove duplicate after comparing

# Method 4: Use set() to remove duplicates
a = [1,2,2,1,3,4,5]
a = list(set(a))
print(a)