import threading
import display_graphics
import Read_data


C_ini,C_fin=list()
Matrix=Read_data.read_matrix()#arreglo de puntos AKA objetos
Coo1=input("Ingrese coordenada de inicio\n")
Coo2=input("Ingrese coordenada de fin\n")
Coo1.replace(',','')
Coo2.replace(',','')
C_ini.append(int(Coo1[0]))
C_ini.append(int(Coo1[1]))
C_fin.append(int(Coo2[0]))
C_fin.append(int(Coo2[1]))






