import file_handler as fh

class prom_index:
    def __init__(self,prom,index):
        self.prom=prom
        self.index=index


class obj:
    def __init__(self,name:str,lista:list): #Tiene que ser una lista de listas, RECIBIMOS los datos de la clase, al final solo se usan los contables
        self.name=name
        self.data=lista
        self.prom() 

    def prom(self):
        self.prom=list()#Lista de promedios, un promedio por cada campo que sea contable(int o float)
        for i in range(len(self.data[0])):#Vamos a recorrer por columnas primero
            if isinstance(self.data[0][i], int)  or isinstance(self.data[0][i], float):#Si es float o int, lo vamos a usar
                aux=0
                for renglon in self.data:#Luego cada renglon
                    aux+=renglon[i]
                self.prom.append(aux/len(self.data[0]))
                aux=None
            else:
                continue


    def get_contable_vals(self):#Devolverá el indice de los valores
        self.contable=list()
        for i in range(self.data[0]):
            if isinstance(self.data[0][i],int) or isinstance(self.data[0][i],float):
                self.contable.append(i)
            else:
                continue

                




        