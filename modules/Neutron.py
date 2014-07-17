'''We want a neutral particle class. A class for particles that are neutral in the sense that they are not attractive nor repulsive.

Charactoristics
* A fixed mass
* non-attractive
* non-repulsive
 
Is a class that inherits from the particle class.'''

#might need to import the partile class

class Neutron(Particle):
    
    #initiation method without bounds
    def __init__(self,xPos,yPos,xVel,yVel,xAcc,yAcc):
        Particle.__init__(self,xPos,yPos,xVel,yVel,xAcc,yAcc,"Neutron")
    
    #initiation method with bounds
    def __init__(self,xPos,yPos,xVel,yVel,xAcc,yAcc,w,h):
        Particle.__init__(self,xPos,yPos,xVel,yVel,xAcc,yAcc,w,h,"Neutron")