import csv
import orbitSimulator as orbSim
from vector import *

def inputParameters(filename):
    positionX = []
    positionY = []
    velocityX = []
    velocityY = []
    mass = []


    with open(filename) as fileObj:
        next(fileObj)
        next(fileObj)
        next(fileObj)
        next(fileObj)
        next(fileObj)
        reader_obj = csv.reader(fileObj)
        firstRow = True
        for row in reader_obj: 
            if firstRow:
                dt = float(row[0])
                duration = float(row[1])
                G = float(row[2])
                firstRow = False
            else:
                positionX.append(float(row[0]))
                positionY.append(float(row[1]))
                velocityX.append(float(row[2]))
                velocityY.append(float(row[3]))
                mass.append(float(row[4]))
    
    bodies = []
    for i in range(len(mass)):
        body = orbSim.body(vector(positionX[i], positionY[i]), vector(velocityX[i], velocityY[i]), mass[i])
        bodies.append(body)
    
    return bodies, G, dt, duration

    