import file_handler as fh
import os

def cls():
    os.system('cls' if os.name=='nt'else 'clear')


path=input("Introduce el path de tu archivo\n")
dataset=fh.file_handler(path)
condition=True
fields=list()
a=input("Quieres hacer auto detect de los campos?  1.-Si    0.-No")
if not a:
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
    dataset.auto_set()



