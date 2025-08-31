class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self):
        print(f"Guau Soy {self.nombre}")

perro1 = Perro("Max", "Pastor", 2)
perro1.ladrar()