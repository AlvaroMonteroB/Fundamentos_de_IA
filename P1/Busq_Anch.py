import Busq_prof as b_p
import Read_data as rd
import Agentes as Ag
import various_methods as vm
from collections import deque
class Queue:
    def __init__(self) -> None:
        self.items=[]
    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)






def alg_busq1(Raiz:b_p.Nodo,Matrix:rd.Coord,Agente:Ag.Agente3,fin_pos:rd.Coord):
    queue = deque([(Agente.position, [])])
    visited = set()
    cost=0
    queue = deque([(Agente.position, [Agente.position])])
    while queue:
        node, path = queue.popleft()
        if node == fin_pos:
            return path
        if node in visited:
            continue
        visited.add(node)
        Agente.position = node
        scanned=Agente.scan()
        for direction in scanned:
            if not direction.dirs:
                continue
            else:
                Agente.position.actual_flag=False
                char_dir=b_p.switch2[direction.dirs]
                m=Agente.move(char_dir,cost)
                if m:
                    queue.append((Agente.position, path + [Agente.position]))
                    Agente.position =vm.assign_point(Matrix,node.Xcoordinate,node.Ycoordinate,node)
        
    
    return None