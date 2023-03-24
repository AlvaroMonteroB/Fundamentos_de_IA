import Read_data
import Busq_prof
import Criaturas
import various_methods
arr={'d':1,'w':2,'a':3,'s':4}
class cost_valid:#Retornaremos esto en todos los casos para revisar a la vez si es punto valido y su costo
    def __init__(self,cost:int,valid:bool,point:Read_data.Coord):
        self.cost=cost
        self.valid=valid
        self.point=point

class agente1:#left, forward
    def __init__(self,direction,position:Read_data.Coord,charact:Criaturas.character,Matrix:Read_data.Coord,user_flag:bool) -> None:
        self.direction=direction
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User
    def turn_left(self):#dirs: 1=-> 2=^ 3=<- 4=v
        if self.direction<3&self.direction>0:
            self.direction+1
        elif self.direction==4:
            self.direction=1
    def scan_forward(self,auto:bool)->cost_valid:#Censado #to DO
        valid_flag=True
        if self.direction==1:#apunta a la derecha
            X=self.position.Xcoordinate+1
            scanned_pos=various_methods.busq_point(self.Matrix,X,self.position.Ycoordinate)#Nos  retorna el objeto de la posicion a escanear
            cost=self.charact.cost(scanned_pos.Valor)#calculamos el costo de la siguiente casilla
            if cost==-1:
                valid_flag=False
                print("Not valid position")
            elif cost>0:  
                if not self.user_flag&(not self.auto):#not false=true, false=user: not true=false, true = pc, not auto=we see the data
                    print(scanned_pos.print_data(cost))#Interfaz grafica
                    opt=input("Do you want to move there?")#Esto se debe imprimir en la interfaz grafica
                elif self.user_flag|self.auto:
                    return cost

        elif self.direction==2:#Apunta hacia arriba
            Y=self.position.Ycoordinate+1
            scanned_pos=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,Y)#Nos  retorna el objeto de la posicion a escanear
            cost=self.charact.cost(scanned_pos.Valor)#calculamos el costo de la siguiente casilla
            if cost==-1:
                print("Not valid position")
            elif cost==0:
                print("You cannot move there")
            elif cost>0:  
                if not self.user_flag&(not self.auto):#not false=true, false=user: not true=false, true = pc, not auto=we see the data
                    print(scanned_pos.print_data(cost))#Interfaz grafica
                    opt=input("Do you want to move there?")#Esto se debe imprimir en la interfaz grafica
                elif self.user_flag|self.auto:
                    return cost


        elif self.direction==3:#Apunta a la izquierda
            X=self.position.Xcoordinate-1
            scanned_pos=various_methods.busq_point(self.Matrix,X,self.position.Ycoordinate)
            if cost==-1:
                print("Not valid position")
            elif cost==0:
                print("You cannot move there")
            elif cost>0:  
                if not self.user_flag&(not self.auto):#not false=true, false=user: not true=false, true = pc, not auto=we see the data
                    print(scanned_pos.print_data(cost))#Interfaz grafica
                    opt=input("Do you want to move there?")#Esto se debe imprimir en la interfaz grafica
                elif self.user_flag|self.auto:
                    return cost


        elif self.direction==4:#Apunta hacia abajo
            Y=self.position.Ycoordinate-1
            scanned_pos=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,Y)
            cost=self.charact.cols(scanned_pos.Valor)
            if cost==-1:
                print("Not valid position")
            elif cost==0:
                print("You cannot move there")
            elif cost>0:  
                if not self.user_flag&(not self.auto):#not false=true, false=user: not true=false, true = pc, not auto=we see the data
                    print(scanned_pos.print_data(cost))#Interfaz grafica
                    opt=input("Do you want to move there?")#Esto se debe imprimir en la interfaz grafica
                                                            #TO DO
                elif self.user_flag|self.auto:
                    return cost
            
                
    def move_forward(self,cost:int,movimientos:int)->bool:#dirs: 1=-> 2=^ 3=<- 4=v
        for casilla in range(movimientos):
            band=self.scan_forward(True)
            if band.valid:
                self.position=various_methods.assign_point(self.Matrix,band.point.Xcoordinate,band.point.position.Ycoordinate)
                cost=cost+band.cost
            else:
                return False
            return True

