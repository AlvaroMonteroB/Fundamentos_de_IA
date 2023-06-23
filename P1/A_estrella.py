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


def alg_busq1(Raiz:bp.Nodo, Matrix:rd.Coord, Agente:Ag.Agente3, fin_pos:rd.Coord):
    queue = []
    order=0
    heapq.heappush(queue, ( 1,order,Raiz))
    visited = set()

    while queue:
       # print(str(len(queue)))
        _, _, node = heapq.heappop(queue)

        if node.point == fin_pos:
            # Construir el camino desde el punto final hasta el inicial
            path = []
            while node.parent:
                path.append(node.point)
                node = node.parent
            path.append(node.point)
            return list(reversed(path))

        if node in visited:
            continue

        visited.add(node)
        
        Agente.position = vm.assign_point(Matrix,node.point.Xcoordinate,node.point.Ycoordinate,node.point) 
        scanned = Agente.scan()

        for direction in scanned:
            if not direction.dirs:
                continue
            else:
                Agente.position.actual_flag = False
                char_dir = bp.switch2[direction.dirs]
                cost = cr.switch[Agente.charact](direction.c_v.point.Valor)
                m = Agente.move(char_dir, cost)

                if m:
                    heuristic_cost =manhattan_dis(direction.c_v.point, fin_pos)+costo_acumulado(Agente.charact,node)
                    new_node = bp.Nodo(direction.c_v.point, node)
                    new_node.cost(Agente.charact)
                    heapq.heappush(queue, (cost + heuristic_cost, order,new_node))
            order+=1
    return None



def costo_acumulado(charact, nodo_hoja):
    suma = 0
    puntos=list()
    while nodo_hoja.parent:
        puntos.append(nodo_hoja.point)
        nodo_hoja = nodo_hoja.parent
        puntos.append(nodo_hoja.point)
    if len(puntos) == 0:
        return suma

    for punto in puntos:
        suma += cr.switch[charact](punto.Valor)

    return suma

