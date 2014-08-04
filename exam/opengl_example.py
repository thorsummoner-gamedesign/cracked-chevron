from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import *
import numpy
import PIL as Image
import sys
import math

ESCAPE = '\033'

window = 0
ID = 0

#rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

DIRECTION = 1

texture  = 0
textureWall = 1
angle = 0

camx = 0
camz = -10

image = ""
image2 = ""

def InitGL(Width, Height):

	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClearDepth(1.0)
	glDepthFunc(GL_LESS)
	glEnable(GL_DEPTH_TEST)
	glShadeModel(GL_SMOOTH)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 8000.0)
	glMatrixMode(GL_MODELVIEW)

	# initialize texture mapping
	glEnable(GL_TEXTURE_2D)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def keyPressed(*args):
	global X_AXIS,Y_AXIS,Z_AXIS
	global camx, camz,angle

	if args[0] == ESCAPE:
		sys.exit()

	if args[0] == 'a':
		Y_AXIS = Y_AXIS - 1.6;
		angle -= 1.6

	if args[0] == 'd':
		Y_AXIS = Y_AXIS + 1.6;
		angle += 1.6


	if args[0] == 'w':
		camx += math.sin(math.radians(-angle))*0.15
		camz += math.cos(math.radians(-angle))*0.15

	if args[0] == 's':
		camx -= math.sin(math.radians(-angle))*0.15
		camz -= math.cos(math.radians(-angle))*0.15

def DrawGLScene():
	global X_AXIS,Y_AXIS,Z_AXIS
	global DIRECTION

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glLoadIdentity()
	glTranslatef(0.0+camx,0.0,0.0+camz)

	glTranslatef(0.0-camx,0.0,0.0-camz)
	glRotatef(X_AXIS,1.0,0.0,0.0)
	glRotatef(Y_AXIS,0.0,1.0,0.0)
	glRotatef(Z_AXIS,0.0,0.0,1.0)
	glTranslatef(0.0+camx,0.0,-0.0+camz)

	#        glBindTexture(GL_TEXTURE_2D, ID)

	#glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)
	glPushMatrix();

	glTranslatef(-2.0,0.0,-10.0)
	#        glBindTexture(GL_TEXTURE_2D, image)
	glRotatef(90,1,0,0);

	glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)

	mySphere2 = gluNewQuadric()
	gluQuadricNormals(mySphere2, GL_SMOOTH)
	gluQuadricTexture(mySphere2, GL_TRUE)

	gluSphere(mySphere2,200.0, 20, 200);

	glPopMatrix();

	glPushMatrix();

	glRotatef(DIRECTION,0,1,0);

	glBindTexture(GL_TEXTURE_2D, textureWall)   # 2d texture (x and y size)

	mySphere = gluNewQuadric()
	gluQuadricNormals(mySphere, GL_SMOOTH)
	gluQuadricTexture(mySphere, GL_TRUE)

	gluSphere(mySphere,2.0, 20, 200);


	glPopMatrix();
							# X_AXIS = X_AXIS - 0.30
							# Z_AXIS = Z_AXIS - 0.30

	DIRECTION += 0.3

	glutSwapBuffers()



def loadTexture ( fileName, texture ):
	image  = open ( fileName )
	width  = 100
	height = 100
	image  = image.read(); ( "raw", "RGBX", 0, -1 )

	#    texture = glGenTextures ( 1 )
	glBindTexture     ( GL_TEXTURE_2D, texture )
	glPixelStorei     ( GL_UNPACK_ALIGNMENT,1 )
	glTexParameterf   ( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
	glTexParameterf   ( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
	glTexParameteri   ( GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR )
	glTexParameteri   ( GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR )
	gluBuild2DMipmaps ( GL_TEXTURE_2D, 3, width, height, GL_RGBA, GL_UNSIGNED_BYTE, image )

	return texture


def main():

	global window
	global ID


	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glutInitWindowSize(640,480)
	glutInitWindowPosition(200,200)

	window = glutCreateWindow('OpenGL Python Universe Model')

	loadTexture ( "space.jpg", texture )
	loadTexture ( "earth.jpg", textureWall )

	glutDisplayFunc(DrawGLScene)
	glutIdleFunc(DrawGLScene)
	glutKeyboardFunc(keyPressed)
	InitGL(640, 480)
	#	loadImage()

	glutMainLoop()

if __name__ == "__main__":
								main()
