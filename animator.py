from vector import *
import graphics as gr
import time as t

class animator:
    def __init__(self, positions : list[list[vector]], masses : list[float], dt : float) -> None:
        self.positions = positions
        self.masses = masses
        self.dt = dt

    def animate(self, duration : float):

        windowWidth = 700
        windowHeight = 700
        window = gr.GraphWin("Gravitational System Evolution", windowWidth, windowHeight)
        window.setBackground("black")
        window.setCoords(0,windowHeight,windowWidth,0)
        
        

        animationLenght = duration
        frameRate = 1/60
        numOfFrames = int(animationLenght/frameRate)
        AnimationPositions = []

        for i in range(numOfFrames):
            AnimationPositions.append(self.positions[int(i*frameRate/self.dt)])


        AllXcoord = []
        AllYcoord = []
        for i in AnimationPositions:
             for ii in i:
                  AllXcoord.append(ii.X)
                  AllYcoord.append(ii.Y)

        minX = min(AllXcoord)
        maxX = max(AllXcoord)
        minY = min(AllYcoord)
        maxY = max(AllYcoord)
        Xrange = maxX - minX
        Yrange = maxY - minY
        if Xrange > Yrange:
             rrange = Xrange
        else:
             rrange = Yrange
        Xcentar = (maxX + minX)/2
        Ycentar = (maxY + minY)/2

        DisplayPositions = []
        for i in AnimationPositions:
            DisplayPositions_ = []
            for ii in i:
                DP = vector(windowWidth/2, windowHeight/2) + \
                    (ii - vector(Xcentar, Ycentar)) * (windowHeight/rrange)
                DP.X = int(DP.X)
                DP.Y = int(DP.Y)
                DisplayPositions_.append(DP)
            DisplayPositions.append(DisplayPositions_)
            

        sizes = []
        minMass = min(self.masses)
        for i in self.masses:
             size = int(4 * m.sqrt(i/minMass))
             sizes.append(size)


        for i in DisplayPositions:
            Circles = []

            for j, ii in enumerate(i):
                Pt = gr.Point(ii.X, ii.Y)
                Cir = gr.Circle(Pt, sizes[j])
                Cir.setFill("white")
                Circles.append(Cir)
                Circles[j].draw(window)

            t.sleep(frameRate)

            for ii in Circles:
                ii.undraw()

        for i in Circles:
            i.draw(window)


        Text=gr.Text(gr.Point(int(windowWidth/2),int(windowHeight/10)),"ANIMATION FINISHED")
        Text.setOutline("white")
        Text.draw(window)

        Text1=gr.Text(gr.Point(int(windowWidth/2),int(2*windowHeight/10)),"Press Enter to repeat")
        Text1.setOutline("white")
        Text1.draw(window)

        Text2=gr.Text(gr.Point(int(windowWidth/2),int(3*windowHeight/10)),"Press ESC to exit")
        Text2.setOutline("white")
        Text2.draw(window)

        def keyPress():
                key = window.getKey()
                if key == "Return":
                    window.close()
                    self.animate(duration)
                elif key == "Escape":
                    window.close()
                else: keyPress()


        keyPress()




