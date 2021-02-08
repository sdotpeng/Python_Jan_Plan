''' map.py
Map function in Python
'''

lst = [1,2,3,4,5,6,7,8,9,10]

new_lst = []
for number in lst:
    new_lst.append(number ** 2)
print(new_lst)

print(list(map(lambda x : x ** 2, lst)))

temperatures = [36.5, 37, 37.5, 38, 39]
print(list(map(lambda x : 9.0*x/5 + 32, temperatures)))

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-2,-4,-9]

print(list(map(lambda x, y, z : x+y+z, a, b, c)))