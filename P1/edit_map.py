from tkinter import *
import Read_data as rd
import various_methods as vm
import sys

class Agente_edit:
    def __init__(self,Matrix):
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
    def update_pos():
        if -1<ter_num[Agente.position.Valor]<5:
         Agente.position.Valor=terrain_switch[ter_num[Agente.position.Valor]+1]
         Matrix[Agente.position.Ycoordinate][Agente.position.Xcoordinate]=Agente.position
        elif ter_num[Agente.position.Valor]==5:
            Agente.position.Valor=terrain_switch[0]
        update_window(canvas,Matrix,Agente.position,text)
    
    def pressUp():
        Agente.up()
        update_window(canvas,Matrix,Agente.position,text)


    def pressDown():
        Agente.down()
        update_window(canvas,Matrix,Agente.position,text)

    def pressLeft():
        Agente.left()
        update_window(canvas,Matrix,Agente.position,text)

    def pressRight():
        Agente.right()
        update_window(canvas,Matrix,Agente.position,text)

    def pressDone():
        update_file(Matrix)
        update_window(canvas,Matrix,Agente.position,text)
        ventana.destroy()
    
                
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

    text=Canvas(ventana,width=150,height=100,bg="#FDF6FF")
    text.pack(side=LEFT)
    text.create_text((1,7),text=str(Agente.position))

    up = Button(ventana, text="arriba", command=pressUp)
    up.pack(side=TOP, padx=20)

    right = Button(ventana, text="Derecha", command=pressRight)
    right.pack(side=TOP, padx=20)

    left = Button(ventana, text="Izquierda", command=pressLeft)
    left.pack(side=TOP, padx=20)

    down = Button(ventana, text="abajo", command=pressDown)
    down.pack(side=TOP, padx=20)

    done=Button(ventana,text="Hecho", command=pressDone)
    done.pack(side=RIGHT,padx=20)
    
    update=Button(ventana,text="Act pos",command=update_pos)
    update.pack(side=LEFT,padx=20)

    ventana.mainloop()




def update_window(canvas,Matrix,act_pos,text):
    list = Matrix
    a = len(list)
    length = 500//a
    canvas.delete("all")
    list = Matrix
    a = len(list)
    length = 500//a
    canvas.pack(side=LEFT,padx=50)
    for i in range(a):
        y = i * length
        for j in range(a):
            x = j * length
            terrain=list[i][j]
            if terrain==act_pos:
                color="#FFFFFF"
            else:
                color=visited_switch[terrain.Valor]
            canvas.create_rectangle(x, y, x+length, y+length, fill=color)
    text.delete("all")
    text.pack(side=LEFT)
    text.create_text((1,7),text=str(act_pos))
    canvas.update()
    text.update()




def update_file(Matrix:rd.Coord):
    with open("matriz.txt",'w',encoding="utf-8") as f:
        for J in range(len(Matrix)):
            for I in range(len(Matrix[0])):
                terreno=Matrix[J][I]
                if I<len(Matrix[0])-1 :
                    f.write(terreno.Valor+',')
                else:
                    f.write(terreno.Valor+'\n')
    f.close()
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


terrain_switch={#Numero a terreno
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5'
}

ter_num={#Terreno a numero
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5
}