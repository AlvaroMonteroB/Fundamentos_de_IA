import file_handler as fh
import os
import estatistics as stt
import knn

def cls():
    os.system('cls' if os.name=='nt'else 'clear')


path=input("Introduce el path de tu archivo\n")
dataset=fh.file_handler(path)
condition=True
fields=list()
a=input("Quieres hacer auto detect de los campos?  1.-Si    0.-No\n")
if  a=='0':
    while condition:
        print(dataset.archivo[0])
        for i in range(dataset.campos):
            aux=input("Introduce campo "+str(i+1)+" ||  int=1, float=2, str=3, bool=4\n")
            fields.append(int(aux))
            cls()
        if dataset.set_fields(fields):
            condition=False
        else:
            print("Intrduce campos validos\n")
else:
    dataset.auto_set()#Se settean los datos a un tipo especifico
    
opt=int(input("Introduce la columna de la clase(empezando de 0 la de la izquierda)\n"))
clases=dataset.get_distinct(opt)

newMatrix=dataset.get_rows(0,dataset.pattern-1)

objetos=[]
for nombre in clases:
    filtered_matrix=[]
    for row in newMatrix:
        if row[opt] == nombre:
            filtered_matrix.append(row)
    objetos.append(stt.obj(nombre,filtered_matrix))

for clase in objetos:
    print("Nombre "+clase.name)
    names=None
    for i,col in enumerate(clase.data[0]):#en las columnas
        if isinstance(col,str) and not i==opt:
            names=clase.get_distinct(i)
            
            for j,name in enumerate(names):
                print(str(j))
                print

    
    clase.max_min_mean()
    tuplas=clase.medidas
    for i,tupla in enumerate(tuplas):
        min,max,mean=tupla
        print(str(i)+" min= "+str(min)+" max= "+str(max)+" mean= "+str(mean))
        
    pattern=5.2,3.2,5.4,2
    nearest=knn.knn(pattern,3,clase,opt)
    print("Patrones mas cercanos")
    for nn in nearest:
        print(nn[1])
    
       










"""
    for i in range(len(dataset.archivo)):
        for j in range(dataset.campos):
            if isinstance(self.data[i][j],int) or isinstance(self.data[i][j],float):#Si es int o float
                if dataset.archivo[opt]==nombre:
                    lista.append(dataset.get_cell(i,))"""


    




