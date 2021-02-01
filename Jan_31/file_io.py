'''file_io.py
File input/output workflow
'''

# Read in text from a text file (.txt)
# 3 primary ways to do this

# 1) Read whole file in at once as a single string
# file = open('Jan_31/loveletter.txt', 'r')
# theText = file.read()
# file.close()
# print(theText)

# 2) Read individual lines until we hit the end of the file
# (indicated by empty string)
file = open('Jan_31/loveletter.txt', 'r')
texts = file.readlines()
file.close()
print(texts)

# # 3) Looping through a file
# file = open('Jan_31/loveletter.txt', 'r')
# for line in file:
#     print(file.readline())

# File input
file = open('Jan_31/loveletter.txt', 'w')
file.write('I love you very very much\nMe too!?')
file.close()

file = open('Jan_31/loveletter.txt', 'r')
print(file.read())
file.close()