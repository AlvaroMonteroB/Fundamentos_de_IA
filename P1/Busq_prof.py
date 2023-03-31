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
    def __init__(self,point:r_d.Coord,padre):
        self.point=point
        self.hijo=[]
        self.padre=padre
    def C_nodo_h(self,clave_hijo,padre):
        self.hijo.append(Nodo(clave_hijo,padre))
    def howm_son(self):#Para saber cuantos hijos tiene el nodo
        return len(self.hijo)
    
def rec_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:list[r_d.Coord],cost:int)->bool:
    new_scan=list()
    valid_scan=list()
    print(str(Agente.direction))
    mov=Agente.move_forward(cost,1)
    if not mov:
        print("No se mueve")
        return False
    output.append(Agente.position)
    if Agente.position==fin_pos:
        return True
    print('\n'+str(output[-1].Xcoordinate)+','+str(output[-1].Ycoordinate))
    counter=0
    for dirs in range(4):
        print("Esto 4 veces pero es del rec")
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid:
            counter+=1
    print(str(counter)+" Valid directions")
    if counter<1:
        print("Breakpoint0")
        return False
    elif counter>1:
        Agente.position.deci_flag=True

    for dirs in range(4):#analizamos en las 4 direcciones para generar los nuevos nodos
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid and not aux.point.visited_flag:
            dir=Agente.direction
            raiz.C_nodo_h(aux.point,raiz)
            n_raiz=raiz.hijo[-1]
            result=rec_busq1(n_raiz, Agente, Matrix, fin_pos, output, cost)
            if result:
                return True
            Agente.direction=dir
            output.pop()
            Agente.position=V_M.assign_point(Matrix,raiz.point.Xcoordinate,raiz.point.Ycoordinate,raiz.point)
            
    return False
      
    
def alg_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord)->resultado:#inicializacion del algoritmo  
    stack=[]
    output=resultado(stack, 0)
    print("Scanning dirs")
    counter=0
    for dirs in range(4):
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid and not aux.point.visited_flag:
            counter+=1
    for dirs in range(4):
        Agente.turn_left()
        print("Posicion "+str(Agente.position.Xcoordinate)+','+str(Agente.position.Ycoordinate)+"  Direccion"+str(Agente.direction)+str())
        dir=Agente.direction
        aux=Agente.scan_forward(True)
        print(aux.point.Valor)
        if aux.valid and not aux.point.visited_flag:
            print("Valid scan")
            raiz.C_nodo_h(aux.point,raiz)#Por cada escaneo valido creamos un nuevo nodo
            n_raiz=raiz.hijo[-1]#Guardamos como nueva raiz el nodo[N] de la lista de hijos
            result=rec_busq1(n_raiz,Agente,Matrix,fin_pos,output.stack,output.cost)#si es verdadero vamos a tener el stack lleno       
            if result:
                return output
            else:
                Agente.direction=dir
                Agente.position=V_M.assign_point(Matrix,raiz.point.Xcoordinate,raiz.point.Ycoordinate,raiz.point)
                if Agente.position.Xcoordinate==raiz.point.Xcoordinate and Agente.direction==dir:
                    print("Si volvio a casa")
        
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