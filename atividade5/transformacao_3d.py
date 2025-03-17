from OpenGL.GL import *
from OpenGL.GLUT import * 
from OpenGL.GLU import *
import math


angle_sun = 0
angle_planet1 = 0
angle_planet2 = 0
angle_moon1 = 0
angle_moon2 = 0
move_planets = False 

def draw_circle(radius, slices=30):
    segments = slices
    glBegin(GL_POLYGON)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_scene():
    global angle_sun, angle_planet1, angle_planet2, angle_moon1, angle_moon2

    glPushMatrix()
    glColor(1, 1, 0)
    draw_circle(0.2)
    glPopMatrix()

    glPushMatrix()
    glRotatef(angle_planet1, 0, 0, 1)
    glTranslatef(1.0, 0.0, 0.0)
    glColor(0, 0, 1)
    draw_circle(0.1)

    glPushMatrix()
    glRotatef(angle_moon1, 1, 0, 0)
    glTranslatef(0.3, 0.0, 0.0)
    glColor(0.5, 0.5, 0.5)
    draw_circle(0.05)
    glPopMatrix()

    
    glPushMatrix()
    glRotatef(angle_moon2, 1, 1, 0)
    glTranslatef(0.4, 0.0, 0.0)  
    glColor(0.7, 0.7, 0.7)  
    draw_circle(0.05)
    glPopMatrix()

    glPopMatrix()
    
    glPushMatrix()
    glRotatef(angle_planet2, 0, 0, 1)
    glTranslatef(-1.5, 0.0, 0.0)  
    glColor(0, 1, 0)  
    draw_circle(0.1)
    glPopMatrix()


def update_scene(value):
    global angle_sun, angle_planet1, angle_planet2, angle_moon1, angle_moon2

    if move_planets:
        angle_sun += 0.1
        angle_planet1 += 0.2  
        angle_planet2 -= 0.2  
        angle_moon1 += 0.5  
        angle_moon2 += 0.4  

    glutPostRedisplay()
    glutTimerFunc(16, update_scene, 0)


def key_pressed(key, x, y):
    global move_planets
    if key == b'y' or key == b'Y':
        move_planets = True

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2, 2, -2, 2)  
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_scene()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Sistema Solar com Planetas e Luas")
    init()
    
    glutDisplayFunc(display)
    glutKeyboardFunc(key_pressed)
    glutTimerFunc(25, update_scene, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
