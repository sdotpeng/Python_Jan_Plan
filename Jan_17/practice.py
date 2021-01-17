# 有一个整数，加上100或者加上268都是一个完全平方数，请问该数是多少？
# 完全平方数：4 9 16 25 36 49

import math
def isSquare(number):
    '''
    Check if the given number is a perfect square
    '''
    for temp in range(1, int(math.sqrt(number)) + 1):
        if temp * temp == number:
            return True
    return False

for n in range(1, 10000):
    if isSquare(n + 100) and isSquare(n + 268):
        print('n =', n, "->", 'n + 100 =', n+100, 'n + 268 =', n+268)

# 求出1! + 2! + 3! + 4! + 5! + ... + 20!的和

def factorial(number):
    product = 1
    for num in range(1, number + 1):
        product = product * num
    return product

# def factorial(number):
#     if number == 1:
#         return 1
#     return number * factorial(number - 1)

sum = 0
for number in range(1, 21):
    sum = sum + factorial(number)

print(sum)