class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def arrancar(self):
        print(f"El {self.marca}, modelo {self.modelo} del año {self.año}, está arrancando.")

auto1 = Auto("Toyota", "Corolla", 2005)
auto1.arrancar()