from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


angle_planet1 = 0  # Ângulo do primeiro planeta (gira para a esquerda)
angle_planet2 = 0  # Ângulo do segundo planeta (gira para a direita)
angle_moon1 = 0  # Ângulo da primeira lua (translação no eixo X)
angle_moon2 = 0  # Ângulo da segunda lua (translação no eixo XY)
move_planets = False

def draw_circle(radius, slices=30):
    glBegin(GL_POLYGON)
    for i in range(slices):
        angle = 2 * math.pi * i / slices
        glVertex2f(radius * math.cos(angle), radius * math.sin(angle))
    glEnd()

def draw_solar_system():
    global angle_planet1, angle_planet2, angle_moon1, angle_moon2

    # Desenha o Sol
    glPushMatrix()
    glColor3f(1, 1, 0)  # Amarelo
    draw_circle(0.2)
    glPopMatrix()

    # Planeta 1 (gira para a esquerda)
    glPushMatrix()
    glRotatef(angle_planet1, 0, 0, 1)  # Translação ao redor do Sol
    glTranslatef(1.0, 0.0, 0.0)  # Distância do Sol

    # Define cores diferentes para frente e trás das luas
    front_moon_color = (0.7, 0.7, 0.7)  # Cinza claro
    back_moon_color = (0.4, 0.4, 0.4)  # Cinza escuro

    # POSIÇÕES DAS LUAS
    x_moon1 = 0.3 * math.cos(math.radians(angle_moon1))
    y_moon1 = 0.0  # Apenas no eixo X

    x_moon2 = 0.35 * math.cos(math.radians(angle_moon2))
    y_moon2 = 0.35 * math.sin(math.radians(angle_moon2)) * 0.7  # Inclinado no eixo XY

    # Se a lua está atrás do planeta (X < 0), desenhe-a primeiro
    if x_moon1 < 0:
        glPushMatrix()
        glTranslatef(x_moon1, y_moon1, 0.0)
        glColor3f(*back_moon_color)
        draw_circle(0.05)
        glPopMatrix()

    if x_moon2 < 0:
        glPushMatrix()
        glTranslatef(x_moon2, y_moon2, 0.0)
        glColor3f(*back_moon_color)
        draw_circle(0.05)
        glPopMatrix()

    # Desenha o planeta (sempre depois das luas que estão atrás)
    glColor3f(0, 0, 1)  # Azul
    draw_circle(0.1)

    # Se a lua está na frente do planeta (X >= 0), desenhe depois do planeta
    if x_moon1 >= 0:
        glPushMatrix()
        glTranslatef(x_moon1, y_moon1, 0.0)
        glColor3f(*front_moon_color)
        draw_circle(0.05)
        glPopMatrix()

    if x_moon2 >= 0:
        glPushMatrix()
        glTranslatef(x_moon2, y_moon2, 0.0)
        glColor3f(*front_moon_color)
        draw_circle(0.05)
        glPopMatrix()

    glPopMatrix()  # Fim do planeta 1 e suas luas

    # Planeta 2 (gira para a direita)
    glPushMatrix()
    glRotatef(angle_planet2, 0, 0, 1)  # Translação ao redor do Sol
    glTranslatef(-1.5, 0.0, 0.0)  # Distância do Sol
    glColor3f(0, 1, 0)  # Verde
    draw_circle(0.1)
    glPopMatrix()

# Atualiza os ângulos de rotação
def update_solar_system(value):
    global angle_planet1, angle_planet2, angle_moon1, angle_moon2

    if move_planets:
        angle_planet1 += 0.5  # Gira para a esquerda
        angle_planet2 -= 0.5  # Gira para a direita
        angle_moon1 += 2.0  # A primeira lua orbita rapidamente no eixo X
        angle_moon2 += 2.0  # A segunda lua orbita inclinada

    glutPostRedisplay()
    glutTimerFunc(16, update_solar_system, 0)

# Captura da tecla Y para iniciar o movimento
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
    draw_solar_system()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(800, 800)
    glutCreateWindow("Movimento de Translação - OpenGL")
    init()

    glutDisplayFunc(display)
    glutKeyboardFunc(key_pressed)
    glutTimerFunc(25, update_solar_system, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
