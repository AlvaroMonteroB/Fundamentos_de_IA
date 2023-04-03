import threading
import multiprocessing
import display_graphics
import Read_data
import Criaturas
import various_methods
import Busq_prof as b_p
import Agentes
b_p.sys.setrecursionlimit(8000)
C_aux:str=list()
C_ini=list()
C_fin=list()
Matrix=list()
def test(Matrix:Read_data.Coord):
    point_ini=various_methods.assign_point(Matrix,1,1,Matrix[0][0])
    agentA=Agentes.agente1(1,point_ini,'1',Matrix,True)
    print('"'+agentA.position.Valor+'"'+'('+str(agentA.position.Xcoordinate)+','+str(agentA.position.Ycoordinate)+')')
    raiz=b_p.Nodo(point_ini,None)
    fin=various_methods.busq_point(Matrix,7,14)
    fin.visited_flag=False
    output=b_p.alg_busq1(raiz,agentA,Matrix,fin)
    print_stack(output.stack)
    
def test2(Matrix:Read_data.Coord):
    print("Prueba con agente 2")
    point_ini=various_methods.assign_point(Matrix,1,1,Matrix[0][0])
    agentA=Agentes.Agente2(1,point_ini,'1',Matrix,True)
    print('"'+agentA.position.Valor+'"'+'('+str(agentA.position.Xcoordinate)+','+str(agentA.position.Ycoordinate)+')')
    raiz=b_p.Nodo(point_ini,None)
    fin=various_methods.busq_point(Matrix,7,14)
    fin.visited_flag=False
    output=b_p.alg_busq2(raiz,agentA,Matrix,fin)
    if output.stack:
        print_stack(output.stack)
    else:
        print("No se encontro el punto")

def print_stack(stack):
    i=0
    p=-1
    print("Agente terminado")
    while i<len(stack):
        print(str(stack[p].Xcoordinate)+","+str(stack[p].Ycoordinate)+"\n")
        p-=1
        i+=1
        
        
        
Read_data.read_matrix(Matrix)#arreglo de puntos AKA objetos
matrix_agent=list()
for ent in range(5):#Mapa para cada agente
    matrix_agent.append(Matrix)
test(matrix_agent[0])
Coo1=input("Ingrese coordenada de inicio\n")
Coo2=input("Ingrese coordenada de fin\n")
aux=''
for letra in Coo1:
    if not letra==',' :#Si no es ',' pasa al siguiente paso
        C_aux.append(letra)
    for val in C_aux:
        aux=aux+val#Construimos el string atraves de los char en la lista
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
pepito=input("Choose a name\n")
opt=input("Choose a character:\n1.-Human\n2.-Sasquatch\n3.-Monkey\n4.-Octopus\n")
user=input("Do you ant to play against the machine?  y/n\n")
if user=='y':
    userband=False #not the user
else:
     userband=True
    
X=C_ini[0]
Y=C_ini[1]
point_ini=various_methods.assign_point(Matrix, X, Y)
opt=input("Choose an Agent:\n1\n2\n3\n4\n5\n")#Menu para escoger el agente a usar
if opt=='1':
    if userband:
        agent=Agentes.agente1(1,point_ini,opt,Matrix,userband)#true=PC, false=User
        agentA=Agentes.agente1(1,point_ini,opt,Matrix,True)
    else:
        agentA=Agentes.agente1(1,point_ini,opt,Matrix,True)
elif opt=='2':
    if userband:
        agent=Agentes.Agente2(1,point_ini,opt,Matrix,userband)#true=PC, false=User
        agentA=Agentes.Agente2(1,point_ini,opt,Matrix,True)
    else:
        agentA=Agentes.Agente2(1,point_ini,opt,Matrix,True)
elif opt=='3':
    if userband:
        agent=Agentes.Agente3(point_ini,opt,Matrix,True)
        agentA=Agentes.Agente3(point_ini,opt,Matrix,True)
    else:
        agentA=Agentes.Agente3(point_ini,opt,Matrix,True)
elif opt==4:
    if userband:
        agent=Agentes.Agente4(point_ini,opt,Matrix,True)
    else:
        agentA=Agentes.Agente4(point_ini,opt,Matrix,True)

finx=C_fin[0]
finy=C_fin[1]
fpoint=various_methods.busq_point(Matrix,finx,finy)
Raiz=b_p.Nodo(agentA.position)#Iniciando la raiz
if userband: #true if user doesnt do anything
    Raiz.append(agentA.position)#aqui se añade el elemento a la raiz
else:
    Raiz.append(agent.position)
    Raiz2=list()
    Raiz2.append(agentA.position)
#AgentA es el algoritmo de busqueda
stack=b_p.switch[opt](Raiz,agentA,Matrix,fpoint)



enter_game=True


#Empieza el bucle de la interfaz grafica
#while enter_game:
    
    
    
    
    
    
    
