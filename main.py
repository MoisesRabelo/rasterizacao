import matplotlib.pyplot as plt
import numpy as np
import math

def rasterizar(reta, resolucao):
    x1 = reta[0][0] * resolucao[0]
    x2 = reta[1][0] * resolucao[0]
    y1 = reta[0][1] * resolucao[1]
    y2 = reta[1][1] * resolucao[1]

    deltaX = (x2 - x1)
    deltaY = (y2 - y1)

    x = x1
    y = y1

    m = 0
    if deltaX != 0 and deltaY != 0:
        m = deltaY/deltaX
    
    b = y - m * x

    minX = math.floor(min(x1, x2))
    maxX = math.floor(max(x1, x2))

    minY = math.floor(min(y1, y2))
    maxY = math.floor(max(y1, y2))

    matriz = np.zeros((resolucao[0], resolucao[1]))

    xp, yp = produzFragmento(x, y)
    matriz[math.floor(xp)][math.floor(yp)] = 1

    if abs(deltaX) > abs(deltaY):
        for x in range(minX, maxX):
            if deltaY != 0:
                y = m * x + b
            else:
                y = y1
            xp, yp = produzFragmento(x, y)
            matriz[math.floor(xp)][math.floor(yp)] = 1
    else:
        for y in range(minY, maxY):
            if deltaX != 0:
                x = (y - b)/m
            else:
                x = x1
            xp, yp = produzFragmento(x, y)
            matriz[math.floor(xp)][math.floor(yp)] = 1
    return matriz

def produzFragmento(x, y):
    xp = math.floor(x) + 0.5
    yp = math.floor(y) + 0.5

    return xp, yp

if __name__ == '__main__':
    
    reta1 = np.array([[0.5, 0.5], [0.5, 0.8]])
    reta2 = np.array([[0.1, 0], [0.75, 0.75]])
    reta3 = np.array([[0.1, 0.9], [0.6, 0.2]])
    reta4 = np.array([[0.1, 0.2], [0.83, 0.2]])

    resolucao = np.array([[100, 75], [600, 300], [800, 1200]])

    for i in range(len(resolucao)):
        fig, figures = plt.subplots(ncols = 4, figsize = (15, 7), facecolor = 'lime')
        fig.suptitle("Resolução: {resolucao}".format(resolucao = resolucao[i]))

        matriz = [rasterizar(reta1, resolucao[i]), rasterizar(reta2, resolucao[i]),
                rasterizar(reta3, resolucao[i]), rasterizar(reta4, resolucao[i])]

        for figure in range(0, len(matriz)):
            figures[figure].imshow(matriz[figure].T,
                                cmap='PRGn_r')

    plt.show()