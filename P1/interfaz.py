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
                elif terrain.Valor == '0': #montaña
                    color = "#57605A"
                elif terrain.Valor == '1': #tierra
                    color = "#5D370F"
                elif terrain.Valor == '2': #agua
                    color = "#06ACEE"
                elif terrain.Valor == '3': #arena
                    color = "#E2C58B"
                elif terrain.Valor == '4': #bosque
                    color = "#00C606"
                elif terrain.Valor == '5': #pantano
                    color = "#830EC6"
                else:
                    color = "FFFFFF"
            elif terrain.seen_flag and not terrain.visited_flag:
                if terrain.Valor == '0': #montaña
                    color = "#7D7D7D"
                elif terrain.Valor == '1': #tierra
                    color = "#7D5F3F"
                elif terrain.Valor == '2': #agua
                    color = "#6DADBB"
                elif terrain.Valor == '3': #arena
                    color = "#B8A972"
                elif terrain.Valor == '4': #bosque
                    color = "#007F00"
                elif terrain.Valor == '5': #pantano
                    color = "#7D3F7D"

                else:
                    color = "FFFFFF"
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


