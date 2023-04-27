import A_estrella as ae #Algoritmo de A*
import Agentes as ag #Los agentes, este no se toca, ya esta iniciado
import Read_data as rd #leer el archivo y transformarlo una matriz de objetos
from anytree import Node
from anytree import NodeMixin
import copy
import interfaz as ifz #Es la interfaz grafica
import various_methods as vm #Es para asignar y buscar el punto de la matriz


class Nodo(NodeMixin):
    def __init__(self,point:rd.Coord,padre=None):
        self.point=point
        self.parent=padre
    def __str__(self) -> str:
        if self.point.deci_flag:
            str_out="O({},{})".format(self.point.Xcoordinate,self.point.Ycoordinate)
        else:
            str_out="({},{})".format(self.point.Xcoordinate,self.point.Ycoordinate)
        return str_out+')'


#Aqui empieza
Matrix=[]
rd.read_matrix(Matrix)
Matrix1=copy.deepcopy(Matrix)
Matrix2=copy.deepcopy(Matrix)
Matrix3=copy.deepcopy(Matrix)
Matrix4=copy.deepcopy(Matrix)
    
ifz.select_Ag()

Agente=ag.Agente3()
puntos=list()
puntos.append(None)
raiz=Nodo(point,None)#Falta definir el punto y las posiciones finales
for punto in range(1,len(puntos)):
    ae.Init_busq(raiz, Agente, Matrix, fin_pos)