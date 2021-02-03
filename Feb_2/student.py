'''student.py
Our very first class on OOP! Represents a Student


TODO:
Make Student class with methods:
    - Construtor with 2 parameters: name and year
    - get methods
    - set year method
Main code:
    - Create two students
    - Get and print their names and years
    - Set one of their years
    - Print both years
'''

class Student:
    # Constructor
    def __init__(self, name, gradYear):
        '''This is the constructor
        self is always the first parameter for a class method. It is a
        ''bundle of instance variables'' for the current object
        '''
        # Create internal values for name and gradYear
        self.name = name # Tell Python we want to save info as an internal value
        self.year = gradYear # IVs don't need to have the same name as parameters

    def __len__(self):
        return 0

    def getName(self):
        return self.name
        # You CAN NOT DO THIS:
        # return name # name went away after constructor ended

    def getGradYear(self):
        return self.year

if __name__ == '__main__':
    Yixin = Student('Yixin', 2024)
    print(Yixin.getName())
    print(Yixin.getGradYear())
    print(len(Yixin))

# len([1,23])
# len('str')

# def len(object):
#     return object.__len__()