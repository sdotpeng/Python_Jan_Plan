# First step: have a random number
import random
number = random.randint(1, 100)

# While loop
# while <boolean_statement>:
#   <loop body>

i = 0
while i < 10:
    # print(i)
    i = i + 1

# In a while loop, we need to ensure the boolean statement will be False at one point

# Second step: take a guess from the user
guess = int(input('Enter the number you guess: '))
# print(type(guess))

# Third step: while loop
# while guess != number:
#     if guess > number:
#         print('You guessed a greater number...')
#     else:
#         print('You guessed a smaller number...')
#     guess = int(input('Enter the number you guess: '))

# There're two keywords in Python loops (for loop or while loop): break and continue
while True:
    if guess == -1:
        break
    if guess > number:
        print('You guessed a greater number...')
    else:
        print('You guessed a smaller number...')
    guess = int(input('Enter the number you guess (enter -1 to abort): '))

print('You are correct!')

