import matplotlib.pyplot as plt
import numpy as np
import math

def produzFragmento(x, y):
    xp = math.floor(x) + 0.5
    yp = math.floor(y) + 0.5

    return xp, yp


def rast(x1, y1, x2, y2, resX, resY):
    x1, x2 = x1 * resX, x2 * resX
    y1, y2 = y1 * resY, y2 * resY

    deltaX = x2 - x1
    deltaY = y2 - y1

    if deltaX != 0 and deltaY != 0:
        m = deltaY / deltaX
    else:
        m = 0

    b = y2 - (m * x2)

    x = x1
    y = y1

    xMin = math.floor(min(x1, x2))
    xMax = math.floor(max(x1, x2))

    yMin = math.floor(min(y1, y2))
    yMax = math.floor(max(y1, y2))

    mat = np.zeros((resX, resY), dtype=int)

    xp, yp = produzFragmento(x, y)
    mat[math.floor(xp)][math.floor(yp)] = 1

    if abs(deltaX) > abs(deltaY):
        for x in range(xMin, xMax):
            if deltaY != 0:          
                y = m * x + b
            else: 
                y = y1

            xp, yp = produzFragmento(x, y)
            mat[math.floor(xp)][math.floor(yp)] = 1                                
    else: 
        for y in range(yMin, yMax):
            if deltaX != 0:
                x = (y - b) / m
            else:
                x = x1

            xp, yp = produzFragmento(x, y)
            mat[math.floor(xp)][math.floor(yp)] = 1            


    return mat


if __name__ == '__main__':
    matrix = [
        rast(0.1, 0.1, 0.1, 0.9, 352, 240),
        rast(0.1, 0.1, 0.1, 0.9, 720, 480),
        rast(0.1, 0.1, 0.1, 0.9, 1280, 960)
    ]

    fig, figures = plt.subplots(ncols=3, figsize=(15,7))
    fig = plt.subplots_adjust(wspace=0.5)

    figures[0].set_title('Resolução: 352x240')
    figures[1].set_title('Resolução: 720x480')
    figures[2].set_title('Resolução: 1280x960')

    matrix1 = [
        rast(0.1, 0, 0.75, 0.75, 352, 240),
        rast(0.1, 0, 0.75, 0.75, 720, 480),
        rast(0.1, 0, 0.75, 0.75, 1280, 960)
    ]

    fig1, figures1 = plt.subplots(ncols=3, figsize=(15,7))
    fig1 = plt.subplots_adjust(wspace=0.35)

    figures1[0].set_title('Resolução: 352x240')
    figures1[1].set_title('Resolução: 720x480')
    figures1[2].set_title('Resolução: 1280x960')

    matrix2 = [
        rast(0, 0.9, 0.6, 0.2, 352, 240),
        rast(0, 0.9, 0.6, 0.2, 720, 480),
        rast(0, 0.9, 0.6, 0.2, 1280, 960)
    ]

    fig2, figures2 = plt.subplots(ncols=3, figsize=(15,7))
    fig2 = plt.subplots_adjust(wspace=0.35)
        
    figures2[0].set_title('Resolução: 352x240')
    figures2[1].set_title('Resolução: 720x480')
    figures2[2].set_title('Resolução: 1280x960')

    matrix3 = [
        rast(0.1, 0.2, 0.83, 0.2, 352, 240),
        rast(0.1, 0.2, 0.83, 0.2, 720, 480),
        rast(0.1, 0.2, 0.83, 0.2, 1280, 960)
    ]

    fig3, figures3 = plt.subplots(ncols=3, figsize=(15,7))
    fig3 = plt.subplots_adjust(wspace=0.35)

    figures3[0].set_title('Resolução: 352x240')
    figures3[1].set_title('Resolução: 720x480')
    figures3[2].set_title('Resolução: 1280x960')    

    for figure in range(0, len(matrix)):
        figures[figure].imshow(matrix[figure].T,
                               cmap=plt.cm.gray_r,
                               origin="lower")

    for figure in range(0, len(matrix1)):
        figures1[figure].imshow(matrix1[figure].T,
                                cmap=plt.cm.gray_r,
                                origin="lower")

    for figure in range(0, len(matrix2)):
        figures2[figure].imshow(matrix2[figure].T,
                                cmap=plt.cm.gray_r,
                                origin="lower")
    
    for figure in range(0, len(matrix3)):
        figures3[figure].imshow(matrix3[figure].T,
                                cmap=plt.cm.gray_r,
                                origin="lower")                                

    plt.show()