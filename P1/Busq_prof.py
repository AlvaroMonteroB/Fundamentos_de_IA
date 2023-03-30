import Agentes as Ag
import various_methods as V_M
import Read_data as r_d
import acciones as acc
import sys

sys.setrecursionlimit(8000)

class resultado:
    def __init__(self,stack,cost):
        self.stack=stack
        self.cost=cost

class Nodo:
    def __init__(self,point:r_d.Coord):
        self.point=point
        self.hijo=[]
    def C_nodo_h(self,clave):
        self.hijo.append(Nodo(clave))
    def howm_son(self):#Para saber cuantos hijos tiene el nodo
        return len(self.hijo)
    
def rec_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord,output:list[r_d.Coord],cost:int)->bool:
    new_scan=list()
    valid_scan=list()
    ini=Agente.position
    mov=Agente.move_forward(cost,1)
    fin=Agente.position
    if not comprobacion(ini, fin):#Comprovacion a ver si nos movimos
        print("No sirve aqui")
        return False
    if not mov:
        print("Aqui tampoco sirve")
        return False
    else:
        print("Valid")
    print(str(Agente.position.Xcoordinate)+','+str(Agente.position.Ycoordinate)+' '+Agente.position.Valor+'\n')
    if (Agente.position.Xcoordinate==fin_pos.Xcoordinate) and( Agente.position.Ycoordinate==fin_pos.Ycoordinate):#Si la posicion en la que nos encontramos es la final, devolvemos true
        output.append(Agente.position)#Para que se devuelva el stack generado
        return True#y colocamos la ultima posicion
    output.append(Agente.position)
    for dirs in range(4):#analizamos en las 4 direcciones para generar los nuevos nodos
        Agente.turn_left()
        new_scan.append(Agente.scan_forward(True))
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
            
            #escaneamos para ver que tiene el agente en su direccion actual
            scan_aux=Agente.scan_forward(True)#guardamos el punto
            c=0
            while aux and c<4:#mientras el auxiliar no nos saque del bucle, escaneamos que hay enfrente(si no jala, cambiar el 4 a 3)
                if n_raiz.point == scan_aux:#Si nuestra nueva raiz es igual al punto que hay enfrente nos metemos y repetimos
                    aux=True
                    res=rec_busq1(n_raiz,Agente,Matrix,fin_pos,output,cost)#algoritmo recursivo
                    if res:#Si se encontró el punto retornamos true para guardar el stack
                        return True
                    else:#Si el camino no fue valido, regresamos la posicion actual
                        output.pop()#Quitamos del stack donde no fue valido
                        Agente.position.actual_flag=False
                        Agente.position=V_M.assign_point(Matrix,output.stack[-1].Xcoordinate,output.stack[-1].Ycoordinate)
                        #devolvemos al agente a un estado anterior para repetir la operacion
                else:#Si el escaneo no es el mismo, giramos a la izquierda y guardamos el siguiente punto
                    Agente.turn_left()
                    result=Agente.scan_forward(True)
                    scan_aux=result.point
                c+=1
    if len(valid_scan)==0:#Si no hubo escaneos validos, regresamos
        return False
                     
            
      
    
def alg_busq1(raiz:Nodo,Agente:Ag.agente1,Matrix:r_d.Coord,fin_pos:r_d.Coord)->resultado:#inicializacion del algoritmo
    scan=list()   
    direction=list()
    valid_scan=list()
    result = Agente.scan_forward(True)
    scan.append(result)
    dir_ini=Agente.direction
    print("Scanning dirs")
    for dirs in range(3):#Escaneamos en todas las direcciones
        Agente.turn_left()
        scan.append(Agente.scan_forward(True))
    Agente.turn_left()
    for dir_obj in scan:#Iteramos en los escaneos obtenidos
        if dir_obj.valid:#Si algun escaneo fue valido lo añadimos a la lista
            valid_scan.append(dir_obj)
            direction.append(Agente.direction)
    if len(valid_scan)>1:#Si hubo mas de un escaneo valido, se marca como una decision
        Agente.position.deci_flag=True
    i=0
    o=0
    if len(valid_scan)>0:#Con que haya un escaneo valido entramos
        cost=0
        stack=list()
        dir_ini=Agente.direction
        output=resultado(stack, 0)
        result=False
        for scr in valid_scan: #Iteramos en los escaneos validos
            raiz.C_nodo_h(scr.point)#Por cada escaneo valido creamos un nuevo nodo
            n_raiz=raiz.hijo[i]#Guardamos como nueva raiz el nodo[N] de la lista de hijos
            Agente.direction=direction[o]
            

            
            #Llamaremos a la otra funcion, usando esta nueva raiz
            result=rec_busq1(n_raiz,Agente,Matrix,fin_pos,output,output.cost)#si es verdadero vamos a tener el stack lleno              
            if result:
                break
    if len(valid_scan)==0:#Aqui termina el control de los escaneos
            return resultado(None,0)

    if result:#Si del algoritmo se encontró la salida, retornamos el stack y el costo
        return output
    else:
        return resultado(None,0)#Si no, se envia vacio
#==================================================================================================================================
#==========================================Algoritmo para el segundo agente=================================================
#==================================================================================================================================
def rec_busq2():
    new_scan=list()        
        
 
 
def alg_busq2(raiz:Nodo,Agente:Ag.Agente2)->r_d.Coord:
    stack=list()
 
        


def stack_pop(stack:list[r_d.Coord]):
    for node in stack_pop:
        if not node.point.deci_flag:
            stack.pop
        else:
            return    

#==================================================================================================================================
#==========================================Algoritmo para el tercer agente=================================================
#==================================================================================================================================
def rec_busq3():
    new_scan=list()


def alg_busq3():
    scan=list()












switch={#switch for the algorithms
    1:alg_busq1,
    2:alg_busq2,
    3:alg_busq3
}




def comprobacion(partida:r_d.Coord,llegada:r_d.Coord)->bool:
    if partida.Xcoordinate==llegada.Xcoordinate and partida.Ycoordinate==llegada.Ycoordinate:
        return False#Falso si son el mismo punto, no se movio
    return True #true se movio