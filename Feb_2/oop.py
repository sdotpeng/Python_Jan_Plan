''' OOP.py
Object Oriented Programming
'''

''' 
Procedure Oriented Programming
'''

# weight_lst = [1.0, 0.8, 0.6]
# poo_lst = ['chile', 'wenchuan', 'ca']
# color_lst = ['very red', 'red', 'not so red']

# poo_lst[0]
# color_lst[0]

'''
A class allows us to create our own object types
'''
# e.g. not just what Zelle or tutrle have to offer - OOP opens up tons of possibilities
# Let's say we want to make a type of Object for an Apple
# Having apple class allows us to make objects of that type:
# apple1 = Apple('Chile')
# apple2 = Apple('CA')

# What is a good thing to create objects of?
# They are nouns: things - e.g. an apple is a thing, a turtle is a thing
# And why make a class for a thing?
# 1) Groups data/information related to unique instances of that thing

# 2 Classes allow us to perform actions on each instance, with its own methods
# For the student class, we can add a method called compareGPA(). So every student object
# or instance will be able to call this method

''' Common types of methods: '''
# * Access data from eaech instance of a class (object) - get method (getter)
# getGPA(), getName(), getAge()
# for example, jane.getGPA()

# * Change data from an instance - set method (setter)
# setAge(), setGPA(), setName()
# for example, bob.setGPA(4.0)

# Let's write a simple class for a student and play around with it