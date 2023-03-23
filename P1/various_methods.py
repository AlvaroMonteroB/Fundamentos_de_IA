import Read_data
import Agentes
import Criaturas


def terrain_info(punto,ente):
    punto.print_data(ente.cost)
    return 

def busq_point(Matrix:Read_data.Coord,X:int,Y:int)-> Read_data.Coord:#busca el punto entre nuestra lista de objetos para devolverlo
    for obj in Matrix:#iteramos objeto en la matriz
        if obj.Ycoordinate==Y&obj.Xcoordinate==X:
            output=obj
    if output:#Si encontró punto, la variable output va a existir
        output.seen_flag=True
        return output
    elif not output:#En caso de no estar dentro del mapa, se lanza un punto no válido
        output=Read_data.Coord('Not valid', -1, -1, False, False)
        return output
    

def assign_point(Matrix:Read_data.Coord,X:int,Y:int):
    for obj in Matrix:#iteramos objeto en la matriz
        if obj.Ycoordinate==Y&obj.Xcoordinate==X:
            output=obj
    output.visited_flag=True
    output.seen_flag=True
    return output