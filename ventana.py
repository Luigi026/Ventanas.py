import tkinter                               #Import Extrae modulos de python / INVOCO LA LIBRERIA 


ventana = tkinter.Tk()                       # CREO LA VENTANA
ventana.title("Mi   primera   ventana")      # AGREGO EL TITULO DE LA APP
ventana.geometry("500x200")                  # CONFIGUROEL TAMAÑO DE LA VENTANA
ventana.resizable(0,0)                       # BLOQUEO TAMAÑO DE VENTANA
ventana.iconbitmap("JIRA.ico")               # AGREGO ICONO A LA APP : https://convertio.co/es/
ventana.config(bg="black", relief="groove", bd=8)                 # AGREGO COLOR PERSONALIZADO : https://htmlcolorcodes.com/es/

ventana.mainloop()                           # MUESTRO LA VENTANA