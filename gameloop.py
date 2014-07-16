import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

"""Woking gameloop implemented using glutDisplayFunc(). also initializes a opengl window. 
This is class is the gameloop, it will update and display the particles as they move.

In particular it should:
initiate the openGL and display stuff
allow user input for the type, interaction strength, size and number of the particles
create all the particles
update the system
allow for user control of the system ( as above, but also user interaction with the particles)."""



class GameLoop(object)
 
    '''-------------Fields----------------------------------------------'''
    
    window =0
    width,height = 800,500
    name=b"test"
    maxParticles=200 # the maximum number of allowed particles
    numParticles=0 # the number of particles may be predecided for chosen by the user
    #need to initialise the following array
    particles= 0 # an array to hold all the particles

    '''-------------Methods---------------------------------------------'''

    '''the initialistion method'''
    def __init__(self):
        #initialization the gl interface

        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_RGBA | glut.GLUT_DOUBLE | glut.GLUT_ALPHA | glut.GLUT_DEPTH)
        glut.glutInitWindowSize(width,height)
        glut.glutInitWindowPosition(0,0)
        window = glut.glutCreateWindow(name)
        glut.glutDisplayFunc(draw) #calls function draw on user action, ie keyboard or mouseclick.
        glut.glutIdleFunc(draw) #substitute for gameloop. calls function draw all the time
        glut.glutMainLoop() #starts everything going.
    
        self.newSim # start a new particles simulation
    
        # possible add some buttons/user entry of parameters for the simulator
    
    

    '''skeleton function'''
    def draw():
    	
    	gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) #clear screen
    	gl.glLoadIdentity() #reset postition


    	glut.glutSwapBuffers() #allows doouble buffering

    '''Start a new particle simulation
    -initialise the particles array and clear the graphics plane. 
    -possibly called by a button'''
    def newSim():
        # clear the gl graphics
        self.numParticles=0;
        self.particles=0;# create a new array of particles
    
def main():
    game = GameLoop() 

