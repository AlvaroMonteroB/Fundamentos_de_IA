import csv
class file_handler:
    def __init__(self,path):
        with open(path,'r') as f:
            self.archivo=csv.reader(f)
            f.close()
        self.campos=len(next(self.archivo))#Numero de columnas
        self.pattern=len(list(self.archivo))#numero de filas

    def set_fields(self,type_list):#Una lista que guarda que tipo va a ser cada campo
            if len(type_list)==self.campos:
                self.type_list=type_list
    

    def get_cell(self, iterador, posicion:int):
        if iterador<self.pattern and iterador>=0 and posicion<self.campos and posicion>=0:
            return switch_type[self.type_list[posicion]](self.archivo[iterador])
        else:
            return None



switch_type={
    1:int,
    2:float,
    3:str
}


