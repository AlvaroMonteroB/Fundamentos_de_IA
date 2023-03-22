import threading
import display_graphics
import Read_data
import Criaturas
import Agentes

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


entity=Criaturas.character()
opt=input("Choose a character:\n1.-Human\n2.-Monkey\n3.-Octopus\n4.-Sasquatch\n")
pepito=input("Choose a name")
if opt==1:
    entity=Criaturas.character.Humano(pepito)
elif opt==2:
    entity=Criaturas.character.Monkey(pepito)
elif opt==3:
    entity=Criaturas.character.Octopus(pepito)
elif opt==4:
    entity=Criaturas.character.Sasquatch(pepito)
else:
    print("Put a valid option")
    
    
opt=input("Choose an Agent:\n\n2\n3\n4\n5\n")
if opt==1:
    agent=Agentes.agente1(1,C_ini,entity)