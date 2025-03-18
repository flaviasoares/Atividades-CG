from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)

def draw_flower():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Caule
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(249.0, 250.0)
    glVertex2f(251.0, 250.0)
    glVertex2f(251.0, 100.0)
    glVertex2f(249.0, 100.0)
    glEnd()
    
    # Primeira pétala
    glColor3f(0.7, 0.3, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(250.0, 250.0)
    glVertex2f(230.0, 200.0)
    glVertex2f(270.0, 200.0)
    glEnd()
    
    # Segunda pétala
    glBegin(GL_TRIANGLES)
    glVertex2f(250.0, 250.0)
    glVertex2f(300.0, 230.0)
    glVertex2f(300.0, 270.0)
    glEnd()
    
    # Terceira pétala
    glBegin(GL_TRIANGLES)
    glVertex2f(250.0, 250.0)
    glVertex2f(270.0, 300.0)
    glVertex2f(230.0, 300.0)
    glEnd()
    
    # Quarta pétala
    glBegin(GL_TRIANGLES)
    glVertex2f(250.0, 250.0)
    glVertex2f(200.0, 270.0)
    glVertex2f(200.0, 230.0)
    glEnd()
    
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    glutCreateWindow(b"Picole")

    init()
    glutDisplayFunc(draw_flower)
    glutMainLoop()
    
if __name__ == "__main__":
    main()
