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


def alg_busq1(Raiz, Matrix: rd.Coord, Agente: Ag.Agente3, fin_pos):
    queue = []
    heapq.heappush(queue, 0, Raiz)
    visited = set()

    while queue:
        _, node = heapq.heappop(queue)

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
        Agente.position = node.point
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
                    heuristic_cost = manhattan_dis(direction.c_v.point, fin_pos)
                    new_node = bp.Nodo(direction.c_v.point, node)
                    heapq.heappush(queue, (cost + heuristic_cost, new_node))

    return None


def gen_q(lista, fin_pos, Agente, ini, output):
    cola = []
    for elementos in lista:
        acumulado = costo_acumulado(Agente.charact, output)
        heapq.heappush(cola, manhattan_dis(elementos.c_v.point, Agente.position) + cr.switch[Agente.charact](elementos.c_v.point.Valor) + acumulado)

    return cola

def costo_acumulado(charact, puntos):
    suma = 0
    if len(puntos) == 0:
        return suma

    for punto in puntos:
        suma += cr.switch[charact](punto.Valor)

    return suma

