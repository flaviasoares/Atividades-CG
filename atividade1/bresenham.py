def bresenham(x1, y1, x2, y2):
    pontos = []
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx # Valor inicial de d
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    x = x1
    y = y1

    pontos.append((x, y))
    print(f'd = 2 * {dy} - {dx} = {d}')
    while (x < x2):

        if (d <= 0):
            # Escolhe E
            d += incE
            print(f'd = {d - incE} + 2 * {dy} = {d}')
            x += 1
        else:
            # Escolhe NE
            d += incNE
            print(f'd = {d - incNE} + 2 * ({dy} - {dx}) = {d}')
            x += 1
            y += 1

        pontos.append((x, y))
    
    return pontos


