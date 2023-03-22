import Read_data
class agente1:
    def __init__(self,direction,position) -> None:
        self.direction=direction
        self.position=position
    def turn_left(self):#dirs: 1=-> 2=^ 3=<- 4=v
        if self.direction<3&self.direction>0:
            self.direction+1
        elif self.direction==4:
            self.direction=1
    def advance_forward(self):
        
            
            
            
            
def point_validation(mat_point,n_position):
        Read_data.access_obj(n_position[0],n_position[1])
    
        
        