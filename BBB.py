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
            visit_type: str,
            daily_walks: int,
            steps_per_walk: float,
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
        self.daily_walks = daily_walks
        self.steps_per_walk = steps_per_walk

    def daily_steps(self):
        return f"Hoy mi perro caminó: {self.daily_walks * self.steps_per_walk} pasos"

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
    visit_type="Baño",
    daily_walks=2,
    steps_per_walk=250
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
    visit_type="Vacuna",
    daily_walks=1,
    steps_per_walk=300
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
    visit_type="Cirugía",
    daily_walks=3,
    steps_per_walk=100
)

dog1.master()
steps = dog1.daily_steps()
print(steps)

#branch
