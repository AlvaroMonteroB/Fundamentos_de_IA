import threading
import display_graphics
import Read_data
import Criaturas
import various_methods
import Busq_prof as b_p
import Agentes
C_aux:str=list()
C_ini=list()
C_fin=list()
Matrix=list()
Read_data.read_matrix(Matrix)#arreglo de puntos AKA objetos
Coo1=input("Ingrese coordenada de inicio\n")
Coo2=input("Ingrese coordenada de fin\n")
aux=''
for letra in Coo1:
    if not letra==',' :#Si no es ',' pasa al siguiente paso
        C_aux.append(letra)
    for val in C_aux:
        aux=aux+val
    C_ini.append(int(aux))
    C_aux.clear()
aux=''
for letra in Coo2:
    if not letra==',':
        C_aux.append(letra)
    for val in C_aux:
        aux=aux+val
    C_fin.append(int(aux))
    C_aux.clear()
aux=''
#Puntos con sus respectivas coordenadas

various_methods.busq_point(Matrix, C_ini[0], C_ini[1])
entity=Criaturas.character()
pepito=input("Choose a name\n")
opt=input("Choose a character:\n1.-Human\n2.-Monkey\n3.-Octopus\n4.-Sasquatch\n")
if opt=='1':
    entity=Criaturas.character.Humano(pepito)
elif opt=='2':
    entity=Criaturas.character.Monkey(pepito)
elif opt=='3':
    entity=Criaturas.character.Octopus(pepito)
elif opt=='4':
    entity=Criaturas.character.Sasquatch(pepito)
else:
    print("Put a valid option\n")
    
user=input("Do you ant to play against the machine?  y/n\n")
if user=='y':
    userband=False #not the user
else:
     userband=True

opt=input("Choose an Agent:\n1\n2\n3\n4\n5\n")
if opt=='1':
    if userband:
        agent=Agentes.agente1(1,C_ini,entity,Matrix,userband)#true=PC, false=User
        agentA=Agentes.agente1(1,C_ini,entity,Matrix,True)
    else:
        agentA=Agentes.agente1(1,C_ini,entity,Matrix,True)
elif opt=='2':
    if userband:
        agent=Agentes.Agente2(1,C_ini,entity,Matrix,userband)#true=PC, false=User
        agentA=Agentes.Agente2(1,C_ini,entity,Matrix,True)
    else:
        agentA=Agentes.Agente2(1,C_ini,entity,Matrix,True)
elif opt=='3':
    agent=Agentes.Agente3()

Raiz=list()#Iniciando la raiz
if userband: #true if user doesnt do anything
    Raiz.append(agentA.position)#aqui se añade el elemento a la raiz
else:
    Raiz.append(agent.position)
    Raiz2=list()
    Raiz2.append(agentA.position)
    
    



enter_game=True


#Empieza el bucle de la interfaz grafica
#while enter_game:
    