import Agentes as Ag
import various_methods as V_M
import Read_data as r_d
import acciones as acc
import Criaturas as cr
import sys
from anytree import Node
from anytree import NodeMixin
sys.setrecursionlimit(8000)


"""
Las funciones alg_busqX inicializan el proceso para que posteriormente entremos a la función recursiva "rec_busqX"
si se encuentra el resultado, alg_busq devolvera la pila del camino correcto
"""



class resultado:
    def __init__(self,stack,cost):
        self.stack=stack
        self.cost=cost

class Nodo(NodeMixin):
    def __init__(self,point:r_d.Coord,padre):
        super(Nodo,self).__init__()
        self.point=point
        self.hijo=[]
        self.padre=padre
    def C_nodo_h(self,clave_hijo:r_d.Coord,padre):
        self.hijo.append(Nodo(clave_hijo,padre))
    def __str__(self) -> str:
        if self.point.deci_flag:
            str_out="O({},{})".format(self.point.Xcoordinate,self.point.Ycoordinate)
        elif self.point.actual_flag:
            str_out="Fin({},{})".format(self.point.Xcoordinate,self.point.Ycoordinate)
        else:
            str_out="({},{})".format(self.point.Xcoordinate,self.point.Ycoordinate)
        return str_out+')'
    
    
    
    
    
    
def rec_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:list[r_d.Coord],cost:int)->bool:
    mov=Agente.move_forward(cost,1)
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
    if Agente.position==fin_pos:
        print("Enhorabuena, encontraste la salida")
        return resultado(stack,cr.switch[Agente.charact](Agente.position.Valor))
    cost=0
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
    if Agente.position==fin_pos:
        print("Enhorabuena, encontraste la salida")
        return resultado(stack,cr.switch[Agente.charact](Agente.position.Valor))
    print("Scanning dirs")
    counter=0
    for dirs in range(4):
        Agente.turn_left()
        aux=Agente.scan_forward(True)
        if aux.valid and not aux.point.visited_flag:
            counter+=1
    if counter>1:
        Agente.position.deci_flag=True
    for dirs in range(4):
        dir=Agente.direction#Guardamos la direccion inicial
        aux=Agente.scan_forward(True)#Escaneamos lo que haya en esa direccion
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
    if not dir:
        return False
    char_dir=switch2[dir]
    m=Agente.move(char_dir,cost)
    if not m:
        return False
    output.append(Agente.position)
    if Agente.position==fin_pos:
        return True
    scanned=Agente.scan()
    if len(scanned)>1:
        Agente.position.deci_flag=True
    elif len(scanned)==0:
        return False
    elif not scanned[-1].c_v.valid:
        return False
    for scan in scanned:
        raiz.C_nodo_h(scan,raiz)
        n_raiz=raiz.hijo[-1]
        result=rec_busq3(n_raiz,Agente,Matrix,fin_pos,output,cost,scan.dirs)
        if result:
            return True
        output.pop()
        Agente.position=V_M.assign_point(Matrix,output[-1].Xcoordinate,output[-1].Ycoordinate,output[-1])
        
    return False
    

def alg_busq3(raiz:Nodo,Agente:Ag.Agente3,Matrix:r_d.Coord,fin_pos:r_d.Coord):
    stack=[]
    stack.append(Agente.position)
    if Agente.position==fin_pos:
        print("Enhorabuena, encontraste la salida")
        return resultado(stack,cr.switch[Agente.charact](Agente.position.Valor))
    
    cost=0
    raiz=Nodo(Agente.position,None)
    scanned=Agente.scan()#Nos devolverá todas las posiciones validas con su direccion
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    if len(scanned)>1:
        Agente.position.deci_flag=True
    for scan in scanned:#Iteramos sobre las posiciones y creamos la raiz
        if not (scan.c_v.point.Valor=='-1'):
            raiz.C_nodo_h(scan.c_v.point,raiz)
            n_raiz=raiz.hijo[-1]
            result=rec_busq3(n_raiz,Agente,Matrix,fin_pos,stack,cost,scan.dirs)
            if result:
                return resultado(stack,cost)
    return resultado(None,0)
        
