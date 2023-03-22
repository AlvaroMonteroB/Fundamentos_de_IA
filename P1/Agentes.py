import Read_data
import Criaturas
class agente1:
    def __init__(self,direction,position:Read_data.Coord,charact:Criaturas.character) -> None:
        self.direction=direction
        self.position=position
        self.charact=charact
    def turn_left(self):#dirs: 1=-> 2=^ 3=<- 4=v
        if self.direction<3&self.direction>0:
            self.direction+1
        elif self.direction==4:
            self.direction=1
    def scan_forward(self):#Censado
        if self.direction==1:
            scan_pos=self.position
            
            
            
            
            
            

      