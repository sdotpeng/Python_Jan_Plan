''' More String '''

text = '       His name is Xianyang Zhang     '
print('lower()::', text.lower())
print('upper()::', text.upper())
print('title()::', text.title())

# strip() can trim off the trailing spaces before and after the text
print('strip()::', text.strip())

# rstrip() does the same job but only after the text
print('rstrip()::', text.rstrip())

# lstrip() does the same job but only before the text
print('lstrip()::', text.lstrip())

# isalpha() can test if all the string chars are alphabet
print('isalpha()::', text.isalpha())
print('isalpha()::', 'NoSpace'.isalpha())

# isdigit() can test if all the string chars are digits
print('isdigit()::', text.isdigit())
print('isdigit()::', '1234567890.0'.isdigit())

# startswith() tests if the string starts with the given other string
print('startswith()::', 'I love you'.startswith('I'))

# endswith() does the opposite
print('endswith()::', 'I love you'.endswith('him'))

print('first haha', 'second haha')

print('first haha' + 'second haha')

# format() helps format a string with replaceable parts
text_two = 'I {} {}'.format('hate', 'you')

print(text_two)