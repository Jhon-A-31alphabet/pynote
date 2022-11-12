

from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.colorchooser import askcolor





def guardar(x):
    a = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("textfile",".txt"),("pdf files",".pdf")])
    b = f"{a}.txt"
    file_Text =x.get(1.0,END)
    a.write(file_Text)
    a.close()



def oscuro(x,y):
    ventana = y.config(bg="gray")
    caja_texto = x.config(bg ="black",fg="white")
    
    barra_texto = x.config(insertbackground = "white")
   

def modo_claro(x,y):
    ventana = y.config(bg="white")
    caja_texto = x.config(bg ="white",fg="black")
    
    barra_texto = x.config(insertbackground = "black")


def personalizar_fondo(x,y):
    fondo_color =askcolor(title="color de fondo")
    caja_Texto_color =askcolor(title="caja de texto")
    fuente_caja_texto = askcolor(title="fuente")

    x.configure(bg=fondo_color[1])
    y.configure(bg=caja_Texto_color[1])
    y.configure(fg=fuente_caja_texto[1])



    #----------------




   

   


