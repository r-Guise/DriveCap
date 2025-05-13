# Robert Guise
# Drive Capital interview

class Person:
    def __init__(self, name):
        self.name = name
        self.strength = {}

    def addConnection(self, company):
        if company not in self.strength:
            self.strength[company] = 1
        else:
            self.strength[company] += 1
