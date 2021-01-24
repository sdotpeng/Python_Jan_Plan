import sys

print("Command Line Arguments:", sys.argv)

# sys.argv is a list containing all command line arguments
# Command Line is the Terminal

print("Length of the list:", len(sys.argv))

num1 = int(sys.argv[1])
num2 = int(sys.argv[3])

operation = sys.argv[2]

if operation == "+":
    print(num1, " + ", num2, " = ", num1 + num2)
elif operation == '-':
    print(num1, " - ", num2, " = ", num1 - num2)
elif operation == 'times':
    print(num1, " * ", num2, " = ", num1 * num2)
else:
    print(num1, " / ", num2, " = ", num1 / num2)