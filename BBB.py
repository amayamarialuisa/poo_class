class Dog:
    def __init__(
            self,
            breed: str,
            size: str,
            weight: float,
            age: int,
            name: str,
            gender: str,
            favorite: str,
            long_hair: bool,
            visit_type: str
    ):
        self.breed = breed
        self.size = size
        self.weight = weight
        self.age = age
        self.name = name
        self.gender = gender
        self.favorite = favorite
        self.long_hair = long_hair
        self.visit_type = visit_type

    def medical_record(self):
        return print(f"Hola soy {self.name}, vengo a {self.visit_type}")

    def description(self):
        return print(f"Soy raza {self.breed}, {self.gender} de tamaño {self.size}")

    def master(self):
        return print(f"Soy {self.name} y {self.favorite} es mi favorita")

dog1 = Dog(
    breed="Criolla",
    size="Mediano",
    weight=20,
    age=1,
    name="Burbuja",
    gender="Hembra",
    favorite="Luisa",
    long_hair=True,
    visit_type="Baño"
)

dog2 = Dog(
    breed="Criolla",
    size="Mediano",
    weight=15,
    age=1,
    name="Bombón",
    gender="Hembra",
    favorite="Luisa",
    long_hair=False,
    visit_type="Vacuna"
)

dog3 = Dog(
    breed="Criolla",
    size="Mediano",
    weight=10,
    age=1,
    name="Bellota",
    gender="Hembra",
    favorite="Pablo",
    long_hair=True,
    visit_type="Cirugía"
)

dog1.master()
