'''csstudent.py
Show inheritance with the CSStudent (child class) that inherits from ColbyStudent (parent class)

TODO:
    1. is-a relationship
    2. CSStudent constructor signature: def __init__(self, name, year, favLang)
        - Show with redundant code.
        - Code reuse: call parent constructore (with super() and directly)
    3. When instance variables in parent calling parent constructor
        - Show __init__ with/without calling parent constructor
    4. set/get methods for CSStudent-specific vars
    5. Write printGrades in parent (100 point scale)
        - Show OVERRIDE in child (30 point scale)
        - Show EXTENDING in (both scale)
    6. Symbol table for `newCSStudent.printGrades()` and `newColbyStudent.printGrades()`
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

    def printGrades(self):
        return sum(self.grades) / len(self.grades)

    def getLastDay(self):
        # return ColbyStudent.lastDayOfClass
        return self.lastDayOfClass

class CSStudent(ColbyStudent):

    def __init__(self, name, grad_year, favLang):
        # Leveraging/running code in parent class
        # Parent class has another name: super class
        # Child is called subclass
        super().__init__(name, grad_year=grad_year)
        self.favLang = favLang
        # If super clas __init__() was not called, self.gpa would never be defined
        # So the following code of accessing gpa value will crash

    def getFavLang(self):
        return self.favLang

    def printGrades(self):
        ''' CS class grades should be out of 100 '''
        # Method 1
        # grades = self.getGrades() # subclass
        # grades = super().getGrades()
        # return sum(grades) / len(grades) * 100 / 4

        # Method 2
        return super().printGrades() * 100 / 4

    # An override. Now child and parent versions are not linked/duplicated
    def getLastDay(self):
        return 'June 1'

    # An extend.
    def getLastDay(self):
        print(super().getLastDay())
        return 'June 1'

'''
Override: REPLACES behavior of parent with child version
Extending: Do specific stuff in child version of method, but also call parent version
'''

if __name__ == '__main__':
    colbyStu = ColbyStudent('Yixin', 2024)
    csStu = CSStudent('Ricky', 2024, 'Python')

    csStu.addGrade(4)
    csStu.addGrade(4)
    csStu.addGrade(4)
    csStu.addGrade(4)

    print('CS Student fav language:', csStu.getFavLang())
    print('CS Student name:', csStu.getName())

    print('CS Student Grades:', csStu.printGrades())