import tkinter as tk

pastel_pink = "#FFD1DC"
light_pink = "#FFE4E1"
white = "#FFFFFF"
light_gray = "#F0F0F0"

class Suma:
    def __init__(self, b, a):
        self.b = b
        self.a = a

    def calcular_suma(self):
        return self.b + self.a

def calcular():
    try:
        b = float(entry_b.get())
        a = float(entry_a.get())
        mi_suma = Suma(b, a)
        resultado.config(text=f"Suma: {mi_suma.calcular_suma()}", bg=light_pink)
    except ValueError:
        resultado.config(text="Error: ingresa solo números.", bg=light_pink)

ventana = tk.Tk()
ventana.title("Suma de dos numeros")
ventana.config(bg=pastel_pink)
ventana.geometry("400x300")

tk.Label(ventana, text="Numero 1:", bg=pastel_pink).pack()
entry_b = tk.Entry(ventana, bg=white)
entry_b.pack()

tk.Label(ventana, text="Numero 2:", bg=pastel_pink).pack()
entry_a = tk.Entry(ventana, bg=white)
entry_a.pack()

tk.Button(ventana, text="Calcular suma", command=calcular, bg=light_pink).pack()

resultado = tk.Label(ventana, text="", bg=pastel_pink)
resultado.pack()

ventana.mainloop()