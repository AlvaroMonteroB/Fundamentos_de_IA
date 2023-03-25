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
    
def rec_busq1(raiz:Nodo,stack:list,scan:Ag.cost_valid,Agente:Ag.agente1,Matrix:r_d.Coord):
    new_scan=list()
    valid_scan=list()
    Agente.move_forward
    stack.append(scan.point)
    for dirs in range(4):
        Agente.turn_left
        new_scan.append(Agente.scan_forward)
    for dir in new_scan:
        if dir.valid:
            valid_scan.append(dir)
    if len(valid_scan)>1:
        valid_scan.point.deci_flag=True
    i=0
    if len(valid_scan)>0:
        for src in valid_scan:
            raiz.C_nodo_h(src.point)
            n_raiz=raiz.hijo[i]
            
      
    
def alg_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord)->r_d.Coord:
    stack=list()
    scan=list()
    valid_scan=list()
    scan.append(Agente.scan_forward)
    stack.append(raiz.point)
    dir_ini=Agente.direction
    for dirs in range(4):
        Agente.turn_left
        scan.append(Agente.scan_forward)
    for dir in scan:
        if dir.valid:
            valid_scan.append(dir)
    if len(valid_scan)>1:
        valid_scan.point.deci_flag=True
    i=0
    if len(valid_scan)>0:
        for scr in valid_scan: 
            raiz.C_nodo_h(scr.point)
            n_raiz=raiz.hijo[i]
            result=rec_busq1(n_raiz,stack,valid_scan,Matrix)
            if not result:
                Agente.turn_left
                i+=1
        #    else:
        
        
def rec_busq2():
    new_scan=list()        
        
 
 
def alg_busq2(raiz:Nodo,Agente:Ag.Agente2)->r_d.Coord:
    stack=list()
 
        
switch={#switch for the algorithms
    1:alg_busq1
}