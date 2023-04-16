import Read_data
import Criaturas
import various_methods


#Varios metodos de escaneos van a retornar tuplas
#Asi que hay que descomponer los datos y construir una nueva instancia para usarlos en una funcion que requiera
#el objeto específico

arr={'d':1,'w':2,'a':3,'s':4}
class cost_valid:#Retornaremos esto en todos los casos para revisar a la vez si es punto valido y su costo
    def __init__(self,cost:int,valid:bool,point:Read_data.Coord):
        self.cost=cost
        self.valid=valid
        self.point=point
        
class ag34_out:
    def __init__(self,c_v:cost_valid,dirs:int) -> None:
        self.c_v=c_v#Cost valid
        self.dirs=dirs#direccion
#Tengo que cambiar las condiciones cuando el punto es no valido
class agente1:#left, forward
    def __init__(self,direction,position:Read_data.Coord,charact,Matrix:Read_data.Coord,user_flag:bool) -> None:
        self.direction=direction
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User
    def turn_left(self):#dirs: 1=-> 2=^ 3=<- 4=v
        if self.direction<4 and self.direction>0:
            self.direction+=1
        elif self.direction==4:
            self.direction=1
    def scan_forward(self,auto:bool)->cost_valid:#Censado #to DO
        if self.direction==1:#apunta a la derecha
            X=self.position.Xcoordinate+1
            scanned_pos=various_methods.busq_point(self.Matrix,X,self.position.Ycoordinate)#Nos  retorna el objeto de la posicion a escanear           
            
        elif self.direction==2:#Apunta hacia arriba
            Y=self.position.Ycoordinate-1
            scanned_pos=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,Y)#Nos  retorna el objeto de la posicion a escanear

        elif self.direction==3:#Apunta a la izquierda
            X=self.position.Xcoordinate-1
            scanned_pos=various_methods.busq_point(self.Matrix,X,self.position.Ycoordinate)
            
        elif self.direction==4:#Apunta hacia abajo
            Y=self.position.Ycoordinate+1
            scanned_pos=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,Y)
        if not scanned_pos:
            return cost_valid(0, False, None)
        if scanned_pos.visited_flag:#Si ya visitamos este punto, lo descartamos inmediatamente
            return cost_valid(0,False,scanned_pos)
        cost = Criaturas.switch[self.charact](scanned_pos.Valor)
        if cost==-1:
                return cost_valid(0,False,None)
        elif cost==0:
                return cost_valid(0, False, scanned_pos)
        elif cost>0:  
                return cost_valid(cost,True,scanned_pos)
                
    def move_forward(self,cost:int,movimientos:int)->bool:#dirs: 1=-> 2=^ 3=<- 4=v
        
        if movimientos==1:
            band=self.scan_forward(True)
            if band.valid:
                self.position.actual_flag=False
                self.position=various_methods.assign_point(self.Matrix,band.point.Xcoordinate,band.point.Ycoordinate,self.position)#Asignamos el valor del nuevo punto
                cost=cost+band.cost                                             #Esto afectando al punto dentro de su matriz
                if self.position.Xcoordinate==band.point.Xcoordinate and self.position.Ycoordinate==band.point.Xcoordinate:
                    return True
            else:                  
                return False
        elif movimientos>1:
            for casilla in range(movimientos):
                band=self.scan_forward(True)
                if band.valid:
                    #print(str(band.point.Xcoordinate)+','+str(band.point.Ycoordinate))
                    #a=input()
                    self.position.actual_flag=False
                    self.position=various_methods.assign_point(self.Matrix,band.point.Xcoordinate,band.point.Ycoordinate)
                    cost=cost+band.cost
                    return True
        return False

class Agente2:#left,rigth, forward
    def __init__(self,direction,position:Read_data.Coord,charact,Matrix:Read_data.Coord,user_flag:bool):
        self.direction=direction
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User

    def turn_left(self):
        if self.direction<4 and self.direction>0:
            self.direction+=1
        elif self.direction==4:
            self.direction=1
    def turn_rigth(self):
        if self.direction<5 and self.direction>1:
            self.direction-=1
        elif self.direction==1:
            self.direction=4
        
    def scan_forward(self,auto:bool)->cost_valid:#Censado
        validation=cost_valid(0,True,None)#Se tienen que descomponer las tuplas para usarse
        if self.direction==1:#apunta a la derecha
            X=self.position.Xcoordinate+1
            scanned_pos=various_methods.busq_point(self.Matrix,X,self.position.Ycoordinate)#Nos  retorna el objeto de la posicion a escanear
        elif self.direction==2:#Apunta hacia arriba
            Y=self.position.Ycoordinate-1
            scanned_pos=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,Y)#Nos  retorna el objeto de la posicion a escanear
       
        elif self.direction==3:#Apunta a la izquierda
            X=self.position.Xcoordinate-1
            scanned_pos=various_methods.busq_point(self.Matrix,X,self.position.Ycoordinate)
            
        elif self.direction==4:#Apunta hacia abajo
            Y=self.position.Ycoordinate+1
            scanned_pos=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,Y)
        if not scanned_pos:
            return cost_valid(0,False,None)
        
        if scanned_pos.visited_flag:
            return cost_valid(0, False, scanned_pos)
        cost = Criaturas.switch[self.charact](scanned_pos.Valor)
        if cost==-1:
                return cost_valid(0, False, None)
        elif cost==0:
                if not auto:
                    print("You cannot move there")
                return cost_valid(0,False,scanned_pos)
        elif cost>0:  
                if not self.user_flag and (not self.auto):#not false=true, false=user: not true=false, true = pc, not auto=we see the data
                    print(scanned_pos.print_data(cost))#Interfaz grafica
                return cost_valid(cost,True,scanned_pos)
            
                
    def move_forward(self,cost:int)->bool:#dirs: 1=-> 2=^ 3=<- 4=v
            band=self.scan_forward(True)
            if band.valid:
                self.position.actual_flag=False
                self.position=various_methods.assign_point(self.Matrix,band.point.Xcoordinate,band.point.Ycoordinate,self.position)#Asignamos el valor del nuevo punto
                cost=cost+band.cost                                             #Esto afectando al punto dentro de su matriz
                if self.position.Xcoordinate==band.point.Xcoordinate and self.position.Ycoordinate==band.point.Xcoordinate:
                    return True
            else:                  
                return False
                
            


