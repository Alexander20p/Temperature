from tkinter import ttk,filedialog
import tkinter as tk
import time
def tiemp_act():
    tiempo = time.localtime()    
    hora = f"""    Hoy es {tiempo[0]}/{tiempo[1]}/{tiempo[2]} 
{tiempo[3]} horas, {tiempo[4]} minutos"""
    label_Tiempo_act["text"] = hora

    vent.after(100, tiemp_act)
vent = tk.Tk()
vent.geometry("700x500")
vent.title("hola")
vent.resizable(False,False)
vent.iconbitmap("./App_meteorologia/assets/image.ico")

label_Tiempo_act = ttk.Label(vent,font=( "Italic",20))
label_Tiempo_act.pack(ipadx=10, ipady=10)

tiemp_act()

vent.mainloop()


