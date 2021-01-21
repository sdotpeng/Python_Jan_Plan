import random

# choice() function retuns a random choice from the list you pass in
print(random.choice([1,2,3,4]))

# Random Password Generator
# 1. Has to be 10 digits long
# 2. Has to have characters and numbers
# 3. Lower case character range: a-f
# 4. Do not contain 5 and b
import string
total = ''
for time in range(10):
    char = random.choice(string.ascii_letters + string.digits)
    total = total + char
print(total)