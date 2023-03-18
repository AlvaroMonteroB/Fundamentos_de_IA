#import ctypes         #g++ -fPIC -shared -o Data_read.so data_read.cpp
#Open_file = ctypes.CDLL("D:/Repositorios/Fundamentos_de_IA/P1/Data_read.so")#matrix read in c++ with headers                                                         #to calculate the size
Matrix_rows=list()
Matrix_rows1=list()
with open("D:\Repositorios\Fundamentos_de_IA\P1\matriz.txt","r") as Read_matrix:
    leer=Read_matrix.readline
    for line in Read_matrix:
        Matrix_rows.append(line)
    Read_matrix.close
                                    #Lectura y remplazo de comas en el archiv
print("Read successfully")
for linea in Matrix_rows:
    aux=linea.replace(',','')
    aux.strip()
    Matrix_rows1.append(aux)#Arreglo de renglones sin comas y sin saltos de linea

for line in Matrix_rows1:
    print(line)

Coo1=input("Ingrese coordenada de inicio\n")
Coo2=input("Ingrese coordenada de fin\n")
