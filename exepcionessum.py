class Suma:
    def __init__(self, b, a):
        self.b = b
        self.a = a

    def calcular_suma(self):
        return self.b + self.a

try:
    b = float(input("Ingresa el primer numero : "))
    a = float(input("Ingresa el segundo numero: "))


    mi_suma = Suma(b, a)
    print("El resultado de la suma es:", mi_suma.calcular_suma())

except ValueError:
    print("Error: por favor ingresa solo números.")