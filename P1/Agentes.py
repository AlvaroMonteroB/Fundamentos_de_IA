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

class agente1:#Tenemos que cambiar para que se mueva en un numero continuo de casillas
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

class Agente2:
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
                
            


class Agente3:
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
        validation=cost_valid(0, valid, point)
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate))#x+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1))#y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate))#x-1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1))#y-1
        for x in points:
            if x.Valor>=0:
                if not x.visited_flag:
                    scan_result.append(cost_valid(charact.cost(x.Valor),True,x))
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

            
    #pos-> d=->, w=^,a=<-,s=v
    def move(self,key,cost):
      direction = arr[key]
      scannedpos=self.scan_pos(direction)#aqui directamente hacemos un auto escaneo
      new_pos=various_methods.busq_point(self.Matrix, scannedpos.Xcoordinate, scannedpos.Ycoordinate)

      if list_p.valid:
        self.position=various_methods.assign_point(self.Matrix,list_p.point.Xcoordinate, list_p.point.Ycoordinate)
        cost=cost+list_p.cost
        return True
      return false
    


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
        validation=cost_valid(0, valid, point)
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate))#x+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1))#y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate))#x-1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1))#y-1
        for x in points:
            if x.Valor>=0:
                if not x.visited_flag:
                    scan_result.append(cost_valid(charact.cost(x.Valor),True,x))
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
            scanned=various_methods.busq_point(self.Matrix, p.point.Xcoordinate+1, p.point.Ycoordinate)

    arr={'d':1,'w':2,'a':3,'s':4}# key:value
    def move(self,key,cost,movimientos:int):
        for num in range(movimientos):#Necesitamos calcular todo para esta funcion con scan pos de arriba
            direction = arr[key]
            if list_p.valid:
                self.position=various_methods.assign_point(self.Matrix,list_p.point.Xcoordinate, list_p.point.Ycoordinate)
                cost=cost+list_p.cost
                return True
            return false


class Agente5:
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
        validation=cost_valid(0, valid, point)
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate+1))#x+i,y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate-1))#y+1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate+1))#x-1
        points.append(various_methods.busq_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate-1))#y-1
        for x in points:
            if x.Valor>=0:
                if not x.visited_flag:
                    scan_result.append(cost_valid(charact.cost,True,x))
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
      #    O O /        \ O O        O O O      O O O
      #1=D=O O O   2=W= O O O   3=A= O O O  4=S=O O O
      #    O O O        O O O        / O O      O O \
      def self_scan(self):

                 
                
           

                
            
            
            
            
            
            
            

      