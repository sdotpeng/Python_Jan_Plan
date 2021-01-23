def order(n1, n2, n3, n4):
    lst = [n1, n2, n3, n4]
    lst.sort()
    return lst
print(order(4,5,0,-3))

numbers = input("Enter four numbers with space between: ")
# "Everyone loves Ricky".split()
lst = numbers.split()
output = []
for number in lst:
    output.append(int(number))

print(output)

num = 138
num % 10 -> 8
num = num / 10 -> 13
num % 10 -> 3
num = num / 10 -> 1
num % 10 -> 1
num = num / 10 = 0