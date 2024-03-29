import csv
class file_handler:
    def __init__(self,path):
        with open(path,'r') as f:
            self.archivo=list(csv.reader(f))
            f.close()
        self.campos=len((self.archivo[0]))#Numero de columnas
        self.pattern=len(self.archivo)#numero de filas

    def set_fields(self,type_list):#Una lista que guarda que tipo va a ser cada campo
            if len(type_list)==self.campos and (1 in type_list or 2 in type_list or 3 in type_list or 4 in type_list):
                self.type_list=type_list
                return True
            else: 
                return False


    def auto_set(self):
        types=list()
        aux=self.archivo[0]
        for column,i in zip(aux,range(len(aux))):
            if '.' in column:
                types.append(2)
            elif column.isdigit():
                count=0
                for col in self.archivo:#Vamos a determinar si es bool
                    if col[i]!=0 and  col[i]!=1:
                        count=+1
                        if count>0:
                            break
                if count==0:
                    types.append(4)
                else:
                    types.append(1)
            else:
                types.append(3)
        self.type_list=types

    def set_class(self,col):
        if 0<=col<=self.campos:
            self.clase=col
        else:
            print("class not set")

    def detect_different_classes(self):#Detectar cuantos tipos de diferentes clases hay
        self.type_class=list()
        for row in self.archivo:#columnas en archivo
            if not (row[self.clase] in self.clases):#si row[iterador de clase] no está en clases(lista de las diferentes clases)
               self.type_class.append(row[self.clase])#Si no está, agregamos la siguiente clase
            else:
                continue

            

    def get_cell(self, iterador, posicion:int):#Hacer un select directo a una celda, iterador es para filas y pos para columnas
        if iterador<self.pattern and iterador>=0 and posicion<self.campos and posicion>=0 and self.type_list!=None:
            return switch_type[self.type_list[posicion]](self.archivo[iterador])
        else:
            return None
    
    def get_row(self,iterador):#Devuelve el renglon pero con los cast adecuados
        if iterador<self.pattern and iterador>=0 and self.type_list!=None:
            aux= self.archivo[iterador]
            row=list()
            for i in range(self.pattern):
                row.append(switch_type[self.type_list[i]](aux[i]))    #Mandamos a la lista el dato y su cast al tipo que es            
        else:
            return None
        return row
    
    def get_rows(self,ini=0,fin=None):
        if not fin:
            fin=self.pattern-1
        if ini<fin and ini<self.pattern-1 and ini>=0 and self.type_list!=None and fin<=self.pattern:
            rows=list()
            for it in range(ini,fin,1):#Iterador de 1 en 1
                aux=self.archivo[it]#aux itera en las filas del csv
                row=list()
                for i in range(self.campos):#Tengo que cambiarlo para que no proporcione la informacion de la clase
                    row.append(switch_type[self.type_list[i]](aux[i]))
                rows.append(row)
            return rows

    def get_distinct(self,col:int):
        distinct_names=[]
        seen=set()
        for row in self.archivo:
            if row[col] not in seen:
                distinct_names.append(row[col])
                seen.add(row[col])
        return distinct_names
    


switch_type={
    1:int,
    2:float,
    3:str,
    4:bool
}


