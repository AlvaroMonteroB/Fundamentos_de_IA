import A_estrella as ae #Algoritmo de A*
import Agentes as ag #Los agentes, este no se toca, ya esta iniciado
import Read_data as rd #leer el archivo y transformarlo una matriz de objetos
from anytree import Node
from anytree import NodeMixin
import copy
import print_tree_console as ptc
import arboli
import interfaz as ifz #Es la interfaz grafica
import various_methods as vm #Es para asignar y buscar el punto de la matriz
import sys
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

    
xi, yi, xf, yf,pers = ifz.select_Ag()#Seleccion del agente
puntos = ifz.AgregarPuntos()#X , Y , TIPO

fpoint_a=vm.busq_point(Matrix,xf,yf)
visitas=[]
matrices=[]
matrices.append(copy.deepcopy(Matrix))
for i in range(len(puntos)):
    Xp,Yp,tipo=puntos[i]
    point=vm.busq_point(matrices[0], Xp, Yp)
    visitas.append(ifz.point_interes(point, tipo))
visitas.append(ifz.point_interes(fpoint_a,"Portal"))
point_ini=vm.assign_point(matrices[0],xi,yi,Matrix[yi][xi])
AgentA=ag.Agente3(point_ini,pers,matrices[0],False)
raiz_o=b_p.Nodo(AgentA.position,None)
raiz=b_p.Nodo(AgentA.position,None)

output=ae.alg_busq1(raiz,matrices[-1],AgentA,visitas,fpoint_a)#stack y cost
if output==None:
    print("No funciono A*")
    sys.exit()
ptc.tree_to_file(raiz)
Mat=copy.deepcopy(Matrix)
ifz.recorrido(Mat,fpoint_a,point_ini,output,None,visitas)
arboli.show_tree()


costo_pc=calc_cost(output.stack,AgentA)
print("El algoritmo hizo el camino con un costo de "+str(costo_pc))

