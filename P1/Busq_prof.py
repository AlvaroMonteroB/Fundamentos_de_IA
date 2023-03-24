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
    
def rec_busq1(raiz:Nodo,stack:list,scan:list):
    new_scan=list()
      
    
def alg_busq1(raiz:Nodo,Agente:Ag.agente1)->r_d.Coord:
    stack=list()
    scan=list()
    valid_scan=list()
    scan.append(Agente.scan_forward)
    stack.append(raiz)
    dir_ini=Agente.direction
    for dirs in range(4):
        scan.append(Agente.scan_forward)
        Agente.turn_left
    for dir in scan:
        if dir.valid:
            valid_scan.append(dir)
    n_raiz=raiz.C_nodo_h(valid_scan)
    rec_busq1(valid_scan,stack,valid_scan)
        
        
        
        
        
switch={#switch for the algorithms
    1:alg_busq1
}