from tkinter import *
import numpy as np
import Read_data as rd
import Agentes as ag
import various_methods as vm
from collections import deque
import Busq_prof as b_p
import tree_to_list
class agente:#Solo lo vamos a utilizar para recorrer la solucion al mostrarla
    def __init__(self,Matrix,stack:list()):
        self.Matrix=Matrix
        self.stack=stack
        self.position=vm.assign_point(Matrix, stack[0].Xcoordinate, stack[0].Ycoordinate, Matrix[stack[0].Ycoordinate][stack[0].Xcoordinate])
    def scan(self):
        scanned=[]
        vm.busq_point(self.Matrix, self.position.Xcoordinate+1, self.position.Ycoordinate)
        vm.busq_point(self.Matrix, self.position.Xcoordinate, self.position.Ycoordinate+1)
        vm.busq_point(self.Matrix, self.position.Xcoordinate-1, self.position.Ycoordinate)
        vm.busq_point(self.Matrix, self.position.Xcoordinate, self.position.Ycoordinate-1)
    def move(self):
        self.stack.pop(0)
        if len(self.stack)==0:
            return
        self.position=vm.assign_point(self.Matrix, self.stack[0].Xcoordinate, self.stack[0].Ycoordinate, self.Matrix[self.stack[0].Ycoordinate][self.stack[0].Xcoordinate])
        if self.stack[0].deci_flag:
            self.position.deci_flag=True



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
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="I")

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
        m=Agente.move_forward(0)
        if m:
            Agente.scan_forward(True)
            stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)

    def pressR():
        Agente.turn_rigth()
        Agente.scan_forward(True)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)

    def pressL():
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
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="I")

    avance = Button(ventana, text="avance", command=pressA)
    avance.pack(side=RIGHT, padx=20)

    giroR = Button(ventana, text="GDerecha", command=pressR)
    giroR.pack(side=RIGHT, padx=20)
    giroL = Button(ventana, text="GIzquierda", command=pressL)
    giroL.pack(side=RIGHT, padx=20)
    retorno=Button(ventana,text="Regresar",command=PressRet)
    retorno.pack(side=RIGHT,anchor=CENTER,padx=20)
    ventana.mainloop()
#Estos agentes deberían usar el teclado en forma wasd para moverse
def BAg34(Matrix:rd.Coord,jugador:bool,fin_pos:rd.Coord,ini_pos:rd.Coord,Agente:ag.Agente3):#Botones Agente 3/4
    stack=[]
    stack.append(Agente.position)
    def pressUp():
        m=Agente.move('w',0)
        if m:            
            Agente.scan()
            stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)    
        if Agente.position==fin_pos:
                ventana.destroy()

        

    def pressDown():
        m=Agente.move('s',0)
        if m:            
            Agente.scan()
            stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
        if Agente.position==fin_pos:
                ventana.destroy()

    def pressLeft():
        m=Agente.move('a',0)
        if m:            
            Agente.scan()
            stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
        if Agente.position==fin_pos:
                ventana.destroy()

    def pressRight():
        m=Agente.move('d',0)
        if m:            
            Agente.scan()
            stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
        if Agente.position==fin_pos:
                ventana.destroy()

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
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="I")

    up = Button(ventana, text="arriba", command=pressUp)
    up.pack(side=RIGHT, padx=20)

    right = Button(ventana, text="Derecha", command=pressRight)
    right.pack(side=RIGHT, padx=20)

    left = Button(ventana, text="Izquierda", command=pressLeft)
    left.pack(side=RIGHT, padx=20)

    down = Button(ventana, text="abajo", command=pressDown)
    down.pack(side=RIGHT, padx=20)
    
    retorno=Button(ventana,text="Regresar",command=PressRet)
    retorno.pack(side=RIGHT,anchor=CENTER,padx=20)
    ventana.mainloop()