class Agente2:#left,rigth, forward
    def __init__(self,direction,position:Read_data.Coord,charact:Criaturas.character,Matrix:Read_data.Coord,user_flag:bool):
        self.direction=direction
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User

    def turn_left(self):
        if self.direction<3&self.direction>0:
            self.direction+1
        elif self.direction==4:
            self.direction=1
    def turn_rigth(self):
        if self.direction<5&self.direction>1:
            self.direction-1
        elif self.direction==1:
            self.direction=4
        
    def scan_forward(self,auto:bool)->cost_valid:#Censado
        validation=cost_valid(0,True,None)
        if self.direction==1:#apunta a la derecha
            X=self.position.Xcoordinate+1
            scanned_pos=various_methods.busq_point(self.Matrix,X,self.position.Ycoordinate)#Nos  retorna el objeto de la posicion a escanear
            cost=self.charact.cost(scanned_pos.Valor)#calculamos el costo de la siguiente casilla
            if cost==-1:
                print("Not valid position")
            elif cost>0:  
                if not self.user_flag&(not self.auto):#not false=true, false=user: not true=false, true = pc, not auto=we see the data
                    print(scanned_pos.print_data(cost))#Interfaz grafica
                    opt=input("Do you want to move there?")#Esto se debe imprimir en la interfaz grafica
                elif self.user_flag|self.auto:
                    validation.cost=cost
                    validation.point=scanned_pos
                    validation.valid=True#Guardamos el costo y si la casilla es valida
                    return validation

        elif self.direction==2:#Apunta hacia arriba
            Y=self.position.Ycoordinate+1
            scanned_pos=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,Y)#Nos  retorna el objeto de la posicion a escanear
            cost=self.charact.cost(scanned_pos.Valor)#calculamos el costo de la siguiente casilla
            if cost==-1:
                print("Not valid position")
            elif cost==0:
                print("You cannot move there")
            elif cost>0:  
                if not self.user_flag&(not self.auto):#not false=true, false=user: not true=false, true = pc, not auto=we see the data
                    print(scanned_pos.print_data(cost))#Interfaz grafica
                    opt=input("Do you want to move there?")#Esto se debe imprimir en la interfaz grafica
                elif self.user_flag|self.auto:
                    validation.cost=cost
                    validation.point=scanned_pos
                    validation.valid=True
                    return validation
                


        elif self.direction==3:#Apunta a la izquierda
            X=self.position.Xcoordinate-1
            scanned_pos=various_methods.busq_point(self.Matrix,X,self.position.Ycoordinate)
            if cost==-1:
                print("Not valid position")
            elif cost==0:
                print("You cannot move there")
            elif cost>0:  
                if not self.user_flag&(not self.auto):#not false=true, false=user: not true=false, true = pc, not auto=we see the data
                    print(scanned_pos.print_data(cost))#Interfaz grafica
                    opt=input("Do you want to move there?")#Esto se debe imprimir en la interfaz grafica
                elif self.user_flag|self.auto:
                    validation.cost=cost
                    validation.point=scanned_pos
                    validation.valid=True
                    return validation


        elif self.direction==4:#Apunta hacia abajo
            Y=self.position.Ycoordinate-1
            scanned_pos=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,Y)
            cost=self.charact.cols(scanned_pos.Valor)
            if cost==-1&self.auto:
                print("Not valid position")
            elif cost==0:
                print("You cannot move there")
            elif cost>0:  
                if not self.user_flag&(not self.auto):#not false=true, false=user: not true=false, true = pc, not auto=we see the data
                    print(scanned_pos.print_data(cost))#Interfaz grafica
                    opt=input("Do you want to move there?")#Esto se debe imprimir en la interfaz grafica
                elif self.user_flag|self.auto:
                    validation.cost=cost
                    validation.point=scanned_pos
                    validation.valid=True
                    return validation
            
                
    def move_forward(self,cost:int,key)->bool:#dirs: 1=-> 2=^ 3=<- 4=v
        band=self.scan_forward(True)
        if band.valid:#el escaneo ya nos da toda la informacion para usarla
            x=band.point.Xcoordinate
            y=band.point.Ycoordinate
            self.position.actual_flag=False
            self.position=various_methods.assign_point(self.Matrix,x,y)#soplo usamos esa informacion para
            cost=cost+band.cost                         #Para actualizar la posicion si es posible
            return True
        else:
            return False
                
            


class Agente3:#move one cell any direction
    def __init__(self,position:Read_data.Coord,charact:Criaturas.character,Matrix:Read_data.Coord,user_flag:bool):
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User
    def scan(self)->cost_valid:#Se tiene que implementar la opcion auto como en los otros agentes
        points=list()
        scan_result=list()
        Not_valid=list()
        already_visited=list()
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate))#x+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1))#y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate))#x-1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1))#y-1
        for x in points:
            if x.Valor>=0:
                if not x.visited_flag:
                    scan_result.append(cost_valid(self.charact.cost(x.Valor),True,x))
                else:
                    already_visited.append(x)
            elif x.Valor==-1:
                Not_valid.append(x)
        if len(scan_result)>0:
            if len(scan_result)>1:
                self.position.deci_flag=True
            return scan_result#Sí hay por lo menos un camino para seguir, aqui lo veremos
        elif len(already_visited)+len(Not_valid)==4:
            result=Read_data.Coord('Not valid', -1, -1, False, False,False)#  no hay a donde moverse y hay que regresar
            scan_result.append(cost_valid(0, False, result))
            return scan_result#so mp hay caminos disponibles 


     #These methods are for the movement       
    def scan_pos(self,direction)->cost_valid:#este solo lo usa el metodo move
        if direction==1:
            scanned=various_methods.busq_point(self.Matrix, self.position.Xcoordinate+1,self.position.Ycoordinate)
        elif direction==2:
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1)
        elif direction==3:
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate)
        elif direction==4:
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1)
        if scanned.Valor>0:
            valid=cost_valid(self.charact.cost(scanned.Valor),True,scanned)
        else:
            valid=cost_valid(0,False,scanned)
        return valid
            
            
    #pos-> d=->, w=^,a=<-,s=v: 1,2,3,4
    def move(self,key,cost):
      direction = arr[key]
      scannedpos=self.scan_pos(direction)#aqui directamente hacemos un auto escaneo
      var=self.scan_pos(direction)

      if var.valid:
        self.position=various_methods.assign_point(self.Matrix,var.point.Xcoordinate, var.point.Ycoordinate)
        cost=cost+var.cost
        return True
      return False
    


