import file_handler as fh
import numpy as np



class obj:
    def __init__(self,name:str,lista:list): #Tiene que ser una lista de listas, RECIBIMOS los datos de la clase, al final solo se usan los contables
        self.name=name
        self.data=lista
        self.contable=list()
        

    def promedios(self):
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

    def max_min_mean(self):
        self.medidas=list()#Lista de promedios, un promedio por cada campo que sea contable(int o float)
        for i in range(len(self.data[0])):#Vamos a recorrer por columnas primero
            #Es donde vamos a guardar los datos antes de hacerles push a las medidas por cada columna
            if isinstance(self.data[0][i], int)  or isinstance(self.data[0][i], float):#Si es float o int, lo vamos a usar
                aux=list()
                for renglon in self.data:
                    aux.append(renglon[i])
                arraux=np.array(aux)
                max,min,mean=np.max(arraux),np.min(arraux),np.mean(arraux)
                tupaux=(max,min,mean)
                self.medidas.append(tupaux)
            else:
                continue


            
    def get_distinct(self,col:int):
        distinct_names=[]
        seen=set()
        for row in self.archivo:
            if row[col] not in seen:
                distinct_names.append(row[col])
                seen.add(row[col])
        return distinct_names

    def get_contable_vals(self):#Devolverá el indice de los valores
        for i in range(self.data[0]):
            if isinstance(self.data[0][i],int) or isinstance(self.data[0][i],float):
                self.contable.append(i)
            else:
                continue

                




        