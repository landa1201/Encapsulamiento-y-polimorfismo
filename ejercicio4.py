class Persona:
    def __init__(self, nombre, edad, documento):
        self.__nombre = nombre
        self.__edad = edad if edad >= 0 else 0
        self.__documento = documento

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def documento(self):
        return self.__documento

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("Edad inválida. Debe ser mayor o igual a 0.")

    @documento.setter
    def documento(self, nuevo_documento):
        self.__documento = nuevo_documento

class Paciente(Persona):
    def __init__(self, nombre, edad, documento, diagnostico):
        super().__init__(nombre, edad, documento)
        self.__diagnostico = diagnostico
        self.__historial = []

    def agregar_historial(self, entrada):
        self.__historial.append(entrada)

    def ver_historial(self):
        return self.__historial

    def ver_diagnostico(self):
        return self.__diagnostico

    def _actualizar_diagnostico(self, nuevo_diagnostico):
        self.__diagnostico = nuevo_diagnostico

class Doctor(Persona):
    def __init__(self, nombre, edad, documento, especialidad):
        super().__init__(nombre, edad, documento)
        self.__especialidad = especialidad

    def ver_especialidad(self):
        return self.__especialidad

    def modificar_diagnostico(self, paciente, nuevo_diagnostico):
        if isinstance(paciente, Paciente):
            paciente._actualizar_diagnostico(nuevo_diagnostico)
            print("Diagnóstico actualizado.")
        else:
            print("Error: solo se puede modificar el diagnóstico de un paciente.")


paciente1 = Paciente("Loraine acosta", 22, "12345678", "Gripe")
paciente1.agregar_historial("Consulta inicial - fiebre")
paciente1.agregar_historial("Recetado paracetamol")

doctor1 = Doctor("Dr. Ramírez", 45, "87654321", "Medicina General")

print("Historial:", paciente1.ver_historial())

doctor1.modificar_diagnostico(paciente1, "Bronquitis leve")

print("Nuevo diagnóstico:", paciente1.ver_diagnostico())
