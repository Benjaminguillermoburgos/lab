import  random
#Metodos

filas=int(input("Ingrese Cantidad de filas: "))
columnas=int(input("Ingrese columnas"))

def crear(filas, columnas, elemento=None):
    m = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if elemento is None:
                elemento=random.randint(1,5)
            elemento = (hash(f"{i},{j},{elemento}") % 5+1)
            fila.append(elemento)
        m.append(fila)
    return m 
#Suma

def suma(m,m2):
    mf = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            suma = m[i][j] + m2[i][j]
            fila.append(suma)
        mf.append(fila)
    return mf
#Resta

def resta(m,m2):
    mf = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            resta = m[i][j] - m2[i][j]
            fila.append(resta)
        mf.append(fila)
    return mf

#Resultado

m = crear(filas,columnas, "1")
print(f"\nMatriz 1:")
for fila in m:
    print(fila)

m2 = crear(filas,columnas, "2")
print(f"\nMatriz 2:")
for fila in m2:
    print(fila)

mfinal = suma(m, m2)
print(f"\nSuma matrices (1+2): ")
for fila in mfinal:
    print(mfinal)

m3 = crear(filas,columnas, "3")
print(f"\nMatriz 3:")
for fila in m3:
    print(mfinal)

mfinal = resta(mfinal, m3)
print(f"\nResta matrices (1+2-3): ")
for fila in mfinal:
    print(mfinal)