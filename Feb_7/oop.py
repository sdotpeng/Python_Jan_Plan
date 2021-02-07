''' Review: Inheritance '''

''' 1. Is-a relationship '''
# Inheritance works well when the thing that one class models
# is a thing that a second class models
#   Example: A CS Student (child) is a Colby Student (parent)
#   Example: A gas car (child) is a vehicle (parent)
#   Example: Earth (child) is a planet (parent)
# The more specific thing is usually the child, the more general
# thing is usally the parent

''' Inheritance terminology '''
# Parent class      Child class
# Base class        Derived Class
# Superclass        Subclass
# Paris of terms tend to go together, but mean the same thing

''' What is inherited by the child class? '''
# Child class and objects you make out of it get a copy of all the methods in the parent.
#   Method actually stored in the parent class, but the child class and its object have a
#       connection ('arrow') to it
#   Methods defined in chlid class, but not in parent class, only useable in child class (not parent)
#   Example: Fruit() - Durian() - stinks()

''' Override a method '''
# The child class can override any of the methods of the parent (create a method with the same
# name as method in parent, but have it do different things)
#   The overridden method gets called when called on a child object
#   The parent method gets called when called on the parent object
#   Example: define in both parent and child
#       printGrades(self) called on ColbyStudent prints grades out of 4
#       printGrades(self) called on CSStudent prints grades out of 100

''' Extending vs. Overriding '''
# If method exists in both child and parent, child can call the parent's version (e.g. to do
# redundant operations, like we tend to do with the constructor)
# class CSStudent(ColbyStudent):
#   def __init__(self, name, year, favLang):
#       ColbyStudent.__init__(self, name, year)
#       # super().__init__(self, name, year)
#       self.favLang = favLang
#   - Can also call the parent method from the child method (like above)
#   - Think of code in parent method copy-pasted where it is called from the child method
#   - Calling parent method and doing additional work / assigning instance variables unique to child
#   is called extending the method

''' Instance variables (IVs) are NOT automatically inherited '''
# To have the same set of instance variables as parent, we need to call the parent's
# constructor in child constructor
#   Pass along shared/overlapping paremeters to parent constructor

''' Benefits of Inheritance '''
# - Promotes code reuse. Methods defined in parent (ColbyStudent) already implemented for child
# class (CSStudent) by the parent ColbyStudent (e.g. getName())
# - Saves time programming / fewer lines of code
# - Makes your code less error prone / easier to debug
#       - The more times your write essentially the same method, the more bugs you could
#        introduce
#       - If you fix a bug in one version of the method, you don't want to have to update all
#       the other variants. You'll like likely forget some - hence bugs
# - Promotes encapsualtion best practices
#       - Only the designer of the parent and child class needs to know how each is implemented
#       users that create objects of the parent and child types do not need to now that they 
#       inheritance
#       - They both can be used just like regular classes