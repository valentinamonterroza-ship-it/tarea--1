class Conjun:

    def __init__(self, n, c, g):
        self._nombre = n
        self._cedula = c
        self._genero = g

    # GETTERS
    def get_nombre(self):
        return self._nombre

    def get_cedula(self):
        return self._cedula

    def get_genero(self):
        return self._genero

    # SETTERS
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_cedula(self, nueva_cedula):
        self._cedula = nueva_cedula

    def set_genero(self, nuevo_genero):
        self._genero = nuevo_genero

    def __str__(self):
        return f"Nombre: {self._nombre}, Cedula: {self._cedula}, Genero: {self._genero}"


# -------------------------------------------------

class Paciente(Conjun):

    def __init__(self, nombre, cedula, genero, servicio):
        super().__init__(nombre, cedula, genero)
        self._servicio = servicio

    # GET
    def get_servicio(self):
        return self._servicio

    # SET
    def set_servicio(self, nuevo_servicio):
        self._servicio = nuevo_servicio

    def __str__(self):
        return f"Paciente: {super().__str__()}, Servicio: {self._servicio}"


# -------------------------------------------------

class Enfermera(Conjun):

    def __init__(self, nombre, cedula, genero, turno, rango):
        super().__init__(nombre, cedula, genero)
        self._turno = turno
        self._rango = rango

    # GETTERS
    def get_turno(self):
        return self._turno

    def get_rango(self):
        return self._rango

    # SETTERS
    def set_turno(self, nuevo_turno):
        self._turno = nuevo_turno

    def set_rango(self, nuevo_rango):
        self._rango = nuevo_rango

    def __str__(self):
        return f"Enfermera: {super().__str__()}, Turno: {self._turno}, Rango: {self._rango}"


# -------------------------------------------------

class Medico(Conjun):

    def __init__(self, nombre, cedula, genero, turno, especialidad):
        super().__init__(nombre, cedula, genero)
        self._turno = turno
        self._especialidad = especialidad

    # GETTERS
    def get_turno(self):
        return self._turno

    def get_especialidad(self):
        return self._especialidad

    # SETTERS
    def set_turno(self, nuevo_turno):
        self._turno = nuevo_turno

    def set_especialidad(self, nueva_especialidad):
        self._especialidad = nueva_especialidad

    def __str__(self):
        return f"Medico: {super().__str__()}, Turno: {self._turno}, Especialidad: {self._especialidad}"


# -------------------------------------------------

class HospitalSistema:

    def __init__(self):
        self._pacientes = []
        self._enfermeras = []
        self._medicos = []

    # GETTERS
    def get_pacientes(self):
        return self._pacientes

    def get_enfermeras(self):
        return self._enfermeras

    def get_medicos(self):
        return self._medicos

    # SETTERS
    def set_pacientes(self, nueva_lista):
        self._pacientes = nueva_lista

    def set_enfermeras(self, nueva_lista):
        self._enfermeras = nueva_lista

    def set_medicos(self, nueva_lista):
        self._medicos = nueva_lista

    # AGREGAR
    def agregar_paciente(self, paciente):
        self._pacientes.append(paciente)

    def agregar_enfermera(self, enfermera):
        self._enfermeras.append(enfermera)

    def agregar_medico(self, medico):
        self._medicos.append(medico)

    # MOSTRAR
    def mostrar_todo(self):

        print("PACIENTES:")
        for p in self._pacientes:
            print(p)

        print("\nENFERMERAS:")
        for e in self._enfermeras:
            print(e)

        print("\nMEDICOS:")
        for m in self._medicos:
            print(m)


# -------------------------------------------------
# EJEMPLO DE USO
# -------------------------------------------------

sistema = HospitalSistema()

p1 = Paciente("Ana", "123", "F", "Urgencias")
e1 = Enfermera("Luis", "456", "M", "Noche", "Jefe")
m1 = Medico("Carlos", "789", "M", "Dia", "Cardiologia")

sistema.agregar_paciente(p1)
sistema.agregar_enfermera(e1)
sistema.agregar_medico(m1)

# USANDO GET
print(p1.get_nombre())
print(m1.get_especialidad())

# USANDO SET
p1.set_nombre("Maria")
m1.set_especialidad("Neurologia")

# MOSTRAR TODO
sistema.mostrar_todo()

      


