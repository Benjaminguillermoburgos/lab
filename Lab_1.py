import  random
#Metodos
def matriz_random(filas,columnas):
    m=[]
    for i in range(filas):
        filas=[]
        for j in range(columnas):
            elemento=random.randint(1,5)
            filas.append(elemento)
            m.append(filas)
    return m