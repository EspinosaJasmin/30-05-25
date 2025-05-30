import tkinter as tk

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def calcular():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        mi_triangulo = Triangulo(base, altura)
        resultado.config(text=f"Área: {mi_triangulo.calcular_area()}")
    except ValueError:
        resultado.config(text="Error: ingresa solo números.")

ventana = tk.Tk()
ventana.title("Área de un triángulo")

tk.Label(ventana, text="Base:").pack()
entry_base = tk.Entry(ventana)
entry_base.pack()

tk.Label(ventana, text="Altura:").pack()
entry_altura = tk.Entry(ventana)
entry_altura.pack()

tk.Button(ventana, text="Calcular área", command=calcular).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()