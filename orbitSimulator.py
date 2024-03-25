from vector import *


class body:
    def __init__(self, position : vector, velocity : vector, Mass : float, acceleration : vector = vector(0,0)) -> None:
        self.R = position
        self.V = velocity
        self.A = acceleration
        self.m = Mass

    def updatePositionVelocity(self, dt : float):
        self.V = self.V + (self.A * dt)
        self.R = self.R + (self.V * dt)


class system:
    def __init__(self, bodies : list[body], gravitationalConstant : float) -> None:
        self.N = len(bodies)
        self.bodies = bodies
        self.G = gravitationalConstant

    def simulate(self, duration : float, timestep : float) -> list[list[vector]]:
        numOfSteps = int(duration / timestep)
        positions = []
        for i in range(numOfSteps):

            positions.append([self.bodies[n].R for n in range(self.N)])

            Fkj = computeForces(self.bodies, self.G)

            Fk = []
            rdotdot = []

            for ii in range(self.N):
                F = sum(Fkj[ii])
                rdotdot = F * (1/self.bodies[ii].m)
                self.bodies[ii].A = rdotdot
                self.bodies[ii].updatePositionVelocity(timestep)

        return positions

            



def computeForces(bodies : list[body], gravitationalConstant : float):
    G = gravitationalConstant
    Fkj = []
    for i, b in enumerate(bodies):
        F_j = []
        for ii, bb in enumerate(bodies):
            if i == ii:
                F__ = vector(0, 0)
            else:
                r = bb.R - b.R
                F__ = (r) * (G*bb.m*b.m/((r.abs())**3))
            F_j.append(F__)
        Fkj.append(F_j)
    return Fkj