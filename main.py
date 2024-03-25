from orbitSimulator import *
from animator import *
from inputFromTextFile import *



def main():
    
    filename = input("input the .csv filename: ")
    #filename = "input.csv"

    bodies, G, dt, dur = inputParameters(filename)


    Sys = system(bodies, G)
    Positions = Sys.simulate(dur+1, dt) #motion is numerically simulated one second longer than animation duration

    masses = []
    for i in Sys.bodies:
        masses.append(i.m)

    Animator = animator(Positions, masses, dt)
    Animator.animate(dur)


main()