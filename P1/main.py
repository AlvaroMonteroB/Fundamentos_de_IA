#==================================INGENIERIA EN INTELIGENCIA ARTIFICIAL=========================================
#MONTERO BARRAZA ÁLVARO DAVID
#MANZANERO GONZÁLES THELMA REBECA
#PONCE AGUIRRE YAHIR ALEJANDRO
#MIGUEL MARTÍNEZ ÁNGEL GABRIEL

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
import Busq_Anch as b_a
import copy
import arboli
import edit_map
import tree_to_list as ttl
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
        cost+=Criaturas.switch[Agente.charact](layer.Valor)
    return cost
#Costo de recorrer todo el arbol
def calc_tree_cost(Agente, Raiz: b_p.Nodo):
    if Raiz is None:
        return 0
    cost = Criaturas.switch[Agente.charact](Raiz.point.Valor)
    for hijo in Raiz.children:
        cost += calc_tree_cost(Agente, hijo)
    return cost
def player_cost(Matrix:Read_data.Coord,Agente,ini:Read_data.Coord):
    cost=0
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            if Matrix[j][i].visited_flag:
                cost+=Criaturas.switch[Agente.charact](Matrix[j][i].Valor)
    cost=cost-Criaturas.switch[Agente.charact](ini.Valor)
    
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
    AgentA=Agentes.switch[3](point_ini,'1',Matrix,False)  
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
def testAE(Matrix:Read_data.Coord,xi,yi,xf,yf,charact):
    Matrix1=copy.deepcopy(Matrix)
    print("Prueba con A*")
    point_ini=various_methods.assign_point(Matrix,xi,yi,Matrix[yi][xi])
    AgentA=Agentes.Agente3(point_ini,charact,Matrix,False)
    raiz=b_p.Nodo(AgentA.position,None)
    fin=various_methods.busq_point(Matrix,xf,yf)
    fin.visited_flag=False
    output=A_estrella.alg_busq1(raiz,Matrix,AgentA,fin)
    stack=copy.deepcopy(output)
    print_tree_console.tree_to_file(raiz)
    ifz.recorrido(Matrix1, fin, point_ini, output, None)
    arboli.show_tree()
    cos=calc_cost(stack,AgentA)
    print("El costo por A* es: "+ str(cos))

#================================================================================================
#==========================================test_Anch=============================================
#================================================================================================
def testAnch(Matrix:Read_data.Coord,xi,yi,xf,yf):
    print("Prueba por anchura")
    point_ini=various_methods.assign_point(Matrix,xi,yi,Matrix[yi][xi])
    AgentA=Agentes.Agente3(point_ini,'1',Matrix,False)
    raiz=b_p.Nodo(AgentA.position,None)
    fin=various_methods.busq_point(Matrix,xf,yf)
    fin.visited_flag=False
    ifz.recorrido_anchura(Matrix, fin, point_ini,AgentA)
    arboli.show_tree()




def print_stack(stack):
    i=0
    p=-1
    print("Agente terminado")
    while i<len(stack):
        print(str(stack[p].Xcoordinate)+","+str(stack[p].Ycoordinate)+"\n")
        p-=1
        i+=1
#==================================================================================================
#==================================Aqui empieza====================================================
#==================================================================================================    
edit_map.edit()    
Read_data.read_matrix(Matrix)#arreglo de puntos AKA objetos
Matrix1=copy.deepcopy(Matrix)#Separamos la matriz en 2 variables, dejando la original para despues
Matrix2=copy.deepcopy(Matrix)
Matrix3=copy.deepcopy(Matrix)#Esta es para la busqueda por anchura
Matrix4=copy.deepcopy(Matrix)#Esta es para A*
Matrix5=copy.deepcopy(Matrix)
  
select,X,Y,finx,finy,pers=ifz.select_Ag()#Seleccion del agente
#Switch para seleccionar agentes

#Matrix1->Jugador
#Matrix2->Agente
"""
fpoint_a=various_methods.busq_point(Matrix2,finx,finy)
if 0<select<3:#Como los primeros 2 tienen un atributo de direccion, lo separamos
    point_ini=various_methods.assign_point(Matrix1,X,Y,Matrix1[X][Y])#Asignar el punto en la matriz del jugador
    Agentejugador=Agentes.switch_dir[select](1,point_ini,pers,Matrix1,False)
    point_iniP=various_methods.assign_point(Matrix2,X,Y,Matrix2[X][Y])
    AgentePC=Agentes.switch_dir[select](1,point_iniP,pers,Matrix2,True)
elif 6>select>2:
    point_ini=various_methods.assign_point(Matrix1,X,Y,Matrix1[X][Y])
    Agentejugador=Agentes.switch[select](point_ini,pers,Matrix1,False)
    AgentePC=Agentes.switch[select](point_ini,pers,Matrix2,True)
raiz=b_p.Nodo(point_ini,None)
solution=b_p.switch[select](raiz,AgentePC,Matrix2,fpoint_a)#Busquedas
"""
#ifz.selec_agent_interface[select](Matrix1,True,fpoint_a,point_ini,Agentejugador)#Para desplegar botones dependiendo nuestro agente
"""costo_jugador=player_cost(Matrix1,Agentejugador,point_ini)
costo_pc=calc_cost(solution.stack,AgentePC)"""
#===========Vamos a mostrar que hizo el agente  
testAE(Matrix4,X,Y,finx,finy,pers)

"""ifz.recorrido(Matrix3, fpoint_a, point_ini,solution.stack,raiz)#Solucion paso por paso
print("El algoritmo hizo el camino con un costo de "+str(costo_pc))
print("Mientras tu hiciste un costo de "+str(costo_jugador))
print_tree_console.tree_to_file(raiz)
arboli.show_tree()"""




#Empieza el bucle de la interfaz grafica
#while enter_game:
    
    
    
    
    
    
    



