import Read_data
import Criaturas
import various_methods
class agente1:
    def __init__(self,direction,position:Read_data.Coord,charact:Criaturas.character,Matrix:Read_data.Coord,user_flag:bool) -> None:
        self.direction=direction
        self.position=position
        self.charact=charact
        self.Matrix=Matrix
        self.user_flag=user_flag#true=PC, false=User
    def turn_left(self):#dirs: 1=-> 2=^ 3=<- 4=v
        if self.direction<3&self.direction>0:
            self.direction+1
        elif self.direction==4:
            self.direction=1
    def scan_forward(self):#Censado
        if self.direction==1:
            X=self.position.Xcoordinate+1
            scanned_pos=various_methods.busq_point(self.Matrix,X,self.position.Ycoordinate)#Nos  retorna el objeto de la posicion a escanear
            scanned_pos.seen_flag=True
            cost=charact.cost(scanned_pos.Valor)
            if not self.user_flag:#not false=true, false=user: not true=false, true = pc
                print(scanned_pos.print_data(cost))
                opt=input("Do you want to move there?")
                
            
            
            
            
            
            
            

      