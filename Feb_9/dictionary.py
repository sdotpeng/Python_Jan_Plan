
''' dictionary.py
Guide to dictionary
'''

''' Create a dictionary '''
dic = {} # lst = []
print(type(dic))
dic = dict() # lst = list()
print(type(dic))

''' Add a key-value pair '''
dic['love'] = '爱'
dic['yixin'] = '按摩师'
print(dic)

''' Access a value '''
print(dic['love'])
# print(dic['ricky'])

''' Update a key-value pair '''
dic['yixin'] = '厨师'
print(dic)

''' Initialize a dictionary '''
dic_two = {'ricky': '真正的按摩师', 'julian': '二次元'}
print(dic_two)

''' No order inside a dictionary '''
print(dic)
dic[0] = 'Abel Yan'
dic[1] = 'Lucas Chen'

''' Creating dictionaries with real data '''
students = ['Paul', 'Joel', 'Kim', 'Rose', 'Victoria']
grades = [99,93,88,80,95]
myDic = {'Paul': 99,
         'Joel': 93,
         'Kim': 88,
         'Rose': 80,
         'Victoria': 95}

print(myDic['Kim'])

''' Values in dictionaries can be any data '''
myDic = {'shapes': ['Square', 'Circle'],
         'gpa': 4.0,
         'name': 'bob'}

''' Keys of a dictionary has to be immutable '''
dic1 = {'mag': 0.1, 'width': 20}
dic2 = {'mag': 0.2, 'width': 18}

dic = {100: dic1, 200: dic2}
print(dic)
dic[100]['width']
lst = [1, dic, 2]
lst[1][100]['width']

''' Usually we use str and int as the key, not float '''
dic = {}
dic[1.1 + 2.2] = 6.6
# print(dic[3.3])

''' Methods for dictionary '''
dic = {'Yixin': 0, 'Rachel': 1}

dic = {'a':1}
# 'c' in dic

'''
`dic.get(key, default=None)`
'''
print(dic.get('Yixin'))
print(dic.get('Ricky', 2))

# What is the frequency of each character in the list?
lst = list('aaaaaabbbcbcbbbshdhdbsbshshshahshash')

dic = {}
for letter in lst:
    dic[letter] = dic.get(letter, 0) + 1
print(dic)

'''
`d.pop(key, default=None)`
'''

'''
`d.update(newd)`
'''

dic = {'one':10, 'two':20}
dic.update({'one':100, 'three': 30})
print(dic)

''' keys() method, values() method and items() method '''
# `d.keys()`
dic = {'One': 1, 'Two': 2, 'Three': 3}
print(list(dic.keys()))
# `d.values()`
print(list(dic.values()))
# `d.items()`
print(list(dic.items()))

for key, value in dic.items():
    print(key)
    print(value)