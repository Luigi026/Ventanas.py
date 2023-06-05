import tkinter as tk

# FUNCIONES

def agregarEmpleado():
    if(entryNombre.get() != ""):                                # si el usuario ingresa un nombre y no un espacio vacio
        lista.insert(tk.END, entryNombre.get())                 # entonces que me agrege a la ultima posicion al entryNombre.get()
        entryNombre.delete(0, tk.END)                           # Delete me borra el contenido del campo del entry y al borrarlo lo deja en blaco y al se un espacio vacio deja de agregar

def borrarEmpleado():
    lista.delete(lista.curselection())                          # me devuelve la posicion del elemENto en la lista que el usuario haga clic


def modificarEmpleado():
    pos = lista.curselection()                                  # EN LA VARIABLE POS se guarda la posicion donde el usuario haga clic
    if(entryNombre.get() != ""):                                # luego verifico que el campo no este vacio
        lista.delete(pos)                                       # luego se borra el campo donde se haga clic en la lista                                               
        lista.insert(pos, entryNombre.get())                    # y por ultimo agrego el nuevo nombre modificado en el campo entryNombre
        entryNombre.delete(0, tk.END)

# ----ESTRUCTURA Y DISEÑO DE VENTANA----

ventana = tk.Tk() 
ventana.title("Alta de empleados")
ventana.geometry("400x500")

titulo = tk.Label(ventana,font=("Times New Roman", 15, "bold"), bd=8, text="Lista de empleados")
titulo.place(x=50, y=15)

labelNombre = tk.Label(ventana, font=("Times New Roman", 10, "bold"), text="Ingrese nombre: ")
labelNombre.place(x=50, y=70)

entryNombre = tk.Entry(ventana, fg="grey")
entryNombre.place(x=150, y=70)

# ---BOTONES---

botonAgregar = tk.Button(ventana, activebackground="green", bg="green", relief="groove",font=("Times New Roman", 10, "bold"), bd=8, text="Agregar", command= agregarEmpleado)
botonAgregar.place(x=300, y=67)

botonBorrar = tk.Button(ventana,activebackground="red", bg="red", relief="groove",font=("Times New Roman", 10, "bold"), bd=8, text="Borrar", command=borrarEmpleado)
botonBorrar.place(x=100,y=460)

botonModif = tk.Button(ventana,activebackground="yellow", bg="yellow", relief="groove",font=("Times New Roman", 10, "bold"), bd=8, text="Modificar", command=modificarEmpleado)
botonModif.place(x=200,y=460)

# ---- LISTAS ----

lista = tk.Listbox(ventana,font=("Times New Roman", 8, "bold"), width=50, height=20)
lista.place(x=50, y=120)

lista.insert(0, "Luis")
lista.insert(1, "Maria")
lista.insert(2, "Claudio")

ventana.mainloop()



