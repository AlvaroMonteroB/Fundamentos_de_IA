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

class point_interes:
    def __init__(self,punto:rd.Coord,name):
        self.punto=punto
        self.name=name


## creo que se puede optimizar si cambiamos la forma en la que llamamos las funciones
def mapaR(Matrix:rd.Coord,jugador:bool,fin_pos:rd.Coord,ini_pos:rd.Coord,stack:rd.Coord,puntos): ##le cambie el nombre porque agregué otras funciones dependiendo de lo que se está haciendo en ese momento 

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
                
    if len(puntos) == 0:
        Fx = fin_pos.Xcoordinate # Agrega la x en el punto final
        Fy = fin_pos.Ycoordinate
        canvas.create_text(((Fx+0.5)*length,(Fy+0.5)*length), text="X")

        Ix = ini_pos.Xcoordinate # Agrega la O en el punto inicial
        Iy = ini_pos.Ycoordinate
        canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="I")
    else:
        Fx = fin_pos.Xcoordinate # Agrega la x en el punto final
        Fy = fin_pos.Ycoordinate
        canvas.create_text(((Fx+0.5)*length,(Fy+0.5)*length), text="X")

        Ix = ini_pos.Xcoordinate # Agrega la O en el punto inicial
        Iy = ini_pos.Ycoordinate
        canvas.create_text(((Ix+0.5)*length,(Iy+0.5)*length), text="I")

        for n in len(puntos):
            puntos[n][0] = int(puntos[n][0])
            puntos[n][1] = int(puntos[n][0])
            puntos[n][2] = str(puntos[n][0])
            if puntos[n][2] == "Llave":
                canvas.create_text(((puntos[n][0]+0.5)*length,(puntos[n][1]+0.5)*length), text="K")
            elif puntos[n][2] == "Templo Oscuro":
                canvas.create_text(((puntos[n][0]+0.5)*length,(puntos[n][1]+0.5)*length), text="D")
            else:
                canvas.create_text(((puntos[n][0]+0.5)*length,(puntos[n][1]+0.5)*length), text="P")

    ventana.mainloop()

######################################################



def select_Ag():  #es para escoger el agente, al final retorna el numero que indica cada agente

    def guardar():
        global agente_seleccionado, cxi,cyi,cxf,cyf, personaje_seleccionado
        cxi = int(Xinicio.get())
        cyi = int(Yinicio.get())
        cxf = int(Xfin.get())
        cyf = int(Yfin.get())

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
    return  cxi, cyi, cxf, cyf#

def AgregarPuntos():
    campos = []
    interes = []
    opciones = ["Llave", "Templo Oscuro", "Portal"]
    entry = None
    num = None
    

    def guardar():
        for n in range(len(campos)):
            temp = [int(campos[n][0].get()), int(campos[n][1].get()), campos[n][2].get()]
            interes.append(temp)
            print(interes[n])
            print(type(campos[n][2]))
        ventana.destroy()
        
        

    def add_fields():
        # Obtener el número ingresado en el entry
        nonlocal entry, campos, num
        num = int(entry.get())
        
        frame = Frame(ventana)
        frame.pack(pady=20)

        # Crear y agregar los campos
        count = 0
        for i in range(num):
            label1 = Label(frame, text="X:")
            label1.grid(row=i, column=0, padx=10, pady=10)
            entry1 = Entry(frame)
            entry1.grid(row=i, column=1, padx=10, pady=10)
            
            label2 = Label(frame, text="Y:")
            label2.grid(row=i, column=2, padx=10, pady=10)
            entry2 = Entry(frame)
            entry2.grid(row=i, column=3, padx=10, pady=10)
            
            label3 = Label(frame, text="Tipo:")
            label3.grid(row=i, column=4, padx=10, pady=10)
            
            # Crear el menú desplegable con las opciones
            
            var = StringVar()
            #var.set(list(opciones.keys())[0])
            dropdown = OptionMenu(frame, var, *opciones)
            dropdown.grid(row=i, column=5, padx=10, pady=10)
            
            campos.append((entry1, entry2, var))
            count += 1
            
            # Crear el botón de guardar solo después de crear el primer campo
            if count == 1:
                button.pack_forget() # ocultar el botón "Agregar campos"
                btn_guardar = Button(ventana, text="Guardar", font=("Arial", 16), command=guardar)
                btn_guardar.pack(padx=10)

    # Crear la ventana y los widgets
    ventana = Tk()
    ventana.title("")
    ventana.geometry("800x300")
    label = Label(ventana, text="Ingrese el número de visitas:")
    label.pack()
    entry = Entry(ventana)
    entry.pack()
    button = Button(ventana, text="Agregar", command=add_fields)
    button.pack()

    # Mostrar la ventana
    ventana.mainloop()
    return interes


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


def recorrido(Matrix,fin_pos,ini_pos,stack,raiz:b_p.Nodo,puntos:list[point_interes]):
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
        ventana.after(tim,update_map(canvas, Matrix, fin_pos, ini_pos, Agente.position,puntos))

    ventana.mainloop()


#================Funcion para actualizar el mapa===============
def update_map(canvas,Matrix:rd.Coord,fin_pos,ini_pos,act_pos,puntos:list[point_interes]):
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
            for data in puntos:
                if terrain.Xcoordinate==data.punto.Xcoordinate and terrain.Ycoordinate==data.punto.Ycoordinate:
                    color=destiny_switch[data.name]
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


destiny_switch={
    "Llave":"#FFD700",
    "Templo Oscuro":"#000000",
    "Portal":"#800080"
}

#=========================================================================================================




