from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pos = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

def catavento():
    global pos
    glPushMatrix() 

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.03, 0)
    glVertex2f(0.03, 0)
    glVertex2f(0.03, 3)
    glVertex2f(-0.03, 3)
    glEnd()

    glTranslatef(0, 3, 0)

    glRotatef(pos, 0, 0, 1)

    colors = [(1, 0.5, 0), (1, 1, 0), (0, 0.8, 1), (1, 0, 0.5)]
    for _ in range(4):
        glColor3f(*colors[_])
        glBegin(GL_POLYGON)
        glVertex2f(0.5, 0.0)
        glVertex2f(0.5, 0.5)
        glVertex2f(0.0, 1.5)
        glVertex2f(0.0, 0.0)
        glEnd()
        glRotatef(90, 0, 0, 1)

    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    catavento()
    glFlush()

def keyboard(key, x, y):
    global pos
    if key == b'\x1b':
        glutLeaveMainLoop()
    elif key == b'd':
        pos -= 10
    elif key == b'a':
        pos += 10
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    glutCreateWindow(b"Catavento")

    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
