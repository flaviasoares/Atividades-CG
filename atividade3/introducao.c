#include <GL/glut.h> 

void init(void)
{
    /* selecionar cor de fundo (preto) */
    glClearColor (0.0, 0.0, 0.0, 0.0);
    
    glMatrixMode (GL_PROJECTION); //Projecao
    
    gluOrtho2D(0.0, 500.0, 0.0, 500.0); //Definindo os limites da Porta de Visao (ViewPort)
    
}

void picoleFunc(void)
{
    /* Limpar todos os pixels  */
    glClear (GL_COLOR_BUFFER_BIT);
    
    glColor3f(0.0, 1.0, 0.0);
    glBegin(GL_POLYGON);
        glVertex2f (249.0f, 250.0f);
        glVertex2f (251.0f, 250.0f);
        glVertex2f (249.0f, 100.0f);
        glVertex2f (251.0f, 100.0f);
    glEnd();
    
    /* Desenhar um polígono branco  */
    // PRIMEIRO 
    glColor3f(0.7, 0.3, 1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f (250.0f, 250.0f);
        glVertex2f (230.0f, 200.0f);
        glVertex2f (270.0f, 200.0f);
    glEnd();
    
    // SEGUNDO
    glColor3f(0.7, 0.3, 1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f(250.0f, 250.0f);
        glVertex2f(300.0f, 230.0f);
        glVertex2f(300.0f, 270.0f);
    glEnd();

    //TERCEIRO
    glColor3f(0.7, 0.3, 1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f (250.0f, 250.0f);
        glVertex2f (270.0f, 300.0f);
        glVertex2f (230.0f, 300.0f);
    glEnd();

    //QUARTO
    glColor3f(0.7, 0.3, 1.0);
    glBegin(GL_TRIANGLES);
        glVertex2f (250.0f, 250.0f);
        glVertex2f (200.0f, 270.0f);
        glVertex2f (200.0f, 230.0f);
    glEnd();
        
    /* Não esperar! */
    glFlush ();
}



int main(int argc, char** argv) {
    
	glutInit(&argc, argv);
    
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize (500, 400);
	glutInitWindowPosition (200, 200);
	glutCreateWindow ("Picole");
    
	init (); //iniciar a Viewport
    
	glutDisplayFunc(picoleFunc);
    
	glutMainLoop();
	    
}