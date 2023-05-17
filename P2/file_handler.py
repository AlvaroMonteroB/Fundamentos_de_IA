import csv
class file_handler:
    def __init__(self,path):
        with open(path,'r') as f:
            self.archivo=list(csv.reader(f))
            f.close()
        self.campos=len((self.archivo[0]))#Numero de columnas
        self.pattern=len(list(self.archivo))#numero de filas

    def set_fields(self,type_list):#Una lista que guarda que tipo va a ser cada campo
            if len(type_list)==self.campos:
                self.type_list=type_list
                return True
            else: 
                return False
    

    def get_cell(self, iterador, posicion:int):
        if iterador<self.pattern and iterador>=0 and posicion<self.campos and posicion>=0 and self.type_list!=None:
            return switch_type[self.type_list[posicion]](self.archivo[iterador])
        else:
            return None
    
    def get_row(self,iterador):
        if iterador<self.pattern and iterador>=0 and self.type_list!=None:
            aux= self.archivo[iterador]
            row=list()
            for i in range(aux):
                row.append(switch_type[self.type_list[posicion]](aux[i]))                
        else:
            return None



switch_type={
    1:int,
    2:float,
    3:str
}


