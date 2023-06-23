import Agentes as Ag
import various_methods as V_M
import Read_data as r_d
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
    def __init__(self,point:r_d.Coord,padre=None):
        self.point=point
        self.parent=padre
    def __str__(self) -> str:
        if self.point.deci_flag:
            str_out="O({},{})".format(self.point.Xcoordinate,self.point.Ycoordinate)
        else:
            str_out="({},{})".format(self.point.Xcoordinate,self.point.Ycoordinate)
        return str_out+')'
    def descendants(self):
        return super().descendants
    def path(self,point=None):
        return super().path()

    
    


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