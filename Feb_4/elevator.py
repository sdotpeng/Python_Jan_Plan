'''
elevator.py
Practice making a class for an elevator that carries people and has a weight limit
'''

class Elevator:
    def __init__(self, max_weight=400):
        '''
        TODO: Create instance variables for:
            - max weight capacity
            - list of people names on elevator (initially empty list)
            - list of people weights on elevator (initially empty list)
        '''
        self.max_weight = max_weight
        self.names = []
        self.weights = []

    def getMaxWeight(self):
        '''
        TODO: Write this get method
        '''
        return self.max_weight

    def getRiderNames(self):
        '''
        TODO: Write this get method
        '''
        return self.names

    def getRiderWeights(self):
        '''
        TODO: Write this get method
        '''
        return self.weights

    def setMaxWeight(self, newMaxWeight):
        '''
        TODO: Write this set method setter
        '''
        self.max_weight = newMaxWeight

    def addRider(self, newName, newWeight):
        '''
        TODO: Write this method
        This method is called when someone gets on the elevator
        It should append the name and weight to the appropriate IV lists
        '''
        self.names.append(newName)
        self.weights.append(newWeight)

    def findTotalRiderWeight(self):
        '''
        TODO: Write this method
        This method should determine and return the total weight of all the people
        in the elevator
        '''
        total = 0
        for weight in self.weights:
            total = total + weight

        return total

    def isCapacityOK(self):
        '''
        TODO: Write this method
        This method should return True if the weight of all the people on the elevator
        is BELOW the max capacity, otherwise return False
        '''
        return self.findTotalRiderWeight() <= self.max_weight

if __name__ == '__main__':
    vator = Elevator()
    vator.addRider('Xianyang', 150)
    vator.addRider('Julian', 120)
    vator.addRider('Rachel', 80)

    print('Current weight of all riders:', vator.findTotalRiderWeight())
    print('The limit is:', vator.getMaxWeight())
    print('Do we have room for another rider on the elevator?', vator.isCapacityOK())

    vator.addRider('Harry Huang', 120)
    print('Current weight of all riders:', vator.findTotalRiderWeight())
    print('Do we have room for another rider on the elevator?', vator.isCapacityOK())