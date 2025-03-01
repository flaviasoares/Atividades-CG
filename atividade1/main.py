import matplotlib.pyplot as plt
import bresenham as bresenham

def main():

    x1, y1 = 1, 1
    x2, y2 = 8, 5

    pontos_calculados = bresenham.bresenham(x1, y1, x2, y2)

    print("Pontos calculados pelo algoritmo de Bresenham:", pontos_calculados)

    # Plotando os pontos
    x_values, y_values = zip(*pontos_calculados)

    plt.figure(figsize=(6, 4.2))
    plt.plot(x_values, y_values, marker='o', color='blue', linestyle='dashed', label="Bresenham")
    plt.xticks(range(min(x_values) - 1, max(x_values) + 2))
    plt.yticks(range(min(y_values) - 1, max(y_values) + 2))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Algoritmo de Bresenham - Segmento de Reta")
    plt.legend()
    plt.show()

main()

