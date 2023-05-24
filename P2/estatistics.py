import file_handler as fh



class obj:
    def __init__(self,name:str,lista:list): #Tiene que ser una lista de listas, RECIBIMOS los datos de la clase, al final solo se usan los contables
        self.name=name
        self.data=lista
        self.prom() 
    def prom(self):
        self.prom=list()#Lista de promedios, un promedio por cada campo que sea contable(int o float)
        for i in range(len(self.data[0])):#Vamos a recorrer por columnas primero
            aux=0
            for renglon in self.data:#Luego cada renglon
                aux+=renglon[i]
            self.prom.append(aux/len(self.data[0]))
            aux=None
                




        