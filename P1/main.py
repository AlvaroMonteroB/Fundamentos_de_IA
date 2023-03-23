import threading
import display_graphics
import Read_data
import Criaturas
import various_methods
import Agentes
C_aux:str=list()
C_ini=list()
C_fin=list()
Matrix=list()
Read_data.read_matrix(Matrix)#arreglo de puntos AKA objetos
Coo1=input("Ingrese coordenada de inicio\n")
Coo2=input("Ingrese coordenada de fin\n")
for letra in Coo1:
    if not letra==',' :
        C_aux.append(letra)
    C_ini.append(C_aux.data())
    C_aux.clear()
for letra in Coo2:
    if not letra==',':
        C_aux.append(letra)
    C_fin.append(C_aux.data())
    C_aux.clear()
#Puntos con sus respectivas coordenadas

various_methods.busq_point(Matrix, C_ini[0], C_ini[1])
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
    
user=input("Do you ant to play against the machine?  y/n")
if user=='y':
    userband=False
else:
     userband=True

opt=input("Choose an Agent:\n1\n2\n3\n4\n5\n")
if opt==1:
    agent=Agentes.agente1(1,C_ini,entity,Matrix,userband)#true=PC, false=User
    if not userband:
        agentA=Agentes.agente1(1,C_ini,entity,Matrix,True)
    
elif opt==2:
    agent=Agentes.Agente2(1, C_ini, entity, Matrix, userband)
elif opt==3:
    agent=Agentes.Agente3()

enter_game=True


#Empieza el bucle de la interfaz grafica
#while enter_game:
    