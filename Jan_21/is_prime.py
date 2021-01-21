def is_prime(number):
    '''
    Checks if the given number is prime

    number -> int, given number to be checked
    return -> True of False
    '''

    if number < 2:
        print("Invalid input")
        return

    # A prime number can be only divided by 1 and itself
    # Meaning that there's no other number between 2 and itself-1 that can divide it
    # 19 -> 1,19
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

for number in range(2, 100):
    if is_prime(number):
        print(number)