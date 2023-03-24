import Agentes as Ag
import various_methods as V_M
import Read_data as r_d
import acciones as acc


class Nodo:
    def __init__(self,point:r_d.Coord) -> None:
        self.point=point
        self.hijo=[]
    def C_nodo_h(self,clave):
        self.hijo.append(Nodo(clave))
    def howm_son(self):#Para saber cuantos hijos tiene el nodo
        return len(self.hijo)
    
    
    
def alg_busq1(raiz:Nodo,Agente:Ag.agente1,action:bool):
    scan=Agente.scan_forward
    if scan.valid:
        raiz.C_nodo_h(Agente.position)