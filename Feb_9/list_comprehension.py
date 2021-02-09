''' list_comprehension.py
A introduction guide to list comprehension
'''

lst = list(map(lambda x,y: x+y, [1,3,5,7], [2,4,6,8]))
print(lst)

lst = list(filter(lambda x: x // 10 % 10 == 3, [100, 31, 231]))

lst = []
for i in range(10):
    lst.append(i**2)

lst = [i ** 2 for i in range(10)]

values = [14,15,29,28]

lst = [i ** 2 for i in values]

lst = [i ** 2 for i in range(10) if i % 2 == 0]

file = open('Feb_9/boredom.txt', 'r')
for line in file:
    line = line.strip().replace('DELETE_ME', '').title()
    print(line)
file.close()

print(list(map(lambda x: x.replace(x[0], x[0].upper()), [line.strip().replace('DELETE_ME', '').lower() for line in open('Feb_9/boredom.txt', 'r')])))

print(' '.join([word for word in 'Yixin  is   bored'.split(' ') if word != '']))