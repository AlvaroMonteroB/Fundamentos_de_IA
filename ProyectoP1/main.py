import A_estrella as ae #Algoritmo de A*
import Agentes as ag #Los agentes, este no se toca, ya esta iniciado
import Read_data as rd #leer el archivo y transformarlo una matriz de objetos
from anytree import Node
from anytree import NodeMixin
import copy
import print_tree_console
import arboli
import interfaz as ifz #Es la interfaz grafica
import various_methods as vm #Es para asignar y buscar el punto de la matriz

import Busq_prof as b_p
import Criaturas




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
visitas.append(ifz.point_interes(fpoint_a,"Portal"))
point_ini=vm.assign_point(Matrix1,xi,yi,Matrix1[yi][xi])
AgentA=ag.Agente3(point_ini,'1',Matrix1,False)
raiz_o=b_p.Nodo(AgentA.position,None)
raiz=b_p.Nodo(AgentA.position,None)
#for destiny in visitas:
 #   output=ae.Init_busq(raiz,AgentA,Matrix1,destiny.punto)#stack y cost
  #  if  destiny.punto!=fpoint_a:
   #     ruta = raiz.path(destiny.punto)# Obtiene la ruta de la raíz a "destiny"
    #    print(str(len(ruta))+"\n")
     #   raiz=ruta[-1]
output=ae.Init_busq(raiz,AgentA,Matrix1,visitas[0].punto)#stack y cost    
print_tree_console.tree_to_file(raiz)
ifz.recorrido(Matrix2, fpoint_a, point_ini, None, raiz,visitas)
arboli.show_tree()


costo_pc=calc_cost(output.stack,AgentA)
print("El algoritmo hizo el camino con un costo de "+str(costo_pc))

