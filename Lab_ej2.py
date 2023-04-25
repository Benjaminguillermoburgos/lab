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
#Resta
def resta_matriz(m1,m2):
    matriz_final=[]
    for i in range(len(m1)):
        filas=[]
        for j in range(len(m1[0])):
            resta=m1[i][j]-m2[i][j]
            filas.append(resta)
        matriz_final.append(filas)
    return matriz_final
#Suma
def suma_matriz(m1,m2):
    matriz_final=[]
    for i in range(len(m1)):
        filas=[]
        for j in range(len(m1[0])):
            suma=m1[i][j]+m2[i][j]
            filas.append(suma)
        matriz_final.append(filas)
    return matriz_final
#Creador
filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas: "))
print("Creando la primera matriz")
m1=()
m2=()

#Resta
matriz_final=resta_matriz(m1,m2)
print("La resta de las matrices da como resultado la sig.matriz: ")
print(filas,"/n")

#Suma
matriz_final=suma_matriz(m1,m2)
print("La suma de las matrices da como resultado la sig.matriz: ")
print(filas,"/n")
