'''Important string methods'''
# Strings are technically objects and have methods. There are many:
# https://docs.python.org/3/library/stdtypes.html#string=methods
# Here are important ones that you should know (minimally)
# upper, lower, title, split(char), join, find(word), replace, count, isalpha
# isdigit, isupper, isalum

# Example: Let's see some string methods in action
file = open('Feb_1/dreamjob.txt', 'r')
text = file.read()
file.close()

print(text)
# print(text.upper())
# print(text.lower())
# print(text.title())

# NOTE: split() gives us a LIST
# We use split() to extract words/sentences
sentencesList = text.split('\n')
print(sentencesList[0])
print(sentencesList[1])

wordsList = text.split(' ')
print(wordsList)

# NOTE: join() Opposite of split. Takes in a list and converts it to a string, separated
# by the string it is called on.
# Text: 'two wrongs don\'t make a right'
asString = 'two wrongs don\'t make a right'
asList = asString.split(' ')
print(asList)
backAsString = ' '.join(asList)
print(backAsString)

print(' never '.join(asList))
print(' ----- '.join(asList))
print(' !!!!! '.join(asList))
print('\n'.join(asList))
print('\t'.join(asList))

# Join can be useful if you decide to read from a file line-by-line and store
# each line as an entry in a list. It can convert the list of line strings to one big string
# like we've had above"
file = open('Feb_1/dreamjob.txt', 'r')
dreamjobList = []
for line in file:
    dreamjobList.append(line)
file.close()
dreamjobAsString = ' '.join(dreamjobList)

print(dreamjobAsString)

# NOTE Find: find the input argument in the string, and print it out. If the search string
# is not found, find() returns -1
string = 'I love you'
print('Index of word love:', string.find('love'))
print('Index of word like:', string.find('like'))

# NOTE Replace: replace the word `a` with `b`.
string = 'I love you'
string = string.replace('love', 'like') # in-place operation
print(string)

# NOTE Count: Find total number of the input argument in the string
string = '''Ricky has been teaching Python for six months, and he has
been mentally stable for one month'''
print(string.count('has'))
print(string.count('has been'))
print(string.count('ricky'))

'''Write data to a file'''
# file = open('fileName.txt', 'w')
# file.write()
# file.close()

with open('Feb_1/dreamjob.txt', 'r') as file:
    text = file.read()

print(text)