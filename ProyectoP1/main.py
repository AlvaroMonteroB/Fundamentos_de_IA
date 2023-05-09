import A_estrella as ae #Algoritmo de A*
import Agentes as ag #Los agentes, este no se toca, ya esta iniciado
import Read_data as rd #leer el archivo y transformarlo una matriz de objetos
from anytree import Node
from anytree import NodeMixin
import copy
import interfaz as ifz #Es la interfaz grafica
import various_methods as vm #Es para asignar y buscar el punto de la matriz
<<<<<<< HEAD
import Busq_prof as b_p
import Criaturas


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

def calc_cost(stack,Agente)->int:
    cost=0
    for layer in stack:
        cost=cost+Criaturas.switch[Agente.charact](layer.Valor)
    return cost

#Aqui empieza
Matrix=[]
rd.read_matrix(Matrix)
Matrix1 = copy.deepcopy(Matrix)
Matrix2=copy.deepcopy(Matrix)
Matrix3=copy.deepcopy(Matrix)
Matrix4=copy.deepcopy(Matrix)
    
xi, yi, xf, yf = ifz.select_Ag()#Seleccion del agente
puntos = ifz.AgregarPuntos()#X , Y , TIPO

fpoint_a=vm.busq_point(Matrix1,xf,yf)
visitas=[]
for i in range(len(puntos)):
    Xp,Yp,tipo=puntos[i]
    point=vm.busq_point(Matrix1, Xp, Yp)
    visitas.append(ifz.point_interes(point, tipo))
visitas.append((fpoint_a,"portal"))

print("Prueba con A*")
point_ini=vm.assign_point(Matrix1,xi,yi,Matrix1[yi][xi])
AgentA=ag.Agente3(point_ini,'1',Matrix1,False)
raiz_o=b_p.Nodo(AgentA.position,None)
raiz=b_p.Nodo(AgentA.position,None)
fin=vm.busq_point(Matrix,xf,yf)
fin.visited_flag=False
for destiny in visitas:
    output=ae.Init_busq(raiz,AgentA,Matrix,destiny.punto)#stack y cost
    if  destiny.punto!=fin:
        ruta = raiz.path(raiz_o) # Obtiene la ruta de la raíz a "destiny"
        ultimo_nodo = ruta[-2]
        raiz=b_p.Nodo(fin,ultimo_nodo)
print_tree_console.tree_to_file(raiz)
ifz.recorrido(Matrix2, fin, point_ini, None, raiz)
arboli.show_tree()


costo_pc=calc_cost(solution.stack,AgentePC)
print("El algoritmo hizo el camino con un costo de "+str(costo_pc))

