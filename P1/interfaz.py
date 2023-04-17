from tkinter import *
import numpy as np
import Read_data as rd
import Agentes as ag
import various_methods as vm
## creo que se puede optimizar si cambiamos la forma en la que llamamos las funciones
def mapaR(Matrix:rd.Coord,jugador:bool,fin_pos:rd.Coord,ini_pos:rd.Coord,stack:rd.Coord): ##le cambie el nombre porque agregué otras funciones dependiendo de lo que se está haciendo en ese momento 

    list = Matrix
    a = len(list)
    length = 500//a

    ventana = Tk()
    ventana.title("Mapa")
    ventana.geometry("850x600")
    ventana.configure(bg="#FDF6FF")

    canvas = Canvas(ventana, width=500, height=500, bg="#FDF6FF")
    canvas.pack(side=LEFT,padx=50)
    if stack:#Aqui imprimimos la solucion 
        for i in range(a):
            y = i * length
            for j in range(a):
                x = j * length
                terrain=list[i][j]
                if not terrain.seen_flag:#Si no lo hemos visto lo pasamos a negro
                    color="#000000"
                elif terrain.visited_flag:
                    if terrain==fin_pos:
                        color="#FF0000"
                    elif terrain==ini_pos:
                        color="#0000FF"
                    elif terrain in stack:
                        color=path_swich[terrain.Valor]
                    else:
                        color=visited_switch[terrain.Valor]
                elif terrain.seen_flag and not terrain.visited_flag:
                    color=only_seen_switch[terrain.Valor]
                canvas.create_rectangle(x, y, x+length, y+length, fill=color)
    else:#Si no hubo solucion, mostramos que lugares visitó
          for i in range(a):
            y = i * length
            for j in range(a):
                x = j * length
                terrain=list[i][j]
                if not terrain.seen_flag:#Si no lo hemos visto lo pasamos a negro
                    color="#000000"
                elif terrain.visited_flag:
                    if terrain==fin_pos:
                        color="#FF0000"
                    elif terrain==ini_pos:
                        color="#0000FF"
                    else:
                        color=visited_switch[terrain.Valor]
                elif terrain.seen_flag and not terrain.visited_flag:
                    color=only_seen_switch[terrain.Valor]
                canvas.create_rectangle(x, y, x+length, y+length, fill=color)
                
    Fx = fin_pos.Xcoordinate # Agrega la x en el punto final
    Fy = fin_pos.Ycoordinate
    canvas.create_text(((Fx+.5)*length,(Fy+.5)*length), text="X")

    Ix = ini_pos.Xcoordinate # Agrega la O en el punto inicial
    Iy = ini_pos.Ycoordinate
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="O")

    ventana.mainloop()

######################################################

def BAg1(Matrix:rd.Coord,jugador:bool,fin_pos:rd.Coord,ini_pos:rd.Coord,Agente:ag.agente1):#Botones Agente 1
    stack=[]
    stack.append(Agente.position)
    def pressA(): #aqui es donde quiero hacer prubas para agregar las funciones y ver como cambia en la tabla pero aun estoy investigando como actualizarla o con el delay
        Agente.move_forward(0,1)
        Agente.scan_forward(True) 
        stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
        if Agente.position==fin_pos:
            ventana.after(7000,ventana.destroy())
        
    def pressG():
        Agente.turn_left()
        Agente.scan_forward(True)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
        
    def PressRet():
        stack.pop()
        Agente.position=vm.assign_point(Matrix,stack[-1].Xcoordinate,stack[-1].Ycoordinate,stack[-1])
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
    
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
            if not terrain.seen_flag:#Si no lo hemos visto lo pasamos a negro
                color="#000000"
            elif terrain.visited_flag:
                if terrain==fin_pos:
                    color="#FF0000"
                elif terrain==ini_pos:
                    color="#0000FF"
                else:
                    color=visited_switch[terrain.Valor]
            elif terrain.seen_flag and not terrain.visited_flag:
                color=only_seen_switch[terrain.Valor]
            canvas.create_rectangle(x, y, x+length, y+length, fill=color)

    Fx = fin_pos.Xcoordinate # Agrega la x en el punto final
    Fy = fin_pos.Ycoordinate
    canvas.create_text(((Fx+0.5)*length,(Fy+0.5)*length), text="X")

    Ix = ini_pos.Xcoordinate # Agrega la O en el punto inicial
    Iy = ini_pos.Ycoordinate
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="O")

    avance = Button(ventana, text="avance", command=pressA)
    avance.pack(side=RIGHT, anchor=CENTER, padx=20)

    giro = Button(ventana, text="giro", command=pressG)
    giro.pack(side=RIGHT, anchor=CENTER, padx=20)
    
    retorno=Button(ventana,text="Regresar",command=PressRet)
    retorno.pack(side=RIGHT,anchor=CENTER,padx=20)
    
    ventana.mainloop()
