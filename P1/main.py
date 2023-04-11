import threading
import multiprocessing
import Read_data
import Criaturas
import various_methods
import Busq_prof as b_p
import Agentes
import interfaz as ifz
import print_tree_console
import A_estrella
import Busq_Anch
b_p.sys.setrecursionlimit(8000)
C_aux:str=list()
C_ini=list()
C_fin=list()
Matrix=list()

def calc_cost(stack,Agente)->int:
    cost=0
    for layer in stack:
        cost=cost+Criaturas.switch[Agente.charact](layer.Valor)
    return cost

#================================================================================================
#==========================================test_01===============================================
#================================================================================================

def test(Matrix:Read_data.Coord):
    print("Prueba con agente 1")
    point_ini=various_methods.assign_point(Matrix,1,1,Matrix[0][0])
    agentA=Agentes.agente1(1,point_ini,'1',Matrix,True)
    raiz=b_p.Nodo(point_ini,None)
    fin=various_methods.busq_point(Matrix,7,14)
    fin.visited_flag=False
    output=b_p.alg_busq1(raiz,agentA,Matrix,fin)
    print_stack(output.stack)
    c=calc_cost(output.stack,agentA)
    print("El costo es "+str(c))
    #ifz.mapaR(Matrix,True,fin,point_ini)
    print_tree_console.print_tree(raiz)
    #print_tree_console.print_tre_pre(raiz)
#================================================================================================
#==========================================test_02===============================================
#================================================================================================
    
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
        print_tree_console.print_tree(raiz)
    else:
        print("No se encontro el punto")
        
#================================================================================================
#==========================================test_03===============================================
#================================================================================================        
def test3(Matrix:Read_data.Coord):
    print("Prueba con agente 3")
    point_ini=various_methods.assign_point(Matrix,1,1,Matrix[0][0])
    AgentA=Agentes.Agente3(point_ini,'1',Matrix,False)
    raiz=b_p.Nodo(AgentA.position,None)
    fin=various_methods.busq_point(Matrix,7,14)
    fin.visited_flag=False
    output=b_p.alg_busq3(raiz,AgentA,Matrix,fin)
    if output.stack:
        print_stack(output.stack)
        c=calc_cost(output.stack, AgentA)
        print("El costo es "+str(c))
        print_tree_console.print_tree(raiz)
        print_tree_console.tree_to_file(raiz)

    else:
        print("No se encontro el punto")

#================================================================================================
#==========================================test_04===============================================
#================================================================================================
def test4(Matrix:Read_data.Coord):
    print("Prueba con agente 4")
    point_ini=various_methods.assign_point(Matrix,1,1,Matrix[0][0])
    AgentA=Agentes.Agente4(point_ini,'1',Matrix,False)
    raiz=b_p.Nodo(AgentA.position,None)
    fin=various_methods.busq_point(Matrix,7,14)
    fin.visited_flag=False
    output=b_p.alg_busq4(raiz,AgentA,Matrix,fin)
    if output.stack:
        print_stack(output.stack)
        c=calc_cost(output.stack, AgentA)
        print("El costo es "+str(c))
        print_tree_console.print_tree(raiz)

    else:
        print("No se encontro el punto")


#================================================================================================
#==========================================test_05===============================================
#================================================================================================
def test5(Matrix:Read_data.Coord):
    print("Prueba con agente 5")
    point_ini=various_methods.assign_point(Matrix,1,1,Matrix[0][0])
    AgentA=Agentes.Agente5(point_ini,'1',Matrix,False)
    raiz=b_p.Nodo(AgentA.position,None)
    fin=various_methods.busq_point(Matrix,7,14)
    fin.visited_flag=False
    output=b_p.alg_busq5(raiz,AgentA,Matrix,fin)
    if output.stack:
        print_stack(output.stack)
        c=calc_cost(output.stack, AgentA)
        print("El costo es "+str(c))
        print_tree_console.print_tree(raiz)

    else:
        print("No se encontro el punto")


#================================================================================================
#==========================================test_A*===============================================
#================================================================================================
def testAE(Matrix:Read_data.Coord):
    print("Prueba con A*")
    point_ini=various_methods.assign_point(Matrix,1,1,Matrix[0][0])
    AgentA=Agentes.Agente3(point_ini,'1',Matrix,False)
    raiz=b_p.Nodo(AgentA.position,None)
    fin=various_methods.busq_point(Matrix,7,14)
    fin.visited_flag=False
    output=A_estrella.Init_busq(raiz,AgentA,Matrix,fin)
    if output.stack:
        print_stack(output.stack)
        c=calc_cost(output.stack, AgentA)
        print("El costo es "+str(c))
        
        print_tree_console.print_tree(raiz)

    else:
        print("No se encontro el punto")
    ifz.interfaz(Matrix,False,fin,point_ini)

#================================================================================================
#==========================================test_Anch=============================================
#================================================================================================
def testAnch(Matrix:Read_data.Coord):
    print("Prueba por anchura")
    point_ini=various_methods.assign_point(Matrix,1,1,Matrix[0][0])
    AgentA=Agentes.Agente3(point_ini,'1',Matrix,False)
    raiz=b_p.Nodo(AgentA.position,None)
    fin=various_methods.busq_point(Matrix,7,14)
    fin.visited_flag=False
    output=Busq_Anch.alg_busq1(raiz,Matrix,AgentA,fin)
    if output:
        print_stack(output)
        c=calc_cost(output, AgentA)
        print("El costo es "+str(c))
        print_tree_console.print_tree(raiz)

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
        
#Aqui empieza
        
Read_data.read_matrix(Matrix)#arreglo de puntos AKA objetos
matrix_agent=list()
for ent in range(5):#Mapa para cada agente
    matrix_agent.append(Matrix)
test3(matrix_agent[0])
exit()
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
#Ejecutamos aqui los 5 agentes a la vez
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
    
    
    
    
    
    
    
