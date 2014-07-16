'''We want an abstract class that creats particles in there most general sense. 
This class is then extended by more specfic particles, ie attractors etc'''

class particle(object): 
    
    
    '''----------Fields----------'''
    # variable to be set at the creatation of the particle
    xPosition=0 
    yPosition=0
    xVelocity=0
    yVelocity=0
    xAcceleration=0
    yAcceleration=0
    particleType=0
    isBound=True # is the particle bound by the edge of the window
    #if so then the particle needs to know the edge of the window
    width=0 
    height=0
    #WE ASSUME THAT (0,0) is the top left corner of the window
    
    #NOTE: there are two initiation methods, the chose of the initiation method depends on
    # if bounds are wanted or not. Use the desired initiation method and everything should be okay as long as you are consistent
    
    #initiation method without bounds
    def __init__(self,xPos,yPos,xVel,yVel,xAcc,yAcc,partType):
        self.xPosition=xPos
        self.yPosition=yPos
        self.xVelocity=xVel
        self.yVelocity=yVel
        self.xAcceleration=xAcc
        self.yAcceleration=yAcc
        isBound=False
        self.particleType=partType
    
    #initiation method with bounds
    def __init__(self,xPos,yPos,xVel,yVel,xAcc,yAcc,w,h,partType):
        self.xPosition=xPos
        self.yPosition=yPos
        self.xVelocity=xVel
        self.yVelocity=yVel
        self.xAcceleration=xAcc
        self.yAcceleration=yAcc
        self.width=w
        self.height=h
        isBound=True
        self.particleType=partType
    
    '''----methods for returning the state of the particle------'''
    
    def getXPos(self):
        return self.xPosition
        
    def getYPos(self):
        return self.yPosition
        
    def getXVel(self):
        return self.xVelocity
        
    def getYVel(self):
        return self.yVelocity
        
    def getXAcc(self):
        return self.xAcceleration
    
    def getYAcc(self):
        return self.yAcceleration
        
    def getType(self):
        return self.particelType 
    
    '''----methods for setting the position of the particle------'''
    
    def setXPos(newXPos):
        self.xPosition=newXPos
        return true
        
    def setYPos(newYPos):
        self.yPosition=newYPos
        return true
        
    def setXVel(newXVel):
      self.xVelocity=newXVel
      return true
        
    def setYVel(newYVel):
      self.yVelocity=newYVel
      return true
    
    def setXAcc(newXAcc):
        self.xAcceleration=newXAcc
        return true
    
    def setYAcc(newYAcc):
        self.yAcceleration=newYAcc
        return true
        
    def setType(newType):
        self.particleType=newType
        return true 
        
    '''----methods for incrementing the state of the particle------'''
    
    def increment(self,newXAcc,newYAcc):
        #This method updates the current state of the particle such that it is
        #consistent with the current state of the particle.
        self.xPosition+=self.xVelocity
        self.yPosition+=self.yVelocity
        self.xVelocity+=self.xAcceleration
        self.yVelocity+=self.yAcceleration
        self.xAcceleration=newXAcc
        self.yAcceleration=newYAcc
        
        if (isBound==True):
            reflectParticle() # this method ensures that the particle stays in the window
        
        #return the position of the particle
        return (self.xPosition,self.yPosition)
        
    def reflectParticle(self):
        #reflection off the right edge
        if (xPosition>width):
            xPosition=width
            xVelocity=-xVelocity
        #reflection off the left edge
        if (xPosition<0):
            xPosition=0
            xVelocity=-xVelocity
        #reflection off the top edge
        if (yPosition<0):
            yPosition=0
            yVelocity=-yVelocity
        #relfection off the bottom edge
        if(yPosition>height):
            yPosition=height
            yVelocity=-yVelocity
            