import Agentes as Ag
import various_methods as V_M
import Read_data as r_d

stack=list()
class Nodo:
    def __init__(self,stack,point:r_d.Coord) -> None:
        self.point=point
        self.hijo=[]
    def C_nodo_h(self,clave,hijo,):
        self.hijo.append(Nodo(clave))
    def how_son(self):#Para saber cuantos hijos tiene el nodo
        return len(self.hijo)