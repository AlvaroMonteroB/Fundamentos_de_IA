# 0=montaña, 1 tierra, 2 agua, 3 arena, 4 bosque, 5 pantano
data_terrain={0:"Montaña", 1:"Tierra", 2:"Agua",3:"Arena",4:"Bosque",5:"Pantano"}


class Coord():
    
    def __init__(self,Valor:str,Xcoordinate:int,Ycoordinate:int,visited_flag:bool(),seen_flag:bool()):#Para cada casilla se podrá tener este objeto
        self.Valor=Valor                                           #que define su posición y si ya ha sido visitad
        self.Xcoordinate=Xcoordinate                               #Al igual que el valor de la casilla
        self.Ycoordinate=Ycoordinate
        self.visited_flag=visited_flag     #Probablemente tengamos que añadir si se toma una desicion
        self.seen_flag=seen_flag
    def print_data(self,cost):
        print("Data of point "+self.Xcoordinate+","+self.Ycoordinate)
        print("El terreno es "+data_terrain[self.Valor]+" Tiene un costo de "+cost+" Esta casilla")

def read_matrix():
    Matrix_rows=list()
    Matrix_rows1=list()
    with open("matriz.txt","r") as Read_matrix:
        leer=Read_matrix.readline
        for line in Read_matrix:
            Matrix_rows.append(line)
        Read_matrix.close
                                        #Lectura y remplazo de comas en el archiv
    print("Read successfully")
    for linea in Matrix_rows:
        aux=linea.replace(',','')
        aux=aux.strip()
        Matrix_rows1.append(aux)#Arreglo de renglones sin comas y sin saltos de linea

    for line in Matrix_rows1:
        print(line)

    puntos=list()


    for indice,cadena in enumerate(Matrix_rows1):      #Vamos a agregar los puntos y su valor
        for indice2,letra in enumerate(cadena):             #especificando todos los puntos como no visitados
            puntos.append(Coord(letra,indice2,indice,False,False))
    return puntos


        
def access_obj(cols,rows,Mat_obj:Coord):#Hay que modificar este
    line=Mat_obj[rows-1]
    return line[cols-1]

