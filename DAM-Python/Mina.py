def crearMatriz(f,c):
    matriz = []

    for i in range(f):
        matriz.append([])
        for j in range(c):
            matriz[i].append("-")
    return matriz

def imprimirMatriz(matriz,f,c):
    print("---------------------")
    for i in range(f):
        print (end= "| ")
        for j in range(c):
            print (matriz[i][j], end= " | ")
        print("\n---------------------")

print("Celia")
print("Creamos la matriz:")
f = 5
c = 5
matriz = crearMatriz(f,c)
imprimirMatriz(matriz,f,c)