def BAg2(Matrix:rd.Coord,jugador:bool,fin_pos:rd.Coord,ini_pos:rd.Coord,Agente:ag.Agente2):#Botones Agente 2
    stack=[]
    stack.append(Agente.position)
    def pressA():
        Agente.move_forward(0)
        Agente.scan_forward(True)
        stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos)

    def pressR():
        print("boton giroR")

    def pressL():
        print("boton giroL")
    
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
            if not terrain.seen_flag:#Si no lo hemos visto lo pasamos a negro
                color="#000000"
            elif terrain.visited_flag:
                if terrain==fin_pos:
                    color="#FF0000"
                elif terrain==ini_pos:
                    color="#0000FF"
                else:
                    color=visited_switch[terrain.Valor]
            elif terrain.seen_flag and not terrain.visited_flag:
                color=only_seen_switch[terrain.Valor]
            canvas.create_rectangle(x, y, x+length, y+length, fill=color)

    Fx = fin_pos.Xcoordinate # Agrega la x en el punto final
    Fy = fin_pos.Ycoordinate
    canvas.create_text(((Fx+0.5)*length,(Fy+0.5)*length), text="X")

    Ix = ini_pos.Xcoordinate # Agrega la O en el punto inicial
    Iy = ini_pos.Ycoordinate
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="O")

    avance = Button(ventana, text="avance", command=pressA)
    avance.pack(side=RIGHT, padx=20)

    giroR = Button(ventana, text="GDerecha", command=pressR)
    giroR.pack(side=RIGHT, padx=20)
    giroL = Button(ventana, text="GIzquierda", command=pressL)
    giroL.pack(side=RIGHT, padx=20)
    ventana.mainloop()

def BAg34(Matrix:rd.Coord,jugador:bool,fin_pos:rd.Coord,ini_pos:rd.Coord):#Botones Agente 3/4

    def pressUp():
        print("boton arriba") 

    def pressDown():
        print("boton abajo")

    def pressLeft():
        print("boton izquierda")

    def pressRight():
        print("boton derecha")
    
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
            if not terrain.seen_flag:#Si no lo hemos visto lo pasamos a negro
                color="#000000"
            elif terrain.visited_flag:
                if terrain==fin_pos:
                    color="#FF0000"
                elif terrain==ini_pos:
                    color="#0000FF"
                else:
                    color=visited_switch[terrain.Valor]
            elif terrain.seen_flag and not terrain.visited_flag:
                color=only_seen_switch[terrain.Valor]
            canvas.create_rectangle(x, y, x+length, y+length, fill=color)

    Fx = fin_pos.Xcoordinate # Agrega la x en el punto final
    Fy = fin_pos.Ycoordinate
    canvas.create_text(((Fx+0.5)*length,(Fy+0.5)*length), text="X")

    Ix = ini_pos.Xcoordinate # Agrega la O en el punto inicial
    Iy = ini_pos.Ycoordinate
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="O")

    up = Button(ventana, text="arriba", command=pressUp)
    up.pack(side=RIGHT, padx=20)

    right = Button(ventana, text="Derecha", command=pressRight)
    right.pack(side=RIGHT, padx=20)

    left = Button(ventana, text="Izquierda", command=pressLeft)
    left.pack(side=RIGHT, padx=20)

    down = Button(ventana, text="abajo", command=pressDown)
    down.pack(side=RIGHT, padx=20)
    ventana.mainloop()

def BAg34(Matrix:rd.Coord,jugador:bool,fin_pos:rd.Coord,ini_pos:rd.Coord):#Botones Agente 5

    def pressA():                              # A B   la esquina en la que está cada letra 
        print("boton A")                       # C D   representa su direccion

    def pressB():
        print("boton B")

    def pressC():
        print("boton C")

    def pressD():
        print("boton D")
    
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
            if not terrain.seen_flag:#Si no lo hemos visto lo pasamos a negro
                color="#000000"
            elif terrain.visited_flag:
                if terrain==fin_pos:
                    color="#FF0000"
                elif terrain==ini_pos:
                    color="#0000FF"
                else:
                    color=visited_switch[terrain.Valor]
            elif terrain.seen_flag and not terrain.visited_flag:
                color=only_seen_switch[terrain.Valor]
            canvas.create_rectangle(x, y, x+length, y+length, fill=color)
    
    Fx = fin_pos.Xcoordinate # Agrega la x en el punto final
    Fy = fin_pos.Ycoordinate
    canvas.create_text(((Fx+0.5)*length,(Fy+0.5)*length), text="X")

    Ix = ini_pos.Xcoordinate # Agrega la O en el punto inicial
    Iy = ini_pos.Ycoordinate
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="O")

    A = Button(ventana, text="A", command=pressA)
    A.pack(side=RIGHT, padx=20)

    B = Button(ventana, text="B", command=pressB)
    B.pack(side=RIGHT, padx=20)

    B = Button(ventana, text="C", command=pressC)
    B.pack(side=RIGHT, padx=20)

    B = Button(ventana, text="D", command=pressD)
    B.pack(side=RIGHT, padx=20)
    ventana.mainloop()