class Agente4:#move to any cell in column or row
    def __init__(self,position:Read_data.Coord,charact:Criaturas.character,Matrix:Read_data.Coord,user_flag:bool):
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User

    def scan(self,scan_result:Read_data.Coord)->cost_valid:#Se tiene que implementar la opcion auto como en los otros agentes
        points=list()
        scan_result=list()
        Not_valid=list()
        already_visited=list()
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate))#x+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1))#y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate))#x-1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1))#y-1
        for x in points:
            if x.Valor>=0:
                if not x.visited_flag:
                    scan_result.append(cost_valid(self.charact.cost(x.Valor),True,x))
                else:
                    already_visited.append(x)
            elif x.Valor==-1:
                Not_valid.append(x)
        if len(scan_result)>0:
            if len(scan_result)>1:
                self.position.deci_flag=True
            return scan_result#Sí hay por lo menos un camino para seguir, aqui lo veremos
        elif len(already_visited)+len(Not_valid)==4:
            result=Read_data.Coord('Not valid', -1, -1, False, False,False)#  no hay a donde moverse y hay que regresar
            scan_result.append(cost_valid(0, False, result))
            return scan_result#so mp hay caminos disponibles 

         #These methods are for the movement       
    def scan_pos(self,direction)->Read_data.Coord:#este solo lo usa el metodo move
        if direction==1:
            scanned=various_methods.busq_point(self.Matrix, self.position.Xcoordinate+1,self.position.Ycoordinate)
        elif direction==2:
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1)
        elif direction==3:
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate)
        elif direction==4:
            scanned=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1)
        if scanned.Valor>0:
            valid=cost_valid(self.charact.cost(scanned.Valor),True,scanned)
        else:
            valid=cost_valid(0,False,scanned)
        return valid
    
    arr={'d':1,'w':2,'a':3,'s':4}# key:value
    def move(self,key,cost,movimientos:int):
        direction = arr[key]
        for num in range(movimientos):#Necesitamos calcular todo para esta funcion con scan pos de arriba
            new=self.scan_pos(direction)
            
            if new.valid:
                self.position=various_methods.assign_point(self.Matrix,new.point.Xcoordinate, new.point.Ycoordinate)
                cost=cost+new.cost
                return True
            return False


class Agente5:#Move to any cell in any diagonal
    def __init__(self,position:Read_data.Coord,charact:Criaturas.character,Matrix:Read_data.Coord,user_flag:bool):
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.cost=0
        self.auto=False
        self.user_flag=user_flag#true=PC, false=User
    
    def scan_data(self)->Read_data.Coord:#escanea en diagonal
        points=list()
        scan_result=list()
        Not_valid=list()
        already_visited=list()
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate+1))#x+i,y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate-1))#y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate+1))#x-1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate-1))#y-1
        for x in points:
            if x.Valor>=0:
                if not x.visited_flag:
                    scan_result.append(cost_valid(self.charact.cost,True,x))
                else:
                    already_visited.append(x)
            elif x.Valor==-1:
                Not_valid.append(x)
        if len(scan_result)>0:
            if len(scan_result)>1:
                self.position.deci_flag=True
            return scan_result#Sí hay por lo menos un camino para seguir, aqui lo veremos
        elif len(already_visited)+len(Not_valid)==4:
            result=Read_data.Coord('Not valid', -1, -1, False, False,False)#  no hay a donde moverse y hay que regresar
            scan_result.append(cost_valid(0, False, result))
            return scan_result# no hay caminos disponibles 
      #    O O /        \ O O        O O O      O O O
      #1=D=O O O   2=W= O O O   3=A= O O O  4=S=O O O
      #    O O O        O O O        / O O      O O \}
      
    def self_scan(self,direction:int)->cost_valid:
            if direction==1:
                scann_res=various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate+1)#x+i,y+1)
            elif direction==2:
                scann_res=various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate+1) 
            elif direction==3:
                scann_res=various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate-1)
            elif direction==4:
                scann_res=various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate)
            valid=cost_valid(self.charact.cost(scann_res.Valor),True,scann_res)
            if scann_res.Valor>0:
                     valid=cost_valid(self.charact.cost(scann_res.Valor),True,scann_res)
            else:
                valid=cost_valid(0,False,scann_res)
            return valid
        
        
           
    def move(self,key,movimientos):
        direction=arr[key]
        for num in range(movimientos):
            new=self.self_scan(direction)

                
            
            
            
            
            
            
            
