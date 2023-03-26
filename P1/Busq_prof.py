import Agentes as Ag
import various_methods as V_M
import Read_data as r_d
import acciones as acc


class resultado:
    def __init__(self):
        self.stack:r_d.Coord
        self.cost=0

class Nodo:
    def __init__(self,point:r_d.Coord):
        self.point=point
        self.hijo=[]
    def C_nodo_h(self,clave):
        self.hijo.append(Nodo(clave))
    def howm_son(self):#Para saber cuantos hijos tiene el nodo
        return len(self.hijo)
    
def rec_busq1(raiz:Nodo,scan:Ag.cost_valid,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:resultado)->bool:
    new_scan=list()
    valid_scan=list()
    Agente.move_forward(output.cost,1)
    if Agente.position==fin_pos:#Si la posicion en la que nos encontramos es la final, devolvemos true
        output.stack.append(Agente.position)#Para que se devuelva el stack generado
        return True#y colocamos la ultima posicion
    output.stack.append(Agente.position)
    for dirs in range(4):#analizamos en las 4 direcciones para generar los nuevos nodos
        Agente.turn_left()
        new_scan.append(Agente.scan_forward())
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
            scan_aux=Agente.scan_forward()#escaneamos para ver que tiene el agente en su direccion actual
            scan_aux=scan_aux.point#guardamos el punto
            c=0
            while aux|c<4:#mientras el auxiliar no nos saque del bucle, escaneamos que hay enfrente(si no jala, cambiar el 4 a 3)
                if n_raiz.point == scan_aux:#Si nuestra nueva raiz es igual al punto que hay enfrente nos metemos y repetimos
                    aux=True
                    res=rec_busq1(n_raiz,src,Agente,Matrix,fin_pos,output)#algoritmo recursivo
                    if res:#Si se encontró el punto retornamos true para guardar el stack
                        return True
                    else:#Si el camino no fue valido, regresamos la posicion actual
                        output.stack.pop()#Quitamos del stack donde no fue valido
                        Agente.position.actual_flag=False
                        Agente.position=V_M.assign_point(Matrix,output.stack[-1].Xcoordinate,output.stack[-1].Ycoordinate)
                        #devolvemos al agente a un estado anterior para repetir la operacion
                else:#Si el escaneo no es el mismo, giramos a la izquierda y guardamos el siguiente punto
                    Agente.turn_left()
                    scan_aux=Agente.scan_forward()
                    scan_aux=scan_aux.point
                c+=1
    if len(valid_scan)==0:#Si no hubo escaneos validos, regresamos
        return False
                     
            
      
    
def alg_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord)->resultado:#inicializacion del algoritmo
    scan=list()
    output=resultado()
    output.stack=list()
    None
    valid_scan=list()
    scan.append(Agente.scan_forward(True))
    output.stack.append(Agente.position)
    dir_ini=Agente.direction
    for dirs in range(3):
        Agente.turn_left()
        scan.append(Agente.scan_forward(True))
    Agente.turn_left()
    for dir in scan:
        if dir.valid:
            valid_scan.append(dir)
        else:
            print("No se encontró ningún punto valido")
            exit()
    if len(valid_scan)>1:
        valid_scan.point.deci_flag=True
    i=0
    if len(valid_scan)>0:
        for scr in valid_scan: 
            raiz.C_nodo_h(scr.point)
            n_raiz=raiz.hijo[i]
            result=rec_busq1(n_raiz,output.stack,valid_scan,Matrix,fin_pos,output)#si es verdadero vamos a tener el stack lleno
            if not result:
                Agente.turn_left()
                i+=1
    if len(valid_scan)==0:
            output=resultado()
            output.cost=5
            output.stack=V_M.busq_point(Matrix,-1,-1)

            return 
    if result:
        return output
        
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