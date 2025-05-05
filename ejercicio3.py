class Empleado:
    def __init__(self, nombre, rol, clave_acceso):
        self.__nombre = nombre
        self.__rol = rol
        self.__clave_acceso = self.__cifrar_clave(clave_acceso)

    def __cifrar_clave(self, clave):
        return clave[::-1]

    def __descifrar_clave(self):
        return self.__clave_acceso[::-1]

    @property
    def nombre(self):
        return self.__nombre

    @property
    def rol(self):
        return self.__rol

    def verificar_clave(self, clave_ingresada):
        return self.__cifrar_clave(clave_ingresada) == self.__clave_acceso

    def cambiar_clave(self, clave_antigua, nueva_clave):
        if self.verificar_clave(clave_antigua):
            self.__clave_acceso = self.__cifrar_clave(nueva_clave)
            print("Clave cambiada correctamente.")
            return True
        else:
            print("Clave antigua incorrecta. No se cambió la clave.")
            return False


empleado = Empleado("Angie Camacho", "Abogada", "clave123")

print("Nombre:", empleado.nombre)
print("Rol:", empleado.rol)

print("\nVerificando clave correcta:", empleado.verificar_clave("clave123"))  
print("Verificando clave incorrecta:", empleado.verificar_clave("otraClave"))  

empleado.cambiar_clave("clave123", "nuevaClave456")  
print("Verificando nueva clave:", empleado.verificar_clave("nuevaClave456")) 