def BAg5(Matrix:rd.Coord,jugador:bool,fin_pos:rd.Coord,ini_pos:rd.Coord,Agente:ag.Agente5):#Botones Agente 5
    stack=[]
    stack.append(Agente.position)
    def pressA():                              # A B   la esquina en la que está cada letra 
        m=Agente.move('w',1)                      # C D   representa su direccion
        if m:            
            Agente.scan_data()
            stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
        if Agente.position==fin_pos:
                ventana.destroy()
    def pressB():
        m=Agente.move('d',1)
        if m:            
            Agente.scan_data()
            stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
        if Agente.position==fin_pos:
                ventana.destroy()  

    def pressC():
        m=Agente.move('a',1)
        if m:            
            Agente.scan_data()
            stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
        if Agente.position==fin_pos:
                ventana.destroy()  

    def pressD():
        m=Agente.move('s',1)
        if m:            
            Agente.scan_data()
            stack.append(Agente.position)
        update_map(canvas,Matrix,fin_pos,ini_pos,Agente.position)
        if Agente.position==fin_pos:
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
    Agente.scan_data()
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
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="I")

    A = Button(ventana, text="A", command=pressA)
    A.pack(side=RIGHT, padx=20)

    B = Button(ventana, text="B", command=pressB)
    B.pack(side=RIGHT, padx=20)

    B = Button(ventana, text="C", command=pressC)
    B.pack(side=RIGHT, padx=20)

    B = Button(ventana, text="D", command=pressD)
    B.pack(side=RIGHT, padx=20)
    
    
    ventana.mainloop()


    def mostrar_descripcion(event):

        global agente_seleccionado, cxi,cyi,cxf,cyf, personaje_seleccionado
        cxi = int(Xinicio.get())
        cyi = int(Yinicio.get())
        cxf = int(Xfin.get())
        cyf = int(Yfin.get())
        personaje_seleccionado = personaje.get()
        agente_seleccionado = agente.get()
        opcion = agente.get()
        descripcion = descripciones[opcion]
        print(f"Opción seleccionada: {opcion} + {descripcion}")
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
    opcionesA = [1, 2, 3, 4, 5]
    descripciones = {
        1: "Movimiento de giro izquierda y avance",
        2: "Movimiento de giro izquierda, giro derecha y avance",
        3: "Movimiento de avance hacia las 4 diracciones",
        4: "Movimiento igual a una reina en ajedrez",
        5: "Movimietno igual a un alfil en ajedrez",
    }
    opcionesP = [1, 2, 3, 4]

    FSAP = Frame(ventana)#Frame Seleccion Agente/ Personaje
    FSAP.pack(pady=20)
    FSAP.configure(bg="#FDF6FF")

    # Crear widgets
    personaje = IntVar()
    menuP = OptionMenu(FSAP,personaje,*opcionesP)
    menuP.pack(side=LEFT, padx=10)

    agente = IntVar()
    menuA = OptionMenu(FSAP, agente, *opcionesA, command=mostrar_descripcion)
    menuA.pack(side=LEFT, padx=10)

    lbl_descripcion = Label(FSAP, text="", bg="#FDF6FF", font=("Arial", 12), justify=LEFT)
    lbl_descripcion.pack(side=RIGHT, padx=30)

    FCI = Frame(ventana)#Frame coordenadas de inicio
    FCI.pack(pady=20)
    FCI.configure(bg="#FDF6FF")

    lbl_inicio = Label(FCI, text="Coordenadas de inicio", bg="#FDF6FF", font=("Arial", 12))
    lbl_inicio.pack(padx=10)

    label_texto = Label(FCI, text="X:",bg="#FDF6FF",font=("Arial", 12))
    label_texto.pack(side=LEFT)
    Xinicio = Entry(FCI)
    Xinicio.pack(side=LEFT,)

    label_texto = Label(FCI, text="Y:",bg="#FDF6FF",font=("Arial", 12))
    label_texto.pack(side=LEFT)
    Yinicio = Entry(FCI)
    Yinicio.pack(side=LEFT)

    FCF = Frame(ventana)#Frame coordenadas de fin
    FCF.pack(pady=20)
    FCF.configure(bg="#FDF6FF")

    lbl_inicio = Label(FCF, text="Coordenadas de fin", bg="#FDF6FF", font=("Arial", 12))
    lbl_inicio.pack(padx=10)

    label_texto = Label(FCF, text="X:",bg="#FDF6FF",font=("Arial", 12))
    label_texto.pack(side=LEFT)
    Xfin = Entry(FCF)
    Xfin.pack(side=LEFT,)

    label_texto = Label(FCF, text="Y:",bg="#FDF6FF",font=("Arial", 12))
    label_texto.pack(side=LEFT)
    Yfin = Entry(FCF)
    Yfin.pack(side=LEFT)


    btn_guardar = Button(ventana, text="Guardar", font=("Arial", 16), command=guardar)
    btn_guardar.pack(padx=10)

    
    ventana.mainloop()
    return agente_seleccionado, cxi, cyi, cxf, cyf,personaje_seleccionado#

