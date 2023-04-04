import Read_data
import Agentes
import Criaturas


def terrain_info(punto,ente):
    punto.print_data(ente.cost)
    return 

def busq_point(Matrix:Read_data.Coord,X:int,Y:int)-> Read_data.Coord:#busca el punto entre nuestra matriz de objetos para devolverlo
    if X < 0 or Y < 0 or X >= len(Matrix) or Y >= len(Matrix[0]):
        return Read_data.Coord("-1", -1, -1, False, False, False, False)
    Matrix[Y][X].seen_flag=True
    output=Matrix[Y][X]
    return output
    

def assign_point(Matrix:Read_data.Coord,X:int,Y:int, orig_pos:Read_data.Coord):
    ver=busq_point(Matrix,X,Y)
    if ver.seen_flag:
        Matrix[Y][X].visited_flag=True#Y1->X...
        Matrix[Y][X].actual_flag=True #Y2->X...
        Matrix[Y][X].seen_flag=True   #Y3->X...
        output=Matrix[Y][X]
        return output
    return orig_pos


