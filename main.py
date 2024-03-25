from orbitSimulator import *
from animator import *
from inputFromTextFile import *



def main():
    
    bodies, G, dt, dur = inputParameters()


    Sys = system(bodies, G)
    Positions = Sys.simulate(dur+1, dt) #simulation is created one second longer than animation

    Animator = animator(Positions)
    Animator.animate(dur)


main()