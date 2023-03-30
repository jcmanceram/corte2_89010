import random

def procesar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(1, 100)) 
        matriz.append(fila)
        
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    num_mas_alto = matriz[0][0]
    pos_mas_alta = [0, 0]
    num_mas_bajo = matriz[0][0]
    pos_mas_baja = [0, 0]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > num_mas_alto:
                num_mas_alto = matriz[i][j]
                pos_mas_alta = [i, j]
            if matriz[i][j] < num_mas_bajo:
                num_mas_bajo = matriz[i][j]
                pos_mas_baja = [i, j]
    
    print("El número más alto es", num_mas_alto, "en la posición", pos_mas_alta)
    print("El número más bajo es", num_mas_bajo, "en la posición", pos_mas_baja)
    
    i, j = pos_mas_alta
    temp = matriz[0][0]
    matriz[0][0] = matriz[i][j]
    matriz[i][j] = temp
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0 and j == 0:
                continue
            elif i == 0 and j > 0:
                if matriz[i][j] < matriz[i][j-1]:
                    temp = matriz[i][j]
                    matriz[i][j] = matriz[i][j-1]
                    matriz[i][j-1] = temp
            elif i > 0 and j == 0:
                if matriz[i][j] < matriz[i-1][j]:
                    temp = matriz[i][j]
                    matriz[i][j] = matriz[i-1][j]
                    matriz[i-1][j] = temp
            else:
                if matriz[i][j] < matriz[i-1][j] or matriz[i][j] < matriz[i][j-1]:
                    if matriz[i-1][j] > matriz[i][j-1]:
                        temp = matriz[i][j]
                        matriz[i][j] = matriz[i-1][j]
                        matriz[i-1][j] = temp
                    else:
                        temp = matriz[i][j]
                        matriz[i][j] = matriz[i][j-1]
                        matriz[i][j-1] = temp
    
    print("Matriz ordenada del número más alto:")
    for fila in matriz:
        print(fila)
if __name__=='__main__':
    procesar_matriz(5, 10)