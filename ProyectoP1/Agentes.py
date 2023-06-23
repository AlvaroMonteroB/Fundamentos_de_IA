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
            if cos>0:#Si el valor de la posicion es valido, entramos
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
    




            
            

            
switch={
    3:Agente3,

}  
            
            
