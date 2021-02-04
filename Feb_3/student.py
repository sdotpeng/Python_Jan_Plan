'''Student.py
Our very first class but enhanced

TODO:
Make student class with methods:
    - Constructor with 2 parameters: name and year
    - get methods
    - set year method
Main code:
    - Craete two students
    - Get and print their names and years
    - Set one of their years
    - Print both years
'''

''' Function and Methods? '''
# def name(self, ):

class Student:
    def __init__(self, name, year):
        # There is a variable called name in the current object `self`
        self.name = name
        self.year = year
        # Not all the instance variables need to be parameters.
        # NOTE but all IVs should be defined in constructor
        self.gpa = 4.0
        self.grades = []

    # The following four methods are get methods (getter)
    def getName(self):
        return self.name

    def getGradYear(self):
        return self.year

    def getGPA(self):
        return self.gpa

    def getGrades(self):
        return self.grades

    def setYear(self, year):
        self.year = year

    def addGrade(self, newGrade):
        self.grades.append(newGrade)

    def addBonusPoints(self, grades):
        for i in range(len(grades)):
            self.grades[i] = self.grades[i] + 5

    def __str__(self):
        return "{}, Colby year of {}, has a gpa of {}, and his grades are {}".format(
            self.name, self.year, self.gpa, self.grades
        )

# len() can be used on a lot of objects, because essentially it calls the __len__() method
if __name__ == '__main__':
    xy = Student('Xianyang', 2024)
    print(xy.getGradYear())

    wjl = Student('Julian', 2024)
    print(wjl.getName())

    students = [xy, wjl]

    for student in students:
        print(student.getName())

    xy.addGrade(60)
    xy.addGrade(70)
    xy.addGrade(50)

    print('{}\'s grades are {}'.format(xy.getName(), xy.getGrades()))

    print("--------------")

    print(xy)

# len(object) -> it calls object.__len__()
# print(object) -> it calls object.__str__()