class Mascota:
    def __init__(self,nombre,tipo,edad):
        self.__nombre = nombre
        self.__tipo = tipo
        self.edad = edad

    def __str__(self):
        return f"{self.__nombre}, {self.__tipo},{self.edad}"


class Dueño:
    def __init__(self,dueño,telefono):
        self.__dueño = dueño
        self.__telefono = telefono
        self.__mascotas = []

    def agregar_mascota (self,Mascota):
        self.__mascotas.append(Mascota)        

    def mostrar_mascotas(self):
        return [str(mascota) for mascota in self.__mascotas]    


class Consulta:
    def __init__(self,fecha,motivo,mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.mascota = mascota

    def __str__(self):
        return f"La fecha de la consulta fue: {self.fecha} + El motivo fue: {self.motivo} + Su mascota es: {self.mascota}"




mascota_1 = Mascota("fifi","perro",3)        
mascota_2 = Mascota("garfield","gato",2)

dueño_1 = Dueño ("samy",3168150711)

dueño_1.agregar_mascota(mascota_1)
dueño_1.agregar_mascota(mascota_2)

consulta_1 = Consulta("2024-11-01", "Chequeo general", mascota_1)


print(dueño_1.mostrar_mascotas())
print(consulta_1)

