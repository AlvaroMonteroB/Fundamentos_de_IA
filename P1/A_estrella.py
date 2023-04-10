import Agentes as Ag
import Read_data as rd
import various_methods as vm
import Busq_prof as bp
import Criaturas as cr
import heapq

def manhattan_dis(dest:rd.Coord,act:rd.Coord):
    return abs(dest.Xcoordinate-act.Xcoordinate)+abs(dest.Ycoordinate-act.Ycoordinate)
    
def euc_dis(dest:rd.Coord,act:rd.Coord):
    return ((dest.Xcoordinate-act.Xcoordinate)**2+(dest.Ycoordinate-act.Ycoordinate)**2)**.5




def rec_busq(raiz:bp.Nodo,Agente:Ag.Agente3,Matrix:rd.Coord,fin_pos:rd.Coord,output:list[rd.Coord],cost:int,dir:int):
    if not dir:
        return False
    char_dir=bp.switch2[dir]
    m=Agente.move(char_dir,cost)
    if not m:
        return False
    output.append(Agente.position)
    if Agente.position==fin_pos:
        return True
    scanned=Agente.scan()#Posiciones escaneadas
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    if len(scanned)>1:#Si hay mas de un escaneo valido hub una desicion
        Agente.position.deci_flag=True
    cola=gen_q(scanned, fin_pos, Agente)#Iniciamos la cola de prioridad
    for i in range(len(scanned)):
        #Cola tiene estructura cost, manht dist, euc dist y el objeto
        cost,manh_dist,euc_dist,obj=heapq.heappop(cola)
        #obj tiene estructura cost valid y direction
        raiz.C_nodo_h(obj.c_v.point, raiz)
        n_raiz=raiz.hijo[-1]
        result=rec_busq(raiz, Agente, Matrix, fin_pos, output, cost, obj.dirs)
        if result:
            return True
    return False

    




def Init_busq(raiz:bp.Nodo,Agente:Ag.Agente3,Matrix:rd.Coord,fin_pos:rd.Coord):
    stack=list()
    stack.append(Agente.position)
    if Agente.position==fin_pos:
        return bp.resultado(stack,cr.switch[Agente.charact](Agente.position.Valor))
    cost=0
    raiz=bp.Nodo(Agente.position,None)#Iniciamos la primera posicion como la raiz
    scanned=Agente.scan()#Posiciones escaneadas
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    if len(scanned)>1:#Si hay mas de un escaneo valido hub una desicion
        Agente.position.deci_flag=True
    cola=gen_q(scanned, fin_pos, Agente)#Iniciamos la cola de prioridad
    for i in range(len(scanned)):
        #Cola tiene estructura cost, manht dist, euc dist y el objeto
        cost,manh_dist,euc_dist,obj=heapq.heappop(cola)
        #obj tiene estructura cost valid y direction
        raiz.C_nodo_h(obj.c_v.point, raiz)
        n_raiz=raiz.hijo[-1]
        result=rec_busq(raiz, Agente, Matrix, fin_pos, stack, cost, obj.dirs)
        if result:
            return bp.resultado(stack,cost)
    return bp.resultado(None,0)


    


    


#Necesitamos calcular su costo, distancia euclidiana y mahattan
def gen_q(lista:Ag.ag34_out,fin_pos:rd.Coord,Agente:Ag.Agente3)->list():#Vamos a generar la priority queue
    cola=list()
    for elementos in lista:#heap, costo para moverse, dist manhattan, dist euclidiana
        heapq.heappush(cola, (-cr.switch[Agente.charact](elementos.c_v.point.Valor),manhattan_dis(fin_pos, elementos.c_v.point),euc_dis(fin_pos, elementos.c_v.point),elementos))
    return cola