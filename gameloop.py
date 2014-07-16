import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

"""Woking gameloop implemented using glutDisplayFunc(). also initializes a opengl window. """

window =0
width,height = 800,500
name=b"test"

def draw():
	"""skeleton function"""
	gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) #clear screen
	gl.glLoadIdentity() #reset postition


	glut.glutSwapBuffers() #allows doouble buffering




#initialization

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_RGBA | glut.GLUT_DOUBLE | glut.GLUT_ALPHA | glut.GLUT_DEPTH)
glut.glutInitWindowSize(width,height)
glut.glutInitWindowPosition(0,0)
window = glut.glutCreateWindow(name)
glut.glutDisplayFunc(draw) #calls function draw on user action, ie keyboard or mouseclick.
glut.glutIdleFunc(draw) #substitute for gameloop. calls function draw all the time
glut.glutMainLoop() #starts everything going.
