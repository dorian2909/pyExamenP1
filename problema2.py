
if __name__ == '__main__':

    # Definir las dos matrices de datos
    matriz_datos_uno = [
        [4, 5],
        [7, 8]
    ]

    matriz_datos_dos = [
        [9, 2, 2, 2],
        [3, 4, 5, 1],
        [6, 7, 8, 3],
        [2, 8, 2, 5]
    ]

    # valido si las dimensiones de la matriz de datos uno son menores que las dimensiones de la matriz de datos dos
    if len(matriz_datos_uno) > len(matriz_datos_dos) or len(matriz_datos_uno[0]) > len(matriz_datos_dos[0]):
        print("La matriz de datos uno no puede estar contenida en la matriz de datos dos")
    else:

        for i in range(len(matriz_datos_uno)):
            for j in range(len(matriz_datos_uno)):
                if matriz_datos_uno not in matriz_datos_dos:
                    print("La matriz de datos uno está contenida en la matriz de datos dos")
                    break
                else:
                   print("La matriz de datos uno no está contenida en la matriz de datos dos")