def select_Ag():  #es para escoger el agente, al final retorna el numero que indica cada agente

    def mostrar_descripcion(event):

        global agente_seleccionado
        agente_seleccionado = agente.get()
        opcion = agente.get()
        descripcion = descripciones[opcion]
        lbl_descripcion.config(text=descripcion)
        ventana.destroy()

    def selec():
        opcion = agente.get()
        descripcion = descripciones[opcion]
        print(f"Opción seleccionada: {opcion} + {descripcion}")

    ventana = Tk()
    ventana.title("Seleccionar agente")
    ventana.geometry("600x400")
    ventana.configure(bg="#FDF6FF")

    # Definir opciones y descripciones
    opciones = [1, 2, 3, 4, 5]
    descripciones = {
        1: "Movimiento de giro izquierda y avance",
        2: "Movimiento de giro izquierda, giro derecha y avance",
        3: "Movimietno de avance hacia las 4 diracciones",
        4: "Movimieto igual a una reina en ajedrez",
        5: "Movimietno igual a un alfil en ajedrez",
    }

    # Crear widgets
    agente = IntVar()
    menu = OptionMenu(ventana, agente, *opciones, command=mostrar_descripcion)
    menu.pack(side=LEFT, padx=10)

    lbl_descripcion = Label(ventana, text="", bg="#FDF6FF", font=("Arial", 12), justify=LEFT)
    lbl_descripcion.pack(side=RIGHT, padx=30)

    btn_guardar = Button(ventana, text="Guardar", font=("Arial", 16), command=selec)
    btn_guardar.pack(side=LEFT, padx=10)

    
    ventana.mainloop()
    return agente_seleccionado



#================Funcion para actualizar el mapa===============
def update_map(canvas,Matrix:rd.Coord,fin_pos,ini_pos,act_pos):
    list = Matrix
    a = len(list)
    length = 500//a
    canvas.delete("all")
    for i in range(a):
        y = i * length
        for j in range(a):
            x = j * length
            terrain=list[i][j]
            if not terrain.seen_flag:#Si no lo hemos visto lo pasamos a negro
                color="#000000"
            elif terrain.visited_flag:
                if terrain==fin_pos:
                    color="#FF0000"
                elif terrain==ini_pos:
                    color="#0000FF"
                elif terrain==act_pos:
                    color="#FFFFFF"
                else:
                    color=visited_switch[terrain.Valor]
            elif terrain.seen_flag and not terrain.visited_flag:
                color=only_seen_switch[terrain.Valor]
            canvas.create_rectangle(x, y, x+length, y+length, fill=color)
    Fx = fin_pos.Xcoordinate # Agrega la x en el punto final
    Fy = fin_pos.Ycoordinate
    canvas.create_text(((Fx+0.5)*length,(Fy+0.5)*length), text="X")

    Ix = ini_pos.Xcoordinate # Agrega la O en el punto inicial
    Iy = ini_pos.Ycoordinate
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="O")
    

    canvas.update() # actualiza el widget canvas







#=========================Valores de color que se pueden tomar en la matrix===============================
#key/value
visited_switch={
    '0':"#57605A",
    '1':"#5D370F",
    '2':"#06ACEE",
    '3':"#E2C58B",
    '4':"#00C606",
    '5':"#830EC6"
}

only_seen_switch={
    '0':"#666666",
    '1':"#665030",
    '2':"#5A7F8C",
    '3':"#A69867",
    '4':"#005500",
    '5':"#663366"
}

path_swich={
    '0': "#8A938D",
    '1': "#8F520E",
    '2': "#0AB9FF",
    '3': "#F5E0A7",
    '4': "#18FF08",
    '5': "#BB22FF"
}
#=========================================================================================================

selec_agent_interface={
    1:BAg1,
    2:BAg2,
    3:BAg34,
    4:BAg34,
    5:BAg34
}