class Agente3:#move one cell any row or column  
    def __init__(self,position:Read_data.Coord,charact,Matrix:Read_data.Coord,user_flag:bool):
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User
    def scan(self)->list[ag34_out]:#Se tiene que implementar la opcion auto como en los otros agentes
        points=list()
        scan_result=list()#tenemos que seguir el orden de direcciones
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate))#x+1 derecha
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1))#y-1 arriba
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate))#x-1 izquierda
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1))#y+1 abajo
        for x,i in zip(points,range(1,5)):#iteramos en los puntos y en el rango de direcciones
            cos=Criaturas.switch[self.charact](x.Valor)#Calculamos el costo, si es 0 o menor, no es valida la posicion
            if cos>0 and not x.visited_flag:#Si el valor de la posicion es valido, entramos
                #Si no hemos visitado y es valida, adjuntamos la nueva posicion
                scan_result.append(ag34_out(cost_valid(Criaturas.switch[self.charact](x.Valor),True,x),i))#Escaneos validos con la direccion en que se adquirieron
                
        if len(scan_result)>0:#Si la longitud del escaneo es mayor a 0, es valida la funcion
            if len(scan_result)>1:#Si hubo mas de 1, tomamos una desicion
                self.position.deci_flag=True
            return scan_result#Sí hay por lo menos un camino para seguir, aqui lo veremos
        elif len(scan_result)==0:#Si no hubo caminos, retornaremos como no valido
            result=Read_data.Coord('-1', -1, -1, False, False,False,False)#  no hay a donde moverse y hay que regresar
            scan_result.append(ag34_out(cost_valid(0, False, result),None))
            return scan_result#so mp hay caminos disponibles 


     #These methods are for the movement  
     #this is a private method, only can be used by move     
    def scan_pos(self,direction)->cost_valid:#este solo lo usa el metodo move
        if direction==1:#izq
            scanned=various_methods.busq_point(self.Matrix, self.position.Xcoordinate+1,self.position.Ycoordinate)
        elif direction==2:#arriba
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1)
        elif direction==3:#derecha
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate)
        elif direction==4:#abajo
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1)
        elif direction==0:
            return cost_valid(0,False,None)
        cost=Criaturas.switch[self.charact](self.position.Valor)
        if cost>0:
            valid=cost_valid(cost,True,scanned)
        elif cost<0:
            valid=cost_valid(0,False,None)
        elif cost==0:#al final volvemos a evaluar para poder retornar
            valid=cost_valid(0,False,scanned)
        return valid
            
            
    #pos-> d=->, w=^,a=<-,s=v: 1,2,3,4
    def move(self,key,cost)->bool:
      direction = arr[key]
      #aqui directamente hacemos un auto escaneo
      var=self.scan_pos(direction)
      if var.valid:
        self.position.actual_flag=False
        self.position=various_methods.assign_point(self.Matrix,var.point.Xcoordinate, var.point.Ycoordinate,self.position)
        cost=cost+var.cost
        return True
      return False
    


