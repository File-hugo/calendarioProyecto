import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageTk

ventanaPrincipal=tk.Tk()
ventanaPrincipal.geometry("700x700")
ventanaPrincipal.title("Ventana Principal")

ventanaEnero = tk.Toplevel()
ventanaFebrero = tk.Toplevel()

ventanaEnero.geometry("1900x1000")
ventanaEnero.title("Calendario")
ventanaEnero.withdraw()

ventanaFebrero.geometry("1900x1000")
ventanaFebrero.title("Calendario")
ventanaFebrero.withdraw()

numeros = "123456789"
letras = "abcdefghijklmmnñopqrstuvwxyz"

def ingresarUsuario():
    user = usuario.get()
    if user == "":
        messagebox.showinfo("Aviso", "No ingresó usuario")
        return False
    elif not user.isalnum():  # Verifica si el usuario contiene solo caracteres alfanuméricos
        messagebox.showinfo("Aviso", "Usuario debe contener solo letras y números")
        return False
    else:
        lblMuestroUsuario.config(text="Hola " + user)
        return True

def ingresarContraseña():
    password = contraseña.get()
    if password == "":
        messagebox.showinfo("Aviso", "No ingresó contraseña")
        return False
    elif len(password) < 6 or not any(char.isdigit() for char in password):
        messagebox.showinfo("Aviso", "Contraseña debe tener al menos 6 caracteres y al menos un número")
        return False
    else:
        lblMuestroContraseña.config(text="Contraseña válida")
        return True

def entradaAVentanaEnero():
    if ingresarUsuario() and ingresarContraseña():
        ventanaEnero.deiconify()
        ventanaPrincipal.withdraw()

botonVerificar = tk.Button(ventanaPrincipal, command=entradaAVentanaEnero, text="Verificar", font="Arial 13")

usuario = tk.StringVar()
contraseña = tk.StringVar()

lblUsuario = tk.Label(ventanaPrincipal, text="Usuario", font="Arial 16")
entryUsuario = tk.Entry(ventanaPrincipal, text="", width=25, textvariable=usuario)
lblMuestroUsuario = tk.Label(ventanaPrincipal, bg='yellow', width=13, font="Arial 16")

lblUsuario.grid(row=0, column=0, ipady=7, pady=20, sticky="W", padx=20, columnspan=2)  # Adjusted line
entryUsuario.grid(row=1, column=0, ipady=7, sticky="W", padx=20,columnspan=2)
lblMuestroUsuario.grid(row=2, column=0, ipady=8, pady=50, sticky="W", padx=20, columnspan=2)

entryContraseña = tk.Entry(ventanaPrincipal, text="", width=45, textvariable=contraseña)
lblContraseña = tk.Label(ventanaPrincipal, text="Contraseña", width=17, font="Arial 16")
lblMuestroContraseña = tk.Label(ventanaPrincipal, bg='yellow', width=13, font="Arial 16")
lblAvisoContraseña = tk.Label(ventanaPrincipal, text="Contraseña debe tener mínimo 6 caracteres y numero/s", font="Arial 13")

lblContraseña.grid(row=0, column=1, pady=0, ipady=7, sticky="W", padx=(270, 120), columnspan=2) 
entryContraseña.grid(row=1, column=1, ipady=7, sticky="W", padx=(345, 100))                                                     
lblMuestroContraseña.grid(row=2, column=1, pady=50, sticky="E", padx=100, ipady=7, columnspan=2)
lblAvisoContraseña.grid(row=4, column=0, pady=50, sticky="SW", padx=(50, 0), columnspan=2)

botonVerificar.grid(row=3, column=1, padx=(0, 10)) 

ventanaPrincipal.columnconfigure(0, weight=1)
ventanaPrincipal.columnconfigure(1, weight=1)


#--------------------------PARTE DOS---------------------------------


def mesEnero():
    labelEnero.config(text="Enero")
    ventanaEnero.deiconify()
    ventanaFebrero.withdraw()

def mesFebrero():
    labelFebrero.config(text="Febrero")
    ventanaFebrero.deiconify()
    ventanaEnero.withdraw()
        
#-
fecha2024Enero = tk.Label(ventanaEnero, text="2024", font="Arial 29 bold", fg="red")
fecha2024Enero.grid(row=0, column=0, padx=60)
fecha2024Febrero = tk.Label(ventanaFebrero, text="2024", font="Arial 29 bold", fg="red")
fecha2024Febrero.grid(row=0, column=0, padx=60)

#Frame para contener los widgets de la semana
#Enero
frameDiasSemanaEnero = tk.Frame(ventanaEnero)
frameDiasSemanaEnero.grid(row=3, column=0, columnspan=4, padx=(10, 30), sticky="WN", pady=10)
#Febrero
frameDiasSemanaFebrero = tk.Frame(ventanaFebrero)
frameDiasSemanaFebrero.grid(row=3, column=0, columnspan=4, padx=(10, 30), sticky="WN", pady=10)

