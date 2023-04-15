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
#================================================================================================
#=============================Funciones para calcular el costo===================================
#================================================================================================
#Costo de la solucion
def calc_cost(stack,Agente)->int:
    cost=0
    for layer in stack:
        cost=cost+Criaturas.switch[Agente.charact](layer.Valor)
    return cost
#Costo de recorrer todo el arbol
def calc_tree_cost(Agente, Raiz: b_p.Nodo):
    if Raiz is None:
        return 0
    cost = Criaturas.switch[Agente.charact](Raiz.point.Valor)
    for hijo in Raiz.children:
        cost += calc_tree_cost(Agente, hijo)
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
    if not output.stack:
        exit()
    print_stack(output.stack)
    c=calc_cost(output.stack,agentA)
    print("El costo es "+str(c))
    print_tree_console.print_tree(raiz)
    costo=calc_tree_cost(agentA,raiz)
    print("El costo del arbol es "+str(costo))
    
    ifz.mapaR(Matrix,True,fin,point_ini,output.stack)
    #print_tree_console.tree_to_file(raiz)
    
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
        ifz.mapaR(Matrix,False,fin,point_ini,output.stack)

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
        ifz.mapaR(Matrix,False,fin,point_ini,output.stack)

    else:
        print("No se encontro el punto")


#================================================================================================
#==========================================test_A*===============================================
#================================================================================================
def testAE(Matrix:Read_data.Coord):
    print("Prueba con A*")
    point_ini=various_methods.assign_point(Matrix,1,1,Matrix[0][0])
    AgentA=Agentes.Agente3(point_ini,'4',Matrix,False)
    raiz=b_p.Nodo(AgentA.position,None)
    fin=various_methods.busq_point(Matrix,7,14)
    fin.visited_flag=False
    output=A_estrella.Init_busq(raiz,AgentA,Matrix,fin)
    if output.stack:
        print_stack(output.stack)
        c=calc_cost(output.stack, AgentA)
        print("El costo es "+str(c))
        
        
    else:
        print("No se encontro el punto")
    print_tree_console.print_tree(raiz)
    ifz.mapaR(Matrix,False,fin,point_ini,output.stack)
    

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
        #print_tree_console.print_tree(raiz)
        ifz.mapaR(Matrix,False,fin,point_ini,output)

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
select=ifz.select_Ag()#Seleccion del agente

#Aqui debe haber para seleccionar personaje
pers=input("Selecciona personaje, 1 2 3 4\n")
optn=True
#Puntos con sus respectivas coordenadas
print("Coordenadas del primer punto")
while optn:
    X=input("X=")
    Y=input("Y=")
    point_ini=various_methods.busq_point(Matrix,X,Y)
    if point_ini.Valor=='-1':
        print("Introduce un valor valido")
        continue
    elif Criaturas.switch[pers](point_ini.Valor)!=0:#Significa que la posicion es valida para el personaje
        point_ini=various_methods.assign_point(Matrix,X,Y,Matrix[X][Y])
        optn=False
    else:
        print("Posicion no valida para el personaje")
    
print("Coordenadas del segundo punto")
while optn:
    finx=C_fin[0]
    finy=C_fin[1]
    fpoint=various_methods.busq_point(Matrix,finx,finy)
    if fpoint.Valor=='-1':
        print("Introduce un punto valido")
        continue
    elif Criaturas.switch[pers](point_ini.Valor)!=0:#Significa que la posicion es valida para el personaje
        optn=False
    
point_ini=various_methods.assign_point(Matrix, X, Y)

#Switch para seleccionar agentes
if 0<select<3:
    Agentejugador=Agentes.switch_dir[select](1,point_ini,pers,Matrix[0],False)
    AgentePC=Agentes.switch_dir[select](1,point_ini,pers,Matrix[1],True)
elif 6>select>2:
    Agentejugador=Agentes.switch(point_ini,pers,Matrix[0],False)
    AgentePC=Agentes.switch(point_ini,pers,Matrix[1],True)
raiz=b_p.Nodo(point_ini,None)
b_p.switch[select](raiz,AgentePC,Matrix[1],fpoint)
ifz.selec_agent_interface[select](Matrix[0],True,fpoint,point_ini)


enter_game=True


#Empieza el bucle de la interfaz grafica
#while enter_game:
    
    
    
    
    
    
    
