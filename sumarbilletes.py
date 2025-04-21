#Realizar un formulario dónde se puedan rellenar la cantidad de billetes de 5 €, 10€, 20 €, 50 €, 100 €, 200 € y 500 €.
#Mediante un boton nos informe del total Euros.

from tkinter import *
import tkinter as tk
from tkinter import ttk

def sumar():
    suma = (int(entrada_cinco.get() or 0) * 5 +
            int(entrada_diez.get() or 0) * 10 +
            int(entrada_veinte.get() or 0) * 20 +
            int(entrada_cincuenta.get() or 0) * 50 +
            int(entrada_cien.get() or 0) * 100 +
            int(entrada_doscientos.get() or 0) * 200 +
            int(entrada_quinientos.get() or 0) * 500)

    total.config(text=f'Total: {suma} €')

#.delete(0, tk.END) elimina todo el contenido del campo de entrada (Entry)
#0 indica que la eliminación comienza desde el primer carácter
#tk.END indica que se eliminará todo hasta el final del campo

def limpiar():
    entrada_cinco.delete(0, tk.END)
    entrada_diez.delete(0, tk.END)
    entrada_veinte.delete(0, tk.END)
    entrada_cincuenta.delete(0, tk.END)
    entrada_cien.delete(0, tk.END)
    entrada_doscientos.delete(0, tk.END)
    entrada_quinientos.delete(0, tk.END)
    total.config(text=f'Total: {0} €')

ventana = tk.Tk()
ventana.title("Sumar Billetes")
ventana.geometry("300x350")
icono = tk.PhotoImage(file="calculadora.png")
ventana.iconphoto(True, icono)
style = ttk.Style()
style.configure("TLabel", foreground="#24F895", font=("Segoe UI", 10))
style.configure("TButton", padding=6, relief="flat", font=("Segoe UI", 10, "bold"))

tk.Label(ventana, text="Billetes de 5€: ").grid(row=0, column=0, padx=5, pady=5)
entrada_cinco = tk.Entry(ventana)
entrada_cinco.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Billetes de 10€: ").grid(row=1, column=0, padx=5, pady=5)
entrada_diez = tk.Entry(ventana)
entrada_diez.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Billetes de 20€: ").grid(row=2, column=0, padx=5, pady=5)
entrada_veinte = tk.Entry(ventana)
entrada_veinte.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ventana, text="Billetes de 50€: ").grid(row=3, column=0, padx=5, pady=5)
entrada_cincuenta = tk.Entry(ventana)
entrada_cincuenta.grid(row=3, column=1, padx=5, pady=5)

tk.Label(ventana, text="Billetes de 100€: ").grid(row=4, column=0, padx=5, pady=5)
entrada_cien = tk.Entry(ventana)
entrada_cien.grid(row=4, column=1, padx=5, pady=5)

tk.Label(ventana, text="Billetes de 200€: ").grid(row=5, column=0, padx=5, pady=5)
entrada_doscientos = tk.Entry(ventana)
entrada_doscientos.grid(row=5, column=1, padx=5, pady=5)

tk.Label(ventana, text="Billetes de 500€: ").grid(row=6, column=0, padx=5, pady=5)
entrada_quinientos = tk.Entry(ventana)
entrada_quinientos.grid(row=6, column=1, padx=5, pady=5)


boton = ttk.Button(ventana, text="Sumar", command=sumar)
boton.grid(row=7, column=0, padx=5, pady=5)


total = tk.Label(ventana, text="Total: 0€")
total.grid(row=7, column=1, padx=5, pady=5)

boton = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton.grid(row=8, column=0, padx=5, pady=5)

barra_menus = tk.Menu()
menu = tk.Menu(barra_menus, tearoff=False)

menu.add_command(label="Sumar", command=sumar)
menu.add_separator()
menu.add_command(label="Limpiar", command=limpiar)
menu.add_separator()
menu.add_command(label="Salir", command=ventana.destroy)
barra_menus.add_cascade(menu=menu, label="Menú")

ventana.config(menu=barra_menus) 
ventana.mainloop()
