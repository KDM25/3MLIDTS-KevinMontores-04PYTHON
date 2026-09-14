### Formulario de registro
## almacenamiento en TXT sin validación

import tkinter as tk
from tkinter import messagebox

### Definición de funciones
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar_fun():
    limpiar_campos()

def guardar_valores():
    # Obtener valores desde los entrys
    nombre = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    ### Obtener el genero de los RadioButtons
    genero = ""

    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    elif var_genero.get() == 3:
        genero = "Otro"

    with open(r"C:\Users\monto\Documents\#3MAgoDic26-python.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Apellidos: {apellidos}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Estatura: {estatura}\n")
        archivo.write(f"Teléfono: {telefono}\n")
        archivo.write(f"Género: {genero}\n")
        archivo.write("------------------------\n")


## Creación de Ventana
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")

# Crear variable para el RadioButton
var_genero = tk.IntVar()


## Creación de etiquetas y campos de entrada
lbNombre = tk.Label(ventana, text="Nombres :")
lbNombre.pack()

tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos :")
lbApellidos.pack()

tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Telefono :")
lbTelefono.pack()

tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad :")
lbEdad.pack()

tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura :")
lbEstatura.pack()

tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Genero")
lbGenero.pack()

rbHombre = tk.Radiobutton(
    ventana,
    text="Hombre",
    variable=var_genero,
    value=1
)
rbHombre.pack()

rbMujer = tk.Radiobutton(
    ventana,
    text="Mujer",
    variable=var_genero,
    value=2
)
rbMujer.pack()

rbOtro = tk.Radiobutton(
    ventana,
    text="Otro",
    variable=var_genero,
    value=3
)
rbOtro.pack()


## Creación de Botones
btnBorrar = tk.Button(
    ventana,
    text="Borrar valores",
    command=borrar_fun
)
btnBorrar.pack()

btnGuardar = tk.Button(
    ventana,
    text="Guardar",
    command=guardar_valores
)
btnGuardar.pack()


## Ejecución de ventana
ventana.mainloop()