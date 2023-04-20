from tkinter import *
import Read_data as rd
import various_methods as vm
import sys

class Agente_edit:
    def __init__(self,Matrix,position):
        self.Matrix=Matrix
        self.position=vm.assign_point(Matrix,0,0,Matrix[0][0]) 
    def up(self):
        self.position=vm.assign_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate-1,self.position)
    def right(self):
        self.position=vm.assign_point(self.Matrix,self.position.Xcoordinate+1,self.position.Ycoordinate,self.position)
    def left(self):
        self.position=vm.assign_point(self.Matrix,self.position.Xcoordinate-1,self.position.Ycoordinate,self.position)
    def down(self):
        self.position=vm.assign_point(self.Matrix,self.position.Xcoordinate,self.position.Ycoordinate+1,self.position)

def most_map(Matrix,Agente:Agente_edit):

    
    def pressUp():
        Agente.up()
        update_window(canvas,Matrix,Agente.position)

        

    def pressDown():
        Agente.down()
        update_window(canvas,Matrix,Agente.position)

    def pressLeft():
        Agente.left()
        update_window(canvas,Matrix,Agente.position)

    def pressRight():
        Agente.right
        update_window(canvas,Matrix,Agente.position)
                
    list = Matrix
    a = len(list)
    length = 500//a

    ventana = Tk()
    ventana.title("Mapa")
    ventana.geometry("850x600")
    ventana.configure(bg="#FDF6FF")
    canvas = Canvas(ventana, width=500, height=500, bg="#FDF6FF")
    canvas.pack(side=LEFT,padx=50)
    for i in range(a):
        y = i * length
        for j in range(a):
            x = j * length
            terrain=list[i][j]
            color=visited_switch[terrain.Valor]
            canvas.create_rectangle(x, y, x+length, y+length, fill=color)

    up = Button(ventana, text="arriba", command=pressUp)
    up.pack(side=TOP, padx=20)

    right = Button(ventana, text="Derecha", command=pressRight)
    right.pack(side=TOP, padx=20)

    left = Button(ventana, text="Izquierda", command=pressLeft)
    left.pack(side=TOP, padx=20)

    down = Button(ventana, text="abajo", command=pressDown)
    down.pack(side=TOP, padx=20)
    ventana.mainloop()




def update_window(canvas,Matrix,act_pos):
    list = Matrix
    a = len(list)
    length = 500//a
    canvas.delete("all")
    list = Matrix
    a = len(list)
    length = 500//a
    ventana = Tk()
    ventana.title("Mapa")
    ventana.geometry("850x600")
    ventana.configure(bg="#FDF6FF")
    canvas = Canvas(ventana, width=500, height=500, bg="#FDF6FF")
    canvas.pack(side=LEFT,padx=50)
    for i in range(a):
        y = i * length
        for j in range(a):
            x = j * length
            terrain=list[i][j]
            color=visited_switch[terrain.Valor]
            canvas.create_rectangle(x, y, x+length, y+length, fill=color)


def update_file(Matrix:rd.Coord):
    with open("matrix.tx",'w',encoding="utf-8") as f:
        sys.stdout=f
    for J in len(Matrix):
        for I in len(Matrix[0]):
            terreno=Matrix[J][I]
            if I<len(Matrix[0]):
                print(terreno.Valor+',')
            else:
                print(terreno.Valor+'\n')
    sys.stdout = sys.__stdout__
    return




def edit():
    MatriX=[]
    rd.read_matrix(MatriX)
    Agente=Agente_edit(MatriX)
    most_map(MatriX,Agente)

 

visited_switch={
    '0':"#57605A",
    '1':"#5D370F",
    '2':"#06ACEE",
    '3':"#E2C58B",
    '4':"#00C606",
    '5':"#830EC6"
}