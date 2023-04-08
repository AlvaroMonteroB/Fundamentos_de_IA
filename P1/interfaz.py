from tkinter import *
import numpy as np
import Read_data as rd



def interfaz(Matrix:rd.Coord):
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
            if list[i][j].Valor == '0': #montaña
                color = "#57605A"
            elif list[i][j].Valor == '1': #tierra
                color = "#5D370F"
            elif list[i][j].Valor == '2': #agua
                color = "#06ACEE"
            elif list[i][j].Valor == '3': #arena
                color = "#E2C58B"
            elif list[i][j].Valor == '4': #bosque
                color = "#00C606"
            elif list[i][j].Valor == '5': #pantano
                color = "#830EC6"
            elif list[i][j].Valor == '6': #valor para ver si no ha sido visitado
                color = "#000000"
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