class Agente4:#move to any cell in column or row
    def __init__(self,position:Read_data.Coord,charact,Matrix:Read_data.Coord,user_flag:bool):
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User

    def scan(self)->list[ag34_out]:#Se tiene que implementar la opcion auto como en los otros agentes
        points=list()
        scan_result=list()
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate))#x+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1))#y-1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate))#x-1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1))#y+1 
        for x,i in zip(points,range(1,5)):#iteramos en los puntos y en el rango de direcciones
            cos=Criaturas.switch[self.charact](x.Valor)#Calculamos el costo, si es 0 o menor, no es valida la posicion
            if cos>0 and not x.visited_flag:#Si el valor de la posicion es valido, entramos
                #Si no hemos visitado y es valida, adjuntamos la nueva posicion
                scan_result.append(ag34_out(cost_valid(Criaturas.switch[self.charact](x.Valor),True,x),i))#Escaneos validos con la direccion en que se adquirieron
                
        if len(scan_result)>0:#Si la longitud del escaneo es mayor a 0, es valida la funcion
            if len(scan_result)>1:#Si hubo mas de 1, tomamos una desicion
                self.position.deci_flag=True
            return scan_result#Sí hay por lo menos un camino para seguir, aqui lo veremos
        elif len(scan_result)==0:#Si no hubo caminos, retornaremos como no valido
            result=Read_data.Coord('-1', -1, -1, False, False,False,False)#  no hay a donde moverse y hay que regresar
            scan_result.append(ag34_out(cost_valid(0, False, result),None))
            return scan_result#so mp hay caminos disponibles 

         #These methods are for the movement       
    def scan_pos(self,direction)->Read_data.Coord:#este solo lo usa el metodo move
        if direction==1:#izq
            scanned=various_methods.busq_point(self.Matrix, self.position.Xcoordinate+1,self.position.Ycoordinate)
        elif direction==2:#arriba
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1)
        elif direction==3:#derecha
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate)
        elif direction==4:#abajo
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1)
        elif direction==0:
            return cost_valid(0,False,None)
        cost=Criaturas.switch[self.charact](self.position.Valor)
        if cost>0:
            valid=cost_valid(cost,True,scanned)
        elif cost<0:
            valid=cost_valid(0,False,None)
        elif cost==0:#al final volvemos a evaluar para poder retornar
            valid=cost_valid(0,False,scanned)
        return valid
    
    arr={'d':1,'w':2,'a':3,'s':4}# key:value
    def move(self,key,cost,movimientos:int):
        direction = arr[key]
        for num in range(movimientos):#Necesitamos calcular todo para esta funcion con scan pos de arriba
            new=self.scan_pos(direction)
            if new.valid:
                self.position.actual_flag=False
                self.position=various_methods.assign_point(self.Matrix,new.point.Xcoordinate, new.point.Ycoordinate,self.position)
                cost=cost+new.cost
                return True
            return False


class Agente5:#Move to any cell in any diagonal
    def __init__(self,position:Read_data.Coord,charact,Matrix:Read_data.Coord,user_flag:bool):
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User
    
    def scan_data(self)->ag34_out:#escanea en diagonal
        points=list()
        scan_result=list()
        Not_valid=list()
        already_visited=list()
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate-1))#x+i,y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate-1))#y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate+1))#x-1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate+1))#y-1
        for x,i in zip(points,range(1,5)):#iteramos en los puntos y en el rango de direcciones
            cos=Criaturas.switch[self.charact](x.Valor)#Calculamos el costo, si es 0 o menor, no es valida la posicion
            if cos>0 and not x.visited_flag:#Si el valor de la posicion es valido, entramos
                #Si no hemos visitado y es valida, adjuntamos la nueva posicion
                scan_result.append(ag34_out(cost_valid(Criaturas.switch[self.charact](x.Valor),True,x),i))#Escaneos validos con la direccion en que se adquirieron
                
        if len(scan_result)>0:#Si la longitud del escaneo es mayor a 0, es valida la funcion
            if len(scan_result)>1:#Si hubo mas de 1, tomamos una desicion
                self.position.deci_flag=True
            return scan_result#Sí hay por lo menos un camino para seguir, aqui lo veremos
        elif len(scan_result)==0:#Si no hubo caminos, retornaremos como no valido
            result=Read_data.Coord('-1', -1, -1, False, False,False,False)#  no hay a donde moverse y hay que regresar
            scan_result.append(ag34_out(cost_valid(0, False, result),None))
            return scan_result#so mp hay caminos disponibles 
      #    O O /        \ O O        O O O      O O O
      #1=D=O O O   2=W= O O O   3=A= O O O  4=S=O O O
      #    O O O        O O O        / O O      O O \}
      
    def self_scan(self,direction:int)->cost_valid:
            if direction==1:
                scann_res=various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate-1)#x+i,y-1)
            elif direction==2:
                scann_res=various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate-1) 
            elif direction==3:
                scann_res=various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate+1)
            elif direction==4:
                scann_res=various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate+1)
            valid=cost_valid(Criaturas.switch[self.charact](scann_res.Valor),True,scann_res)
            if scann_res.Valor>0:
                     valid=cost_valid(self.charact.cost(scann_res.Valor),True,scann_res)
            else:
                valid=cost_valid(0,False,scann_res)
            if valid.cost==0:
                valid.valid=False
            return valid
        
        
           
    def move(self,key,movimientos,cost):
        direction=arr[key]
        for num in range(movimientos):
            new=self.self_scan(direction)
            if new.valid:
                self.position.actual_flag=False
                cost=cost+new.cost
                self.position=various_methods.assign_point(self.Matrix,new.point.Xcoordinate,new.point.Ycoordinate)
                cost=cost+new.cost
                return True
            return False
                
            
            
switch_dir={
    1:agente1,
    2:Agente2,
}           
            
switch={
    3:Agente3,
    4:Agente4,
    5:Agente5
}  
            
            
