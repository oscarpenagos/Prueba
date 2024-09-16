from Controlador import * 
from tkinter import *
from tkinter import messagebox, simpledialog

ventana = Tk()
ventana.title("Tarjetas")

def agregar():
    try:
        x = int(entry_id.get())
        y = entry_clave.get()
        z = int(entry_saldo.get())
        w = nueva_tarjeta(x,y,z)
        mostrar_mensaje(w,0,z)
    except:
        mostrar_mensaje(9,0,0)
    entry_clave.delete(0,'end')
    entry_id.delete(0,'end')
    entry_saldo.delete(0,'end')

    return

def consultar():
    try:
        x = int(entry_id.get())
        y = entry_clave.get()
        z = int(entry_saldo.get())
        w,v = consultar_saldo(x,y,z)
        mostrar_mensaje(w,v,z)
    except:
        mostrar_mensaje(9,v,0)
    entry_clave.delete(0,'end')
    entry_id.delete(0,'end')
    entry_saldo.delete(0,'end')
    return

def abonar():
    try:
        x = int(entry_id.get())
        y = entry_clave.get()
        z = int(entry_saldo.get())
        w,v = abonar_saldo(x,y,z)
        mostrar_mensaje(w,v,z)
    except:
        mostrar_mensaje(9,v,0)
    entry_clave.delete(0,'end')
    entry_id.delete(0,'end')
    entry_saldo.delete(0,'end')
    return

def retirar():
    try:
        x = int(entry_id.get())
        y = entry_clave.get()
        z = int(entry_saldo.get())
        w,v = retirar_saldo(x,y,z)
        mostrar_mensaje(w,v,z)
    except:
        mostrar_mensaje(9,v,0)
    entry_clave.delete(0,'end')
    entry_id.delete(0,'end')
    entry_saldo.delete(0,'end')
    return

def mostrar_mensaje(w,v,z=0):
    match w:
        case 1:
            messagebox.showerror(title="Error", message="Error, la tarjeta ya existe")
        case 2:
            messagebox.showerror(title="Error", message="Error, la tarjeta no existe")
        case 3:
            messagebox.showinfo(title=None, message="La tarjeta ha sido agregada")
        case 4:
            messagebox.showinfo(title=None, message="Su saldo es {}".format(v))
        case 5:
            messagebox.showerror(title="Error", message="Error, la clave es incorrecta")
        case 6:
            messagebox.showinfo(title=None, message="Su saldo era {}. Ahora su saldo es {}".format(v+int(z),v))
        case 7:
            messagebox.showerror(title="Error", message="Error, saldo insuficiente")
        case 8:
            messagebox.showinfo(title=None, message="Su saldo era {}. Ahora su saldo es {}".format(v-int(z),v))
        case 9:
            messagebox.showerror(title="Error", message="Las casillas ID y Saldo requieren valores numéricos")
    return

label_id = Label(ventana, text="ID")
label_id.grid(row=1,column=1,columnspan=2, padx=(10,10), pady=(5,5))

label_clave = Label(ventana, text="Clave")
label_clave.grid(row=3,column=1,columnspan=2, padx=(10,10), pady=(5,5))

label_saldo = Label(ventana, text="Saldo")
label_saldo.grid(row=5,column=1,columnspan=2, padx=(10,10), pady=(5,5))

entry_id = Entry(ventana)
entry_id.grid(row=2,column=1,columnspan=2, padx=(10,10), pady=(5,5))

entry_clave = Entry(ventana, show="*")
entry_clave.grid(row=4,column=1,columnspan=2, padx=(10,10), pady=(5,5))

entry_saldo = Entry(ventana)
entry_saldo.grid(row=6,column=1,columnspan=2, padx=(10,10), pady=(5,5))

button_abonar = Button(ventana,text="Abonar", command=abonar)
button_abonar.grid(row=7, column = 1, padx=(10,10), pady=(5,5))

button_retirar = Button(ventana,text="Retirar", command=retirar)
button_retirar.grid(row=7, column = 2, padx=(10,10), pady=(5,5))

button_consultar = Button(ventana,text="Consultar", command=consultar)
button_consultar.grid(row=8, column = 1, padx=(10,10), pady=(5,5))

button_agregar = Button(ventana,text="Agregar", command = agregar)
button_agregar.grid(row=8, column = 2, padx=(10,10), pady=(5,5))

button_cerrar = Button(ventana,text="Cerrar", command=ventana.destroy)
button_cerrar.grid(row=9, column = 1, columnspan=2, padx=(10,10), pady=(5,5))

ventana.mainloop()

