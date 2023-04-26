print("Creación de una matriz")
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

def crear(filas, columnas, elementos=None):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if elementos is None:
                elementos = "standard"
            elef = (hash(f"{i},{j},{elementos}") % 11)
            fila.append(elef)
        m.append(fila)
    return m

def multiplicacion(m,n):
    mf = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            mult = m[i][j] * n
            fila.append(mult)
        mf.append(fila)
    return mf

m = crear(filas,columnas, "algo1")
print(f"\nMatriz:")
for fila in m:
    print(fila)

n = int(input("\nIngrese un escalar con el cual multiplicar la matriz: "))

mfinal = multiplicacion(m, n)
print(f'\nMultiplicación de matriz por el escalar "{n}": ')
for fila in mfinal:
    print(fila)