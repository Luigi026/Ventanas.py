import tkinter as tk

def funcionSaludar():
    labelSaludo = tk.Label(ventana, fg="green", font=("Times New Roman", 14, "bold"), text="Hola "+entryNombre.get()+", como estas ? ")
    labelSaludo.grid(row=3, column=0, pady=5)

ventana = tk.Tk()                       
ventana.title("Saludar")
ventana.geometry("500x200")                  

labelNombre = tk.Label(ventana, font=("Times New Roman", 14, "bold"), text="Por favor ingrese nombre: ")   
labelNombre.grid(row=0, column=0) 

entryNombre = tk.Entry(ventana,fg="grey")
entryNombre.grid(row=0, column=1)

boton1 = tk.Button(ventana,bg="skyblue", font=("Times New Roman", 15, "bold"), bd=5, activebackground="skyblue", text="Saludar", command=funcionSaludar)
boton1.grid(row=3, column=1, pady=5)

ventana.mainloop()                           