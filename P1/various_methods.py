import Read_data
import Agentes
import Criaturas


def terrain_info(punto,ente):
    punto.print_data(ente.cost)
    return 

def busq_point(Matrix:Read_data.Coord,X:int,Y:int)-> Read_data.Coord:#busca el punto entre nuestra matriz de objetos para devolverlo
    output=Read_data.Coord('',-1,-1,False,False,False,False)
    if X < 0 or Y < 0 or X >= len(Matrix) or Y >= len(Matrix[0]):
        return Read_data.Coord('Not valid', -1, -1, False, False, False, False)
    Matrix[X][Y].seen_flag=True
    output=Matrix[X][Y]
    return output
    

def assign_point(Matrix:list[Read_data.Coord],X:int,Y:int):
    
    Matrix[X][Y].visited_flag=True
    Matrix[X][Y].actual_flag=True
    Matrix[X][Y].seen_flag=True
    output=Matrix[X][Y]
    return output