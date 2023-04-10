from tkinter import *
import numpy as np
import Read_data as rd



def interfaz(Matrix:rd.Coord,jugador:bool,fin_pos:rd.Coord,ini_pos:rd.Coord):
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

    f = Frame(ventana, bg="#FDF6FF")
    f.pack(side=RIGHT, anchor=CENTER, padx=50)

    up_button = Button(f, text="\u2191", font=("Arial", 16))
    up_button.grid(row=0, column=1)

    down_button = Button(f, text="\u2193", font=("Arial", 16))
    down_button.grid(row=2, column=1)

    left_button = Button(f, text="\u2190", font=("Arial", 16))
    left_button.grid(row=1, column=0)

    right_button = Button(f, text="\u2192", font=("Arial", 16))
    right_button.grid(row=1, column=2)


    ventana.mainloop()
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
    '0':"#7D7D7D",
    '1':"#7D5F3F",
    '2':"#6DADBB",
    '3':"#B8A972",
    '4':"#007F00",
    '5':"#7D3F7D"
}
#=========================================================================================================