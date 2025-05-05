class Estudiante:
    def __init__(self, nombre, codigo):
        self.__nombre = None
        self.__codigo = None
        self.__notas = []

        self.nombre = nombre
        self.codigo = codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if value.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = value

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        if not value.isalnum():
            raise ValueError("El código debe ser alfanumérico.")
        self.__codigo = value

    def agregar_nota(self, nota):
        if 0.0 <= nota <= 5.0:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self):
        if len(self.__notas) == 0:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    def es_aprobado(self):
        return self.calcular_promedio() >= 3.0

try:
    estudiante = Estudiante("Juan Pérez", "123ABC")
    estudiante.agregar_nota(4.5)
    estudiante.agregar_nota(3.8)
    estudiante.agregar_nota(5.0)

    print(f"Promedio: {estudiante.calcular_promedio()}")
    print(f"¿Está aprobado? {'Sí' if estudiante.es_aprobado() else 'No'}")

except ValueError as e:
    print(f"Error: {e}")
