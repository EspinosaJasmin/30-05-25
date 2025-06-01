class Suma:
    def __init__(self, b, a):
        self.b = b
        self.a = a

    def calcular_suma(self):
        return self.b + self.a


b = float(input("Ingresa el primer numero: "))
a = float(input("Ingresa el segundo numero: "))

mi_suma = Suma (b, a)

print("El área del triángulo es:", mi_suma.calcular_suma())