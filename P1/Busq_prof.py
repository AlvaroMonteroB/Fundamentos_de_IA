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
    mov=Agente.move_forward(cost,1)
    if not mov:
        print("No se mueve")
        return False
    output.append(Agente.position)
    if Agente.position==fin_pos:
        print("Enhorabuena, encontraste la salida")
        return True
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
            Agente.position=V_M.assign_point(Matrix,output[-1].Xcoordinate,output[-1].Ycoordinate,raiz.point)
        Agente.turn_left()
    return False
      
    
def alg_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord)->resultado:#inicializacion del algoritmo  
    stack=[]
    stack.append(Agente.position)
    cost=0
    print("Scanning dirs")
    counter=0
    for dirs in range(4):
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid and not aux.point.visited_flag:
            counter+=1
    for dirs in range(4):
        dir=Agente.direction
        aux=Agente.scan_forward(True)
        if aux.valid and not aux.point.visited_flag:
            raiz.C_nodo_h(aux.point,raiz)#Por cada escaneo valido creamos un nuevo nodo
            n_raiz=raiz.hijo[-1]#Guardamos como nueva raiz el nodo[N] de la lista de hijos
            result=rec_busq1(n_raiz,Agente,Matrix,fin_pos,stack,cost)#si es verdadero vamos a tener el stack lleno       
            if result:
                return resultado(stack,cost)
            else:
                Agente.direction=dir
                Agente.position=V_M.assign_point(Matrix,raiz.point.Xcoordinate,raiz.point.Ycoordinate,raiz.point)
        Agente.turn_left()        
        
    return resultado(None,0)
#==================================================================================================================================
#==========================================Algoritmo para el segundo agente=================================================
#==================================================================================================================================
def rec_busq2(raiz:Nodo,Agente:Ag.Agente2,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:list[r_d.Coord],cost:int):
    mov=Agente.move_forward(cost)
    if not mov:
        print("No se mueve")
        return False
    print("Posicion actual ("+str(Agente.position.Xcoordinate)+','+str(Agente.position.Ycoordinate)+')')
    output.append(Agente.position)
    if Agente.position==fin_pos:
        print("Enhorabuena, encontraste la salida")
        return True
    counter=0
    for dirs in range(4):
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid:
            counter+=1
    print(str(counter)+" Valid directions")
    if counter<1:
        return False
    elif counter>1:
        Agente.position.deci_flag=True

    for dirs in range(4):#analizamos en las 4 direcciones para generar los nuevos nodos
        aux=Agente.scan_forward(True)
        if aux.valid and not aux.point.visited_flag:
            dir=Agente.direction
            raiz.C_nodo_h(aux.point,raiz)
            n_raiz=raiz.hijo[-1]
            result=rec_busq2(n_raiz, Agente, Matrix, fin_pos, output, cost)
            if result:
                return True
            Agente.direction=dir
            output.pop()
            Agente.position=V_M.assign_point(Matrix,output[-1].Xcoordinate,output[-1].Ycoordinate,output[-1])
        Agente.turn_rigth()
    return False    
        
 
 
def alg_busq2(raiz:Nodo,Agente:Ag.Agente2,Matrix:r_d.Coord,fin_pos:r_d.Coord)->resultado:
    stack=[]
    cost=0
    stack.append(Agente.position)
    print("Scanning dirs")
    counter=0
    for dirs in range(4):
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid and not aux.point.visited_flag:
            counter+=1
    for dirs in range(4):
        dir=Agente.direction
        aux=Agente.scan_forward(True)
        if aux.valid and not aux.point.visited_flag:
            raiz.C_nodo_h(aux.point,raiz)#Por cada escaneo valido creamos un nuevo nodo
            n_raiz=raiz.hijo[-1]#Guardamos como nueva raiz el nodo[N] de la lista de hijos
            result=rec_busq2(n_raiz,Agente,Matrix,fin_pos,stack,cost)#si es verdadero vamos a tener el stack lleno       
            if result:
                return resultado(stack,cost)
            else:
                Agente.direction=dir
                Agente.position=V_M.assign_point(Matrix,raiz.point.Xcoordinate,raiz.point.Ycoordinate,raiz.point)
        Agente.turn_rigth()       
        
    return resultado(None,0)

 

#==================================================================================================================================
#==========================================Algoritmo para el tercer agente=================================================
#==================================================================================================================================
def rec_busq3(raiz:Nodo,Agente:Ag.Agente3,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:list[r_d.Coord],cost:int,dir:int)->bool:
    scan=list()
    m=Agente.move(dir,cost)
    if not m:
        return False
    if Agente.position==fin_pos:
        return True
    scanned=Agente.scan()
    if len(scanned)>1:
        Agente.position.deci_flag=True
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    for scan in scanned:
        raiz.C_nodo_h(scan,raiz)
        n_raiz=raiz.hijo[-1]
        result=rec_busq3(n_raiz,Agente,Matrix,fin_pos,output,cost,scan.dirs)
        if result:
            return True
    return False
    

def alg_busq3(raiz:Nodo,Agente:Ag.Agente3,Matrix:r_d.Coord,fin_pos:r_d.Coord):
    stack=[]
    print("Scanning dirs")
    cost=0
    raiz=Agente.position
    scanned=Agente.scan()
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    for scan in scanned:
        raiz.C_nodo_h(scan.c_v.point,raiz)
        n_raiz=raiz.hijo[-1]
        result=rec_busq3(n_raiz,Agente,Matrix,fin_pos,stack,cost,scan.dirs)
        if result:
            return resultado(stack,cost)
    return resultado(None,0)
        
#==================================================================================================================================
#==========================================Algoritmo para el cuarto agente=================================================
#==================================================================================================================================
        
    








#==================================================================================================================================
#==========================================Algoritmo para el quinto agente=================================================
#==================================================================================================================================




switch={#switch for the algorithms
    1:alg_busq1,
    2:alg_busq2,
    3:alg_busq3,
    4:alg_busq4,
    5:alg_busq5
}




def comprobacion(partida:r_d.Coord,llegada:r_d.Coord)->bool:
    if partida.Xcoordinate==llegada.Xcoordinate and partida.Ycoordinate==llegada.Ycoordinate:
        return False#Falso si son el mismo punto, no se movio
    return True #true se movio