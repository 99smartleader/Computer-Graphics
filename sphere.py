import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *




def sphere(s):
    quad = gluNewQuadric()
    
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 64.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1,1,1,1])
    gluQuadricNormals(quad, GLU_SMOOTH)
    glPushMatrix()
    #glTranslatef(1, 1, 1)
    glColor(0, 0, 1, 0)
    gluSphere(quad,s,5,5)
    glPopMatrix()
    
def main():
    pygame.init()
    display = (1000,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        sphere(1)
        pygame.display.flip()
        pygame.time.wait(10)


main()

