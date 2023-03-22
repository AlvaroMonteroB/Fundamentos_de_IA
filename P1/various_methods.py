import Read_data
import Agentes
import Criaturas


def terrain_info(punto,ente):
    punto.print_data(ente.cost)
    return 

def busq_point(Matrix:Read_data.Coord,X:int,Y:int):
    i=0
    for obj in Matrix:
        if obj.Ycoordinate==Y&obj.Xcoordinate==X:
            output=obj
    return obj