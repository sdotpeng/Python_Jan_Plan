''' recursion.py
'''

# Ever wonder what would happen if you called a function from inside a function?
def func(x):
    func(x)

# Called recursion. Yes! It is a valid thing we can do!

# Powerful design technique to produce elegant solutions to challenging problems that might
# otherwise require lots of code

# When to use recursion? Solution to a complex problem can be expressed in terms of solutions
# to slightly simpler versions of the original problem.

''' Example: factorial '''
def factorial_nr(number):
    # Non recursive method
    total = 1
    for i in range(1, number+1):
        total *= i
    return total

def factorial(number):
    # Recursive method
    if number == 1:
        return 1
    return number * factorial(number - 1)


print(factorial_nr(10000))

factorial(4)

''' Example: sum of list '''
def sum_list_nr(lst):
    # Non recursive method
    total = 0
    for number in lst:
        total += number
    return total

lst = [1,2,3,4]
print(sum_list_nr(lst))

def sum_list(lst):
    if len(lst) == 1:
        return  lst[0]
    return lst[0] + sum_list(lst[1:])

print(sum_list(lst))