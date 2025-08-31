

class Nombre:
    def __init__(self, edad, sexo, pais):
        self.edad = edad
        self.sexo = sexo
        self.pais = pais
        self.orientacion = None

    def agregar_orientacion_sexual(self, orientacion):
        self.orientacion = orientacion

victor = Nombre(30, "M", "Bolivia")
maria = Nombre(25, "F", "Colombia")

print(f"Esta es la orientación de Victor antes de añadir orientación a su objeto: {victor.orientacion}")
print(f"Esta es la orientación de María antes de añadir orientación a su objeto: {maria.orientacion}")

orientacion_sexual_victor = victor.agregar_orientacion_sexual("heterosexual")
orientacion_sexual_maria = maria.agregar_orientacion_sexual("homosexual")

print(f"Esta es la orientación de Victor después de añadir orientación a su objeto: {victor.orientacion}")
print(f"Esta es la orientación de María después de añadir orientación a su objeto: {maria.orientacion}")