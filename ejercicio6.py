class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base

    @property
    def nombre(self):
        return self.__nombre

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self.__sueldo_base = nuevo_sueldo
        else:
            raise ValueError("El sueldo base no puede ser negativo.")

    def calcular_salario(self):
        return self.__sueldo_base


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo_base, bono):
        super().__init__(nombre, sueldo_base)
        self.__bono = bono

    def calcular_salario(self):
        return self.sueldo_base + self.__bono


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, tarifa_por_hora, horas_trabajadas):
        super().__init__(nombre, 0) 
        self.__tarifa_por_hora = tarifa_por_hora
        self.__horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.__tarifa_por_hora * self.__horas_trabajadas


class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, sueldo_base, impuesto):
        super().__init__(nombre, sueldo_base)
        self.__impuesto = impuesto  

    def calcular_salario(self):
        return self.sueldo_base * (1 - self.__impuesto)




empleados = [
    EmpleadoFijo("Ana", 2000, 500),
    EmpleadoPorHoras("Luis", 20, 120),
    EmpleadoTemporal("Marta", 1800, 0.15)
]

print("Cálculo de salarios:\n")
for emp in empleados:
    print(f"{emp.nombre} - Salario calculado: ${emp.calcular_salario():.2f}")
