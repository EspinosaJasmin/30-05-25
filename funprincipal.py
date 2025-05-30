class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def main():
    try:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        mi_triangulo = Triangulo(base, altura)
        print("El área del triángulo es:", mi_triangulo.calcular_area())
    except ValueError:
        print("Error: por favor ingresa solo números.")
if __name__ == "__main__":
    main()