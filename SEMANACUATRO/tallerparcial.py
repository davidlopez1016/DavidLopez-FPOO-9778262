class CitaMedica:
    def __init__(self, fecha, doctor, paciente):
        self.fecha = fecha
        self.doctor = doctor
        self.paciente = paciente

    def get_info(self):
        return f"Cita para {self.paciente.nombre} con {self.doctor.nombre} en {self.fecha}"


class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.citas = []

    def asignar_cita(self, paciente, fecha):
        cita = CitaMedica(fecha, self, paciente)
        self.citas.append(cita)
        paciente.agregar_historial(cita)
        return cita


class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial_clinico = []

    def agregar_historial(self, cita):
        self.historial_clinico.append(cita)

    def listar_historial(self):
        for cita in self.historial_clinico:
            print(cita.get_info())


class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []
        self.pacientes = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def listar_doctores(self):
        for doctor in self.doctores:
            print(doctor.nombre)

    def listar_pacientes(self):
        for paciente in self.pacientes:
            print(paciente.nombre)

