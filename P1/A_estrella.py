import Agentes as Ag
import Read_data as rd
import various_methods as vm
import Busq_prof as bp
import Criaturas as cr
from collections import deque
import heapq
import copy

from collections import deque
import heapq
def manhattan_dis(dest:rd.Coord,act:rd.Coord):
    return abs(dest.Xcoordinate-act.Xcoordinate)+abs(dest.Ycoordinate-act.Ycoordinate)
    
def euc_dis(dest:rd.Coord,act:rd.Coord):
    return ((dest.Xcoordinate-act.Xcoordinate)**2+(dest.Ycoordinate-act.Ycoordinate)**2)**.5




def rec_busq(raiz:bp.Nodo,Agente:Ag.Agente3,Matrix:rd.Coord,fin_pos:rd.Coord,output:list[rd.Coord],cost:int,dir:int,ini_pos:rd.Coord):
    if not dir:
        return False
    char_dir=bp.switch2[dir]
    Agente.position.actual_flag=False
    temp=Agente.position
    m=Agente.move(char_dir,cost)
    if not m:
        return False
    output.append(Agente.position)
    if(manhattan_dis(raiz.root.point,fin_pos)<len(output) and manhattan_dis(fin_pos,temp)<manhattan_dis(fin_pos,Agente.position)):
        return False
    
   
    if Agente.position==fin_pos:
        return True
    scanned=Agente.scan()#Posiciones escaneadas
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    if len(scanned)>1:#Si hay mas de un escaneo valido hub una desicion
        Agente.position.deci_flag=True
    if not scanned[-1].c_v.valid:
        return False
    cola=gen_q(scanned, fin_pos, Agente,ini_pos,output)#Iniciamos la cola de prioridad
    while len(cola)>0:
        #Cola tiene estructura cost, manht dist, euc dist y el objeto
        cost=cola[0]
        heapq.heappop(cola)
        #obj tiene estructura cost valid y direction
        for slf in scanned:
            if (cr.switch[Agente.charact](slf.c_v.point.Valor)+manhattan_dis(slf.c_v.point,Agente.position))==cost:
                obj=slf
                break
        n_raiz=bp.Nodo(obj.c_v.point, raiz)
        result=rec_busq(n_raiz, Agente, Matrix, fin_pos, output, cost, obj.dirs,ini_pos)
        if result:
            return True
        output.pop()
        Agente.position=vm.assign_point(Matrix,output[-1].Xcoordinate,output[-1].Ycoordinate,output[-1])
    return False

    




def Init_busq(raiz:bp.Nodo,Agente:Ag.Agente3,Matrix:rd.Coord,fin_pos:rd.Coord):
    stack=list()
    stack.append(Agente.position)
    ini_pos=copy.deepcopy(Agente.position)
    if Agente.position==fin_pos:
        return bp.resultado(stack,cr.switch[Agente.charact](Agente.position.Valor))
    cost=0
    scanned=Agente.scan()#Posiciones escaneadas
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    if len(scanned)>1:#Si hay mas de un escaneo valido hub una desicion
        Agente.position.deci_flag=True
    cola=gen_q(scanned, fin_pos, Agente,ini_pos,stack)#Iniciamos la cola de prioridad
    if not scanned[-1].c_v.valid:
        return False
    for i in range(len(scanned)):
        #Cola tiene estructura cost, manht dist, euc dist y el objeto
        cost=cola[0]
        band=False
        heapq.heappop(cola)
        for slf in scanned:
            if (cr.switch[Agente.charact](slf.c_v.point.Valor)+manhattan_dis(slf.c_v.point,Agente.position))==cost :
                obj=slf
                break
        #obj tiene estructura cost valid y direction
        n_raiz=bp.Nodo(obj.c_v.point,raiz)
        result=rec_busq(n_raiz, Agente, Matrix, fin_pos, stack, cost, obj.dirs,ini_pos)
        if result:
            return bp.resultado(stack,cost)
        stack.pop()
        Agente.position=vm.assign_point(Matrix,stack[-1].Xcoordinate,stack[-1].Ycoordinate,stack[-1])
    return bp.resultado(None,0)



def gen_q(lista, fin_pos, Agente, ini, output):
    cola = []
    for elementos in lista:
        acumulado = costo_acumulado(Agente.charact, output)
        heapq.heappush(cola, manhattan_dis(elementos.c_v.point, Agente.position) + cr.switch[Agente.charact](elementos.c_v.point.Valor))

    return cola

def costo_acumulado(charact, puntos):
    suma = 0
    if len(puntos) == 0:
        return suma

    for punto in puntos:
        suma += cr.switch[charact](punto.Valor)

    return suma