# Widgets para lunes a jueves dentro del frame
#Enero
entradaLunesEnero = tk.Text(frameDiasSemanaEnero, width=26, bd=2, height=8, font="Times 16")
entradaLunesEnero.grid(row=0, column=0,padx=20)
#Febrero
entradaLunesFebrero= tk.Text(frameDiasSemanaFebrero, width=26, bd=2, height=8, font="Times 16")
entradaLunesFebrero.grid(row=0, column=0,padx=20)
#Enero
entradaMartesEnero = tk.Text(frameDiasSemanaEnero, width=26, bd=2, height=8, font="Times 16")
entradaMartesEnero.grid(row=0, column=1,padx=10)
#Febrero
entradaMartesFebrero = tk.Text(frameDiasSemanaFebrero, width=26, bd=2, height=8, font="Times 16")
entradaMartesFebrero.grid(row=0, column=1,padx=10)
#Enero
entradaMiercolesEnero = tk.Text(frameDiasSemanaEnero, width=26, bd=2, height=8, font="Times 16")
entradaMiercolesEnero.grid(row=0, column=2,padx=10)
#Febrero
entradaMiercolesFebrero = tk.Text(frameDiasSemanaFebrero, width=26, bd=2, height=8, font="Times 16")
entradaMiercolesFebrero.grid(row=0, column=2,padx=10)
#Enero
entradaJuevesEnero = tk.Text(frameDiasSemanaEnero, width=26, bd=2, height=8, font="Times 16")
entradaJuevesEnero.grid(row=0, column=3,padx=0)
#Febrero
entradaJuevesFebrero = tk.Text(frameDiasSemanaFebrero, width=26, bd=2, height=8, font="Times 16")
entradaJuevesFebrero.grid(row=0, column=3,padx=0)
#Enero
entradaViernesEnero = tk.Text(frameDiasSemanaEnero, width=26, bd=2, height=8, font="Times 16")
entradaViernesEnero.grid(row=1, column=0, sticky="WN",padx=30,pady=100)
#Febrero
entradaViernesFebrero = tk.Text(frameDiasSemanaFebrero, width=26, bd=2, height=8, font="Times 16")
entradaViernesFebrero.grid(row=1, column=0, sticky="WN",padx=30,pady=100)
#Enero
entradaSabadoEnero = tk.Text(frameDiasSemanaEnero, width=26, bd=2, height=8, font="Times 16")
entradaSabadoEnero.grid(row=1, column=1, sticky="WN",padx=30,pady=100)
#Febrero
entradaSabadoFebrero = tk.Text(frameDiasSemanaFebrero, width=26, bd=2, height=8, font="Times 16")
entradaSabadoFebrero.grid(row=1, column=1, sticky="WN",padx=30,pady=100)
#Enero
entradaDomingoEnero = tk.Text(frameDiasSemanaEnero, width=26, bd=2, height=8, font="Times 16")
entradaDomingoEnero.grid(row=1, column=2, sticky="WN",padx=50,pady=100)
#Febrero
entradaDomingoFebrero = tk.Text(frameDiasSemanaFebrero, width=26, bd=2, height=8, font="Times 16")
entradaDomingoFebrero.grid(row=1, column=2, sticky="WN",padx=50,pady=100)

#Labels
#Enero
labelEnero = tk.Label(ventanaEnero, text="Enero", font="Times 20 underline ")
labelEnero.grid(row=0, column=1, padx=200, pady=40)
#FEbrero
labelFebrero = tk.Label(ventanaFebrero, text="Enero", font="Times 20 underline ")
labelFebrero.grid(row=0, column=1, padx=200, pady=40)

#Dias Label de Enero
lunesLabelEnero = tk.Label(ventanaEnero, text="Lunes", font="Times 17")
martesLabelEnero = tk.Label(ventanaEnero, text="Martes", font="Times 17")
miercolesLabelEnero = tk.Label(ventanaEnero, text="Miercoles", font="Times 17")
juevesLabelEnero = tk.Label(ventanaEnero, text="Jueves", font="Times 17")
viernesLabelEnero = tk.Label(ventanaEnero, text="Viernes", font="Times 17")
sabadoLabelEnero = tk.Label(ventanaEnero, text="Sabado", font="Times 17")
domingoLabelEnero = tk.Label(ventanaEnero, text="Domingo", font="Times 17")

lunesLabelEnero.grid(row=1, column=0,padx=200,sticky="WN")
martesLabelEnero.grid(row=1, column=1,padx=130,sticky="WN")
miercolesLabelEnero.grid(row=1, column=2,padx=160,sticky="WN")
juevesLabelEnero.grid(row=1, column=3,padx=180,sticky="WN")
viernesLabelEnero.grid(row=3, column=0,padx=180,pady=330,sticky="WN")
sabadoLabelEnero.grid(row=3, column=1,padx=180,pady=330,sticky="WN")
domingoLabelEnero.grid(row=3, column=2,padx=180,pady=330,sticky="WN")

