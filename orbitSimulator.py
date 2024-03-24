from vector import *

class system:
    def __init__(self, numOfBodies: int, initialPositions : list[vector], initialVelocities : list[vector], /
                 masses : list[float], gravitationalConstant : float) -> None:
        self.N = numOfBodies
        self.r0 = initialPositions
        self.v0 = initialVelocities
        self.G = gravitationalConstant
        self.M = masses

    def simulate(self, duration : float, timestep : float):
        numOfSteps = duration / timestep
        positions = [self.r0]
        
        for i in range(numOfSteps):
            pass

