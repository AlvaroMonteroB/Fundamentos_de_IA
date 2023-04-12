
# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
data_terrain={0:"Montaña", 1:"Tierra", 2:"Agua",3:"Arena",4:"Bosque",5:"Pantano"}


class Coord():
    
    def __init__(self,Valor:str,Xcoordinate:int,Ycoordinate:int,visited_flag:bool,seen_flag:bool,deci_flag:bool,actual_flag:bool):#Para cada casilla se podrá tener este objeto
        self.Valor=Valor                                           #que define su posición y si ya ha sido visitad
        self.Xcoordinate=Xcoordinate                               #Al igual que el valor de la casilla
        self.Ycoordinate=Ycoordinate
        self.visited_flag=visited_flag     
        self.seen_flag=seen_flag
        self.deci_flag=deci_flag #Bandera para ver si se ha tomado una desicion
        self.actual_flag=actual_flag
    def print_data(self,cost):
        print("Data of point "+str(self.Xcoordinate)+","+str(self.Ycoordinate))
        print("El terreno es "+data_terrain[self.Valor]+" Tiene un costo de "+cost+" Esta casilla")

def read_matrix(puntos:list[Coord])->None:
    Matrix_rows=list()
    Matrix_rows1=list()
    list_aux=list()
    with open("map.txt","r") as Read_matrix:
        leer=Read_matrix.readline
        for line in Read_matrix:
            Matrix_rows.append(line)
        Read_matrix.close()
                                        #Lectura y remplazo de comas en el archiv
    print("Read successfully")
    for linea in Matrix_rows:
        aux=linea.replace(',','')#cadena sin comas
        aux=aux.strip()
        Matrix_rows1.append(aux)#Arreglo de renglones sin comas y sin saltos de linea
    for i, fila in enumerate(Matrix_rows1):#i es el enumerado, fila es el contenido de las rows de la matriz
        puntos_fila = []
        for j, letra in enumerate(fila):
            coord = Coord(letra, j, i, False, False, False, False)
            puntos_fila.append(coord)
        puntos.append(puntos_fila)

    """for rows in puntos:#Primero van los Y y luego los X
        for cols in rows:
            print("("+str(cols.Xcoordinate)+','+str(cols.Ycoordinate)+')'+cols.Valor, end=' ')
        print('\n')"""

        
    return

        
def access_obj(cols,rows,Mat_obj:Coord):#Hay que modificar este
    return Mat_obj[rows][cols]

