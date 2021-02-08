''' lambda.py
Lambda function in Python
'''

# Lambda function 匿名函数
def square(number):
    return number ** 2
print(square(2))

# Few differences
#   1. No name
#   2. Argument name is simplied
lambdaSquare = lambda x : x ** 2
print(lambdaSquare(3))

lambda x, y : x + y
lambdaTwenty = lambda: 20
print(lambdaTwenty())

lambdaSum = lambda *args : sum(args)
print(lambdaSum(1,2,3,4,5,6,7,8))

lst = ['Yixin', 'Scottie', 'Rachel', 'Lily']

lst.sort(key=lambda x : len(x), reverse=True)

print(lst)