def select_Ag():  #es para escoger el agente, al final retorna el numero que indica cada agente

    def guardar():
        global agente_seleccionado, cxi,cyi,cxf,cyf, personaje_seleccionado
        cxi = int(Xinicio.get())
        cyi = int(Yinicio.get())
        cxf = int(Xfin.get())
        cyf = int(Yfin.get())
        personaje_seleccionado = str(personaje.get())
        agente_seleccionado = agente.get()
        ventana.destroy()

    def mostrar_descripcion(event):
        opcion = agente.get()
        descripcion = descripciones[opcion]
        lbl_descripcion.config(text=descripcion)

    def selec():
        opcion = agente.get()
        descripcion = descripciones[opcion]
        print(f"Opción seleccionada: {opcion} + {descripcion}")

    ventana = Tk()
    ventana.title("Seleccionar agente")
    ventana.geometry("600x400")
    ventana.configure(bg="#FDF6FF")

    # Definir opciones y descripciones
    opcionesA = [1, 2, 3, 4, 5]
    descripciones = {
        1: "Movimiento de giro izquierda y avance",
        2: "Movimiento de giro izquierda, giro derecha y avance",
        3: "Movimietno de avance hacia las 4 diracciones",
        4: "Movimieto igual a una reina en ajedrez",
        5: "Movimietno igual a un alfil en ajedrez",
    }
    opcionesP = [1, 2, 3, 4]

    FSAP = Frame(ventana)#Frame Seleccion Agente/ Personaje
    FSAP.pack(pady=20)
    FSAP.configure(bg="#FDF6FF")

    # Crear widgets
    personaje = IntVar()
    menuP = OptionMenu(FSAP,personaje,*opcionesP)
    menuP.pack(side=LEFT, padx=10)

    agente = IntVar()
    menuA = OptionMenu(FSAP, agente, *opcionesA, command=mostrar_descripcion)
    menuA.pack(side=LEFT, padx=10)

    lbl_descripcion = Label(FSAP, text="", bg="#FDF6FF", font=("Arial", 12), justify=LEFT)
    lbl_descripcion.pack(side=RIGHT, padx=30)

    FCI = Frame(ventana)#Frame coordenadas de inicio
    FCI.pack(pady=20)
    FCI.configure(bg="#FDF6FF")

    lbl_inicio = Label(FCI, text="Coordenadas de inicio", bg="#FDF6FF", font=("Arial", 12))
    lbl_inicio.pack(padx=10)

    label_texto = Label(FCI, text="X:",bg="#FDF6FF",font=("Arial", 12))
    label_texto.pack(side=LEFT)
    Xinicio = Entry(FCI)
    Xinicio.pack(side=LEFT,)

    label_texto = Label(FCI, text="Y:",bg="#FDF6FF",font=("Arial", 12))
    label_texto.pack(side=LEFT)
    Yinicio = Entry(FCI)
    Yinicio.pack(side=LEFT)

    FCF = Frame(ventana)#Frame coordenadas de fin
    FCF.pack(pady=20)
    FCF.configure(bg="#FDF6FF")

    lbl_inicio = Label(FCF, text="Coordenadas de fin", bg="#FDF6FF", font=("Arial", 12))
    lbl_inicio.pack(padx=10)

    label_texto = Label(FCF, text="X:",bg="#FDF6FF",font=("Arial", 12))
    label_texto.pack(side=LEFT)
    Xfin = Entry(FCF)
    Xfin.pack(side=LEFT,)

    label_texto = Label(FCF, text="Y:",bg="#FDF6FF",font=("Arial", 12))
    label_texto.pack(side=LEFT)
    Yfin = Entry(FCF)
    Yfin.pack(side=LEFT)


    btn_guardar = Button(ventana, text="Guardar", font=("Arial", 16), command=guardar)
    btn_guardar.pack(padx=10)

    
    ventana.mainloop()
    return agente_seleccionado, cxi, cyi, cxf, cyf,personaje_seleccionado#


def recorrido_anchura(Matrix,fin_pos,ini_pos,Agente:ag.Agente3):
    list = Matrix
    a = len(list)
    length = 500//a

    ventana = Tk()
    ventana.title("Mapa")
    ventana.geometry("850x600")
    ventana.configure(bg="#FDF6FF")

    canvas = Canvas(ventana, width=500, height=500, bg="#FDF6FF")
    canvas.pack(side=LEFT,padx=50)
    Agente.scan()
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
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="I")
    
    #=====Algoritmo de busqueda======

    queue = deque([(Agente.position, [])])
    visited = set()
    cost=0
    queue = deque([(Agente.position, [Agente.position])])
    while queue:
        node, path = queue.popleft()
        if node == fin_pos:
            ventana.after(400,print(""))
            ventana.destroy()
            return
        if node in visited:
            continue
        visited.add(node)
        Agente.position = node
        scanned=Agente.scan()
        ventana.after(100,update_map(canvas, Matrix, fin_pos, ini_pos, Agente.position))
        for direction in scanned:
            if not direction.dirs:
                continue
            else:
                Agente.position.actual_flag=False
                char_dir=b_p.switch2[direction.dirs]
                m=Agente.move(char_dir,cost)
                if m:
                    queue.append((Agente.position, path + [Agente.position]))
                    Agente.position =vm.assign_point(Matrix,node.Xcoordinate,node.Ycoordinate,node)
        
    update_map(canvas, Matrix, fin_pos, ini_pos, Agente.position)
    ventana.after(750,print(""))
    ventana.destroy()
    ventana.mainloop()


def recorrido(Matrix,fin_pos,ini_pos,stack,raiz:b_p.Nodo):
    list = Matrix
    if raiz:
        stack=tree_to_list.list_tree(raiz)
    Agente=agente(Matrix,stack)
    a = len(list)
    length = 500//a

    ventana = Tk()
    ventana.title("Mapa")
    ventana.geometry("850x600")
    ventana.configure(bg="#FDF6FF")

    canvas = Canvas(ventana, width=500, height=500, bg="#FDF6FF")
    canvas.pack(side=LEFT,padx=50)
    Agente.scan()
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
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="I")

       # stack=tree_to_list.tree_list(raiz)
    tim=125
    
    ventana.after(tim,print(""))
    while stack:
        if not stack:
            continue
        Agente.move()
        Agente.scan()
        ventana.after(tim,update_map(canvas, Matrix, fin_pos, ini_pos, Agente.position))

    ventana.mainloop()


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
                #Dinujar colores
                if terrain==fin_pos:
                    color="#FF0000"
                elif terrain==ini_pos:
                    color="#0000FF"
                elif terrain==act_pos:
                    color="#FFFFFF"
                else:
                    color=visited_switch[terrain.Valor]
                #dibujar texto arriba del color
            elif terrain.seen_flag and not terrain.visited_flag:
                color=only_seen_switch[terrain.Valor]
            canvas.create_rectangle(x, y, x+length, y+length, fill=color)
    for i in range(a):
        for j in range(a):
            terrain=list[i][j]
            if terrain.deci_flag:
                    canvas.create_text(((j+.5)*length,(i+.5)*length),text="V,O")
            elif terrain.visited_flag:
                    canvas.create_text(((j+.5)*length,(i+.5)*length),text="V")

            
    Fx = fin_pos.Xcoordinate # Agrega la x en el punto final
    Fy = fin_pos.Ycoordinate
    canvas.create_text(((Fx+0.5)*length,(Fy+0.5)*length), text="X")

    Ix = ini_pos.Xcoordinate # Agrega la O en el punto inicial
    Iy = ini_pos.Ycoordinate
    canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="I")
    

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
    5:BAg5
}


