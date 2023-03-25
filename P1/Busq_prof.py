import Agentes as Ag
import various_methods as V_M
import Read_data as r_d
import acciones as acc


class resultado:
    def __init__(self) -> None:
        self.stack=list
        self.cost=0

class Nodo:
    def __init__(self,point:r_d.Coord) -> None:
        self.point=point
        self.hijo=[]
    def C_nodo_h(self,clave):
        self.hijo.append(Nodo(clave))
    def howm_son(self):#Para saber cuantos hijos tiene el nodo
        return len(self.hijo)
    
def rec_busq1(raiz:Nodo,stack:list,scan:Ag.cost_valid,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:resultado)->bool:
    new_scan=list()
    valid_scan=list()
    Agente.move_forward(1,output.cost)
    if Agente.position==fin_pos:#Si la posicion en la que nos encontramos es la final, devolvemos true
        stack.append(Agente.position)#Para que se devuelva el stack generado
        return True#y colocamos la ultima posicion
    stack.append(Agente.position)
    for dirs in range(4):#analizamos en las 4 direcciones para generar los nuevos nodos
        Agente.turn_left
        new_scan.append(Agente.scan_forward)
    for dir in new_scan:#Vamos a ver si se formaron escaneos validos
        if dir.valid:
            valid_scan.append(dir)
    if len(valid_scan)>1:#si hay mas de 1, es que se tuvo que tomar una desicion
        Agente.position.deci_flag=True#Marcamos en la posicion actual ese cambio
    i=0
    if len(valid_scan)>0:#Con que haya una direccion valida, vamos a entrar
        for src in valid_scan:#iteramos en las posiciones validas
            raiz.C_nodo_h(src.point)#creamos nodos hijos por cada una
            n_raiz=raiz.hijo[i]#Nueva raiz con el nodo hijo actual
            aux=True
            scan_aux=Agente.scan_forward#escaneamos para ver que tiene el agente en su direccion actual
            scan_aux=scan_aux.point#guardamos el punto
            c=0
            while aux|c<4:#mientras el auxiliar no nos saque del bucle, escaneamos que hay enfrente(si no jala, cambiar el 4 a 3)
                if n_raiz.point == scan_aux:#Si nuestra nueva raiz es igual al punto que hay enfrente nos metemos y repetimos
                    aux=True
                    res=rec_busq1(n_raiz,stack,src,Agente,Matrix)#algoritmo recursivo
                    if res:#Si se encontró el punto retornamos true para guardar el stack
                        return True
                    else:#Si el camino no fue valido, regresamos la posicion actual
                        stack_pop(stack)
                else:
                    
                    Agente.turn_left
                    scan_aux=Agente.scan_forward
                    scan_aux=scan_aux.point
                c+=1
    if len(valid_scan)==0:
        return
                     
            
      
    
def alg_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,)->r_d.Coord:#inicializacion del algoritmo
    stack=list()
    scan=list()
    output=resultado()
    output.stack=stack
    
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
    if len(valid_scan)==0:
            return 
    if result:
        output.cost
        
def rec_busq2():
    new_scan=list()        
        
 
 
def alg_busq2(raiz:Nodo,Agente:Ag.Agente2)->r_d.Coord:
    stack=list()
 
        
switch={#switch for the algorithms
    1:alg_busq1
}

def stack_pop(stack:list[r_d.Coord]):
    for node in stack_pop:
        if not node.point.deci_flag:
            stack.pop
        else:
            return    