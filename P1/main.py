import threading
import display_graphics
import Read_data


C_ini=list()
C_fin=list()
Obj_comp=Read_data.read_matrix()#arreglo de puntos AKA objetos
Matrix=Obj_comp.matriz()
puntos=Obj_comp.arreglo()
Coo1=input("Ingrese coordenada de inicio\n")
Coo2=input("Ingrese coordenada de fin\n")
Coo1.replace(',','')
Coo2.replace(',','')
C_ini.append(int(Coo1[0]))
C_ini.append(int(Coo1[1]))
C_fin.append(int(Coo2[0]))
C_fin.append(int(Coo2[1]))#Puntos con sus respectivas coordenadas




def access_obj(cols,rows,Mat_obj):
    line=Mat_obj[rows-1]
    return line[cols-1]