#Días label de Febrero
lunesLabelFebrero=tk.Label(ventanaFebrero, text="Lunes", font="Times 17")
martesLabelFebrero=tk.Label(ventanaFebrero, text="Martes", font="Times 17")
miercolesLabelFebrero=tk.Label(ventanaFebrero, text="Miercoles", font="Times 17")
juevesLabelFebrero=tk.Label(ventanaFebrero, text="Jueves", font="Times 17")
viernesLabelFebrero=tk.Label(ventanaFebrero, text="Viernes", font="Times 17")
sabadoLabelFebrero=tk.Label(ventanaFebrero, text="Sabado", font="Times 17")
domingoLabelFebrero=tk.Label(ventanaFebrero, text="Domingo", font="Times 17")

lunesLabelFebrero.grid(row=1, column=0,padx=200,sticky="WN")
martesLabelFebrero.grid(row=1, column=1,padx=130,sticky="WN")
miercolesLabelFebrero.grid(row=1, column=2,padx=160,sticky="WN")
juevesLabelFebrero.grid(row=1, column=3,padx=180,sticky="WN")
viernesLabelFebrero.grid(row=3, column=0,padx=180,pady=330,sticky="WN")
sabadoLabelFebrero.grid(row=3, column=1,padx=180,pady=330,sticky="WN")
domingoLabelFebrero.grid(row=3, column=2,padx=180,pady=330,sticky="WN")

#fotos para enero y febrero:
imagenCalendario = Image.open("imagenes/logoCalendario.png")
resizeImagenCalendario = imagenCalendario.resize((85, 85))

imagenCalendarioTkEnero = ImageTk.PhotoImage(resizeImagenCalendario)
imagenCalendarioTkFebrero = ImageTk.PhotoImage(resizeImagenCalendario)

etiquetaImagenCalendarioEnero = tk.Label(ventanaEnero, image=imagenCalendarioTkEnero)
etiquetaImagenCalendarioEnero.grid(row=0, column=2, padx=10, pady=10)

etiquetaImagenCalendarioFebrero = tk.Label(ventanaFebrero, image=imagenCalendarioTkFebrero)
etiquetaImagenCalendarioFebrero.grid(row=0, column=2, padx=10, pady=10)

#flechasEnero
imagenFlechaDerechaEnero = Image.open("imagenes/flechaDerecha.png")
imagenFlechaIzquierdaEnero = Image.open("imagenes/flechaIzquierda.png")
resizeFlechaDerechaEnero = imagenFlechaDerechaEnero.resize((65, 65))
resizeFlechaIzquierdaEnero = imagenFlechaIzquierdaEnero.resize((65, 65))
imagenFlechaDerechaTkEnero = ImageTk.PhotoImage(resizeFlechaDerechaEnero)
imagenFlechaIzquierdaTkEnero = ImageTk.PhotoImage(resizeFlechaIzquierdaEnero)

etiquetaFlechaDerechaEnero = tk.Button(ventanaEnero, image=imagenFlechaDerechaTkEnero, command=mesFebrero)
etiquetaFlechaIzquierdaEnero = tk.Button(ventanaEnero, image=imagenFlechaIzquierdaTkEnero, command=mesEnero)

etiquetaFlechaDerechaEnero.grid(row=0, column=1, padx=(360,0), pady=40,sticky="WN")
etiquetaFlechaIzquierdaEnero.grid(row=0, column=1, padx=(0,300), pady=10)

#flechasEnero
imagenFlechaDerechaFebrero = Image.open("imagenes/flechaDerecha.png")
imagenFlechaIzquierdaFebrero = Image.open("imagenes/flechaIzquierda.png")
resizeFlechaDerechaFebrero = imagenFlechaDerechaFebrero.resize((65, 65))
resizeFlechaIzquierdaFebrero = imagenFlechaIzquierdaFebrero.resize((65, 65))
imagenFlechaDerechaTkFebrero = ImageTk.PhotoImage(resizeFlechaDerechaFebrero)
imagenFlechaIzquierdaTkFebrero = ImageTk.PhotoImage(resizeFlechaIzquierdaFebrero)

etiquetaFlechaDerechaFebrero = tk.Button(ventanaFebrero, image=imagenFlechaDerechaTkFebrero)
etiquetaFlechaIzquierdaFebrero = tk.Button(ventanaFebrero, image=imagenFlechaIzquierdaTkFebrero, command=mesEnero)

etiquetaFlechaDerechaFebrero.grid(row=0, column=1, padx=(360,0), pady=40,sticky="WN")
etiquetaFlechaIzquierdaFebrero.grid(row=0, column=1, padx=(0,300), pady=10)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ventanaEnero.mainloop()
ventanaFebrero.mainloop()