#==================================================================================================================================
#==========================================Algoritmo para el cuarto agente=================================================
#==================================================================================================================================
def rec_busq4(raiz:Nodo,Agente:Ag.Agente4,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:list[r_d.Coord],cost:int,dir:int):
    if not dir:
        return False
    char_dir=switch2[dir]
    m=Agente.move(char_dir,cost,1)
    output.append(Agente.position)
    if Agente.position==fin_pos:
        return True
    scanned=Agente.scan()
    if len(scanned)>1:
        Agente.position.deci_flag=True
    elif len(scanned)==0:
        return False
    elif not scanned[-1].c_v.valid:
        return False
    for scan in scanned:
        raiz.C_nodo_h(scan,raiz)
        n_raiz=raiz.hijo[-1]
        result=rec_busq4(n_raiz,Agente,Matrix,fin_pos,output,cost,scan.dirs)
        if result:
            return True
        output.pop()
        Agente.position=V_M.assign_point(Matrix,output[-1].Xcoordinate,output[-1].Ycoordinate,output[-1])
        
    return False            
    


def alg_busq4(raiz:Nodo,Agente:Ag.Agente4,Matrix:r_d.Coord,fin_pos:r_d.Coord):
    stack=list()
    stack.append(Agente.position)
    if Agente.position==fin_pos:
        print("Enhorabuena, encontraste la salida")
        return resultado(stack,cr.switch[Agente.charact](Agente.position.Valor))
    
    cost=0
    raiz=Nodo(Agente.position,None)
    scanned=Agente.scan()#Nos devolverá todas las posiciones validas con su direccion
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    if len(scanned)>1:
        Agente.position.deci_flag=True
    for scan in scanned:#Iteramos sobre las posiciones y creamos la raiz
        if not (scan.c_v.point.Valor=='-1'):
            raiz.C_nodo_h(scan.c_v.point,raiz)
            n_raiz=raiz.hijo[-1]
            result=rec_busq4(n_raiz,Agente,Matrix,fin_pos,stack,cost,scan.dirs)
            if result:
                return resultado(stack,cost)
    return resultado(None,0)




#==================================================================================================================================
#==========================================Algoritmo para el quinto agente=================================================
#==================================================================================================================================
def rec_busq5(raiz:Nodo,Agente:Ag.Agente5,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:list[r_d.Coord],cost:int,dir:int):
    if not dir:
        return False
    char_dir=switch2[dir]
    m=Agente.move(char_dir,cost,1)
    output.append(Agente.position)
    if Agente.position==fin_pos:
        return True
    scanned=Agente.scan()
    if len(scanned)>1:
        Agente.position.deci_flag=True
    elif len(scanned)==0:
        return False
    elif not scanned[-1].c_v.valid:
        return False
    for scan in scanned:
        raiz.C_nodo_h(scan,raiz)
        n_raiz=raiz.hijo[-1]
        result=rec_busq5(n_raiz,Agente,Matrix,fin_pos,output,cost,scan.dirs)
        if result:
            return True
        output.pop()
        Agente.position=V_M.assign_point(Matrix,output[-1].Xcoordinate,output[-1].Ycoordinate,output[-1])
        
    return False            




def alg_busq5(raiz:Nodo,Agente:Ag.Agente5,Matrix:r_d.Coord,fin_pos:r_d.Coord):
    stack=list()
    stack.append(Agente.position)
    if Agente.position==fin_pos:
        print("Enhorabuena, encontraste la salida")
        return resultado(stack,cr.switch[Agente.charact](Agente.position.Valor))
    
    cost=0
    raiz=Nodo(Agente.position,None)
    scanned=Agente.scan_data()#Nos devolverá todas las posiciones validas con su direccion
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    if len(scanned)>1:
        Agente.position.deci_flag=True
    for scan in scanned:#Iteramos sobre las posiciones y creamos la raiz
        if not (scan.c_v.point.Valor=='-1'):
            raiz.C_nodo_h(scan.c_v.point,raiz)
            n_raiz=raiz.hijo[-1]
            result=rec_busq5(n_raiz,Agente,Matrix,fin_pos,stack,cost,scan.dirs)
            if result:
                return resultado(stack,cost)
    return resultado(None,0)
















switch={#switch for the algorithms
    1:alg_busq1,
    2:alg_busq2,
    3:alg_busq3,
    4:alg_busq4,
    5:alg_busq5
}

switch2={
    1:'d',
    2:'w',
    3:'a',
    4:'s'
}



def comprobacion(partida:r_d.Coord,llegada:r_d.Coord)->bool:
    if partida.Xcoordinate==llegada.Xcoordinate and partida.Ycoordinate==llegada.Ycoordinate:
        return False#Falso si son el mismo punto, no se movio
    return True #true se movio