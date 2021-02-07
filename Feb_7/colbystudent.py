'''colbystudent.py
Design class ColbyStudent


TODO:
1. Add last day of class global variables (Dec 4)
    - Access with vs. without get method
    - Change date to Nov 24 and demonstrate change acrross all ColbyStudent objects
    - Show symbol table
2. Shallow copy access for getGrades in main code
    - Show symbol table
    - Fix issue in getGrades
'''

class ColbyStudent:

    lastDayOfClass = 'May 26'

    def __init__(self, name, grad_year=2024):
        ''' Constructor to initialize data '''
        self.name = name
        self.year = grad_year
        self.grades = []
        self.gpa = 0.0

    def getName(self):
        ''' Get method to return name '''
        return self.name

    def getGrades(self):
        # return self.grades.copy()
        return self.grades[:]

    def addGrade(self, newGrade):
        self.grades.append(newGrade)

    def getLastDay(self):
        # return ColbyStudent.lastDayOfClass
        return self.lastDayOfClass

# Class global variable

mike = ColbyStudent('Mike', grad_year=2022)
lily = ColbyStudent('Lily', grad_year=2023)
print('Mike last day of class:', mike.getLastDay())
print('Lily last day of class:', lily.getLastDay())
print('Class end day:', ColbyStudent.lastDayOfClass)

ColbyStudent.lastDayOfClass = 'Feb 10'

print('Mike last day:', mike.getLastDay())
print('Lily last day:', lily.getLastDay())

# Copy issues
# Make a student, add grades to show memory access problems
mike = ColbyStudent('Mike', grad_year=2022)
mike.addGrade(4)
mike.addGrade(3)
mike.addGrade(1)

mikesGrades = mike.getGrades()
print('Mike\'s grades outside the object', mikesGrades)

# Modify grades then print grades and the grades from the student accessed again
mikesGrades.pop()
print('Mike\'s grades outside the object (after pop)', mikesGrades)
print('Mike\'s grades object instance variable', mike.getGrades())