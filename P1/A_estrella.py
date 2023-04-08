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

def Init_busq(raiz:bp.Nodo,Agente:Ag.Agente5,Matrix:rd.Coord,fin_pos:rd.Coord):
    stack=list()
    stack.append(Agente.position)
    if Agente.position==fin_pos:
        return bp.resultado(stack,cr.switch[Agente.charact](Agente.position.Valor))
    cost=0
    raiz=bp.Nodo(Agente.position,None)
    