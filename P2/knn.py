import estatistics as stt



def knn(pattern,k:int,clases:stt.obj,class_id:int):
    distancias=list()
    for data in clases.data:#Para operar por renglon
        dist=0
        for field in clases.contable:#para iterar en los campos contables
            dist=+(pattern[field]-data[field])**2 
        distancias.append(((dist**1/2),data[class_id]))#tupla con la distancia y el nombre del patron
        distancias.sort()
        k_nearest=distancias[:k]
    return k_nearest
    