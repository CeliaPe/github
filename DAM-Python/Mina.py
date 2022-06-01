import random

def crearMatriz(f,c):
    matriz = []

    for i in range(f):
        matriz.append([])
        for j in range(c):
            matriz[i].append("-")
    return matriz

def rellenarMatriz(matriz,f,c,dicElementos):
    for i in range(f):
        for j in range(c):
            matriz[i][j] = elementoAleatorio(list(dicElementos.keys()))


def elementoAleatorio(elementos):
    numRandom = random.randint(0,len(elementos)-1)
    return elementos[numRandom]

def imprimirMatriz(matriz,f,c):
    print("---------------------")
    for i in range(f):
        print (end= "| ")
        for j in range(c):
            print (matriz[i][j], end= " | ")
        print("\n---------------------")

def siguienteTurno(turno):
    return (turno+1)%2

def haGanado(listaPuntos):
    # Ponemos el jugador a -1 para al entrar en el bucle que aumente y empieza
    # en la posición 0.
    jugador = -1
    ganar = False
    # Mientras no hayamos ganado y sigua habiendo jugadores en la lista, segui-
    # mos comprobando si algun jugador supera los 10 puntos.
    while(not ganar and jugador < len(listaPuntos)-1):
        jugador += 1
        # En el momento en el que algun jugador supera los 10 puntos ganar es
        # cierto.
        if listaPuntos[jugador] >= 10:
            ganar = True
    # Si hemos salido del bucle sin que nadie gane ponemos el jugador a -1 para 
    # que no sea un valor válido de posición de jugador.
    if (not ganar):
        jugador = -1                                           # Codigo de error
    # Devolvemos jugador, que puede valer -1, si nadie ha ganado; o un número
    # que indica la posición del jugador que ha ganado en caso de que alguno lo
    # haya logrado.
    return jugador
# ------------------------------------------------------------------------------

# Declaracion de objetos e inicializacion de variables:
f = 5
c = 5
#listaMinerales = ["D","O","P","N","C"]
dicMinerales = {"D":5,"O":3,"P":2,"N":0,"C":-3}

# Lógica del juego:

# Creación de las matrices:
print("Celia")
print("Creamos la matriz:")
matrizCompleta = crearMatriz(f,c)
matrizJuego =crearMatriz(f,c)
rellenarMatriz(matrizCompleta,f,c,dicMinerales)
imprimirMatriz(matrizCompleta,f,c)

# ¿Quién empieza?

puntuacion1 = 0
puntuacion2 = 0
turno = 0
listaMoneda = ["CARA","CRUZ"]

jugador1 = input("¿Cómo se llama el jugador 1? ")
jugador2 = input("¿Cómo se llama el jugador 2? ")
# Lo ideal es formar un diccionario jugador:puntuacion, pero vamos a repasar la
# gestion de listas...
listaJugadores = [jugador1,jugador2]
listaPuntuaciones = [puntuacion1,puntuacion2]                           # [0,0]
monedaElegida = input(jugador1 + ": ¿CARA o CRUZ? ")
monedaRandom = random.choice(listaMoneda)

if monedaElegida != monedaRandom:
    turno = 1

print(jugador1 + " ha elegido " + monedaElegida)
print("Aleatoriamente ha salido " + monedaRandom)


# A picar
print()
print("¡¡¡EMPIEZA EL JUEGO!!!")
fin = -1

while (fin == -1):
    imprimirMatriz(matrizJuego,f,c)
    print("Le toca jugar a " + listaJugadores[turno])
    fila = int(input("Elige la fila: "))
    columna = int(input("Elige la columna: "))
    mineralExtraido = matrizCompleta[fila][columna]
    matrizJuego[fila][columna] = mineralExtraido
    listaPuntuaciones[turno] += dicMinerales[mineralExtraido]
    print("El jugador " + listaJugadores[turno] + " ha picado " + mineralExtraido +
    " que vale " + str(dicMinerales[mineralExtraido]) + " puntos... Tiene en total " +
    str(listaPuntuaciones[turno]) + " puntos.")
    fin = haGanado(listaPuntuaciones)
    turno = siguienteTurno(turno)

print ("El jugador " + listaJugadores[fin] + " ha ganado.")
