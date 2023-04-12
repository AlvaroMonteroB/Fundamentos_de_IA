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
    Agente.position.actual_flag=False
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
    if not scanned[-1].c_v.valid:
        return False
    cola=gen_q(scanned, fin_pos, Agente)#Iniciamos la cola de prioridad
    for i in range(len(scanned)):
        #Cola tiene estructura cost, manht dist, euc dist y el objeto
        manh_dist,cost,euc_dist=cola[0]
        heapq.heappop(cola)
        #obj tiene estructura cost valid y direction
        for slf in scanned:
            if (-cr.switch[Agente.charact](slf.c_v.point.Valor))==cost and manh_dist==manhattan_dis(fin_pos,slf.c_v.point) and euc_dist==euc_dis(fin_pos,slf.c_v.point):
                obj=slf
                break
        n_raiz=bp.Nodo(obj.c_v.point, raiz)
        result=rec_busq(n_raiz, Agente, Matrix, fin_pos, output, cost, obj.dirs)
        if result:
            return True
        output.pop()
        Agente.position=vm.assign_point(Matrix,output[-1].Xcoordinate,output[-1].Ycoordinate,output[-1])
    return False

    




def Init_busq(raiz:bp.Nodo,Agente:Ag.Agente3,Matrix:rd.Coord,fin_pos:rd.Coord):
    stack=list()
    stack.append(Agente.position)
    if Agente.position==fin_pos:
        return bp.resultado(stack,cr.switch[Agente.charact](Agente.position.Valor))
    cost=0
    scanned=Agente.scan()#Posiciones escaneadas
    if len(scanned)==0:
        print("No hay movimientos validos")
        exit()
    if len(scanned)>1:#Si hay mas de un escaneo valido hub una desicion
        Agente.position.deci_flag=True
    cola=gen_q(scanned, fin_pos, Agente)#Iniciamos la cola de prioridad
    if not scanned[-1].c_v.valid:
        return False
    for i in range(len(scanned)):
        #Cola tiene estructura cost, manht dist, euc dist y el objeto
        manh_dist, cost, euc_dist=cola[0]
        band=False
        heapq.heappop(cola)
        for slf in scanned:
            if manh_dist==manhattan_dis(fin_pos,slf.c_v.point) and(-cr.switch[Agente.charact](slf.c_v.point.Valor))==cost and  euc_dist==euc_dis(fin_pos,slf.c_v.point):
                obj=slf
                break
        #obj tiene estructura cost valid y direction
        n_raiz=bp.Nodo(obj.c_v.point,raiz)
        result=rec_busq(n_raiz, Agente, Matrix, fin_pos, stack, cost, obj.dirs)
        if result:
            return bp.resultado(stack,cost)
        stack.pop()
        Agente.position=vm.assign_point(Matrix,stack[-1].Xcoordinate,stack[-1].Ycoordinate,stack[-1])
    return bp.resultado(None,0)


    


    


#Necesitamos calcular su costo, distancia euclidiana y mahattan
def gen_q(lista:Ag.ag34_out,fin_pos:rd.Coord,Agente:Ag.Agente3)->list():#Vamos a generar la priority queue
    cola=list()
    for elementos in lista:#heap, costo para moverse, dist manhattan, dist euclidiana
        heapq.heappush(cola, (manhattan_dis(fin_pos, elementos.c_v.point), -cr.switch[Agente.charact](elementos.c_v.point.Valor), euc_dis(fin_pos, elementos.c_v.point)))
    return cola