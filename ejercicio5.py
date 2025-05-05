class Transporte:
    def tipo_transporte(self):
        print("Tipo de transporte no espeficicado.")

class Coche(Transporte):
    def tipo_transporte(self):
        print("Transporte terrestre.")

class Avion(Transporte):
    def tipo_transporte(self):
        print("Transporte aéreo.")

class Barco(Transporte):
    def tipo_transporte(self):
        print("Transporte marítimo.")

mi_coche = Coche()
mi_avion = Avion()
mi_barco = Barco()

mi_coche.tipo_transporte()   
mi_avion.tipo_transporte()   
mi_barco.tipo_transporte()   
