import Agentes as Ag
import various_methods as V_M
import Read_data as r_d
import acciones as acc
import sys

sys.setrecursionlimit(8000)

class resultado:
    def __init__(self,stack,cost):
        self.stack=stack
        self.cost=cost

class Nodo:
    def __init__(self,point:r_d.Coord):
        self.point=point
        self.hijo=[]
    def C_nodo_h(self,clave):
        self.hijo.append(Nodo(clave))
    def howm_son(self):#Para saber cuantos hijos tiene el nodo
        return len(self.hijo)
    
def rec_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:list[r_d.Coord],cost:int)->bool:
    new_scan=list()
    valid_scan=list()
    ini=Agente.position
    mov=Agente.move_forward(cost,1)
    fin=Agente.position
    counter=0
    for dirs in range(4):
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid:
            counter+=1
    if counter<1:
        return False
    elif counter>1:
        Agente.position.deci_flag=True

    for dirs in range(4):#analizamos en las 4 direcciones para generar los nuevos nodos
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid:
            raiz.C_nodo_h(aux.point)
            n_raiz=raiz.hijo[-1]
            result=rec_busq1(n_raiz, Agente, Matrix, fin_pos, output, cost)
            if result:
                return True
            output.pop()
    return False
      
    
def alg_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord)->resultado:#inicializacion del algoritmo  
    stack=[]
    output=resultado(stack, 0)
    print("Scanning dirs")
    for dirs in range(4):
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid:
            raiz.C_nodo_h(aux.point)#Por cada escaneo valido creamos un nuevo nodo
            n_raiz=raiz.hijo[-1]#Guardamos como nueva raiz el nodo[N] de la lista de hijos
            result=rec_busq1(n_raiz,Agente,Matrix,fin_pos,output.stack,output.cost)#si es verdadero vamos a tener el stack lleno              
            if result:
                return output
    else:
        return resultado(None,0)
#==================================================================================================================================
#==========================================Algoritmo para el segundo agente=================================================
#==================================================================================================================================
def rec_busq2():
    new_scan=list()        
        
 
 
def alg_busq2(raiz:Nodo,Agente:Ag.Agente2)->r_d.Coord:
    stack=list()
 
        


def stack_pop(stack:list[r_d.Coord]):
    for node in stack_pop:
        if not node.point.deci_flag:
            stack.pop
        else:
            return    

#==================================================================================================================================
#==========================================Algoritmo para el tercer agente=================================================
#==================================================================================================================================
def rec_busq3():
    new_scan=list()


def alg_busq3():
    scan=list()












switch={#switch for the algorithms
    1:alg_busq1,
    2:alg_busq2,
    3:alg_busq3
}




def comprobacion(partida:r_d.Coord,llegada:r_d.Coord)->bool:
    if partida.Xcoordinate==llegada.Xcoordinate and partida.Ycoordinate==llegada.Ycoordinate:
        return False#Falso si son el mismo punto, no se movio
    return True #true se movio