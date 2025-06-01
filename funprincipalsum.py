class Suma:
    def __init__(self, b, a):
        self.b = b
        self.a = a

    def calcular_suma(self):
        return self.b + self.a

def main():
    try:
        b = float(input("Ingresa el numero1 : "))
        a = float(input("Ingresa el numero2: "))
        mi_suma = Suma(b, a)
        print("El área del triángulo es:", mi_suma.calcular_suma())
    except ValueError:
        print("Error: por favor ingresa solo números.")
if __name__ == "__main__":
    main()