class CitaMedica:
    def __init__(self, fecha, doctor, paciente):
        self.fecha = fecha
        self.doctor = doctor
        self.paciente = paciente

    def get_info(self):
        return f"Cita: {self.fecha}, Doctor: {self.doctor.nombre}, Paciente: {self.paciente.nombre}"


class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial_clinico = []

    def agregar_historial(self, cita):
        self.historial_clinico.append(cita)

    def listar_historial(self):
        print(f"Historial de {self.nombre}:")
        if not self.historial_clinico:
            print("No hay citas registradas.")
        else:
            for cita in self.historial_clinico:
                print(cita.get_info())


class Doctor:
    def __init__(self, nombre, especialidad_num):
        self.nombre = nombre
        self.especialidad_num = especialidad_num
        self.especialidades = {
            1: "Cardiología",
            2: "Neurología",
            3: "Pediatría",
            4: "Ginecología"
        }
        self.especialidad = self.especialidades.get(especialidad_num, "Especialidad no válida")
        self.citas = []

    def asignar_cita(self, paciente, fecha):
        cita = CitaMedica(fecha, self, paciente)
        self.citas.append(cita)
        paciente.agregar_historial(cita)

    def __str__(self):
        return f"{self.nombre} (Especialidad: {self.especialidad})"


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
        print("Lista de Doctores:")
        if not self.doctores:
            print("No hay doctores registrados.")
        else:
            for doctor in self.doctores:
                print(doctor)

    def listar_pacientes(self):
        print("Lista de Pacientes:")
        if not self.pacientes:
            print("No hay pacientes registrados.")
        else:
            for paciente in self.pacientes:
                print(paciente.nombre)


def main():
    hospital = Hospital("Hospital")

    while True:
        print("\n--- Menú del Hospital ---")
        print("1. Registrar Doctor")
        print("2. Registrar Paciente")
        print("3. Programar Cita")
        print("4. Listar Doctores")
        print("5. Listar Pacientes")
        print("6. Consultar Historial Clínico de un Paciente")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del Doctor: ")
            especialidad_num = None
            while especialidad_num not in range(1, 5):
                try:
                    especialidad_num = int(input("Especialidad del Doctor (1-Cardiología, 2-Neurología, 3-Pediatría, 4-Ginecología): "))
                except ValueError:
                     print("Por favor, ingresa un número válido.")
            doctor = Doctor(nombre, especialidad_num)
            hospital.agregar_doctor(doctor)
            print("Doctor registrado con éxito.")

        elif opcion == "2":
            nombre = input("Nombre del Paciente: ")
            edad = int(input("Edad del Paciente: "))
            paciente = Paciente(nombre, edad)
            hospital.agregar_paciente(paciente)
            print("Paciente registrado con éxito.")

        elif opcion == "3":
            hospital.listar_doctores()
            hospital.listar_pacientes()
            nombre_doctor = input("Nombre del Doctor: ")
            nombre_paciente = input("Nombre del Paciente: ")
            fecha = input("Fecha de la Cita (día-mes-año): ")

            if doctor and paciente:
                doctor.asignar_cita(paciente, fecha)
                print("Cita programada con éxito.")
            else:
                print("Doctor o paciente no encontrado.")

        elif opcion == "4":
            hospital.listar_doctores()

        elif opcion == "5":
            hospital.listar_pacientes()

        elif opcion == "6":
            nombre_paciente = input("Nombre del Paciente: ")
            paciente = next((p for p in hospital.pacientes if p.nombre == nombre_paciente), None)
            if paciente:
                paciente.listar_historial()
            else:
                print("Paciente no encontrado.")

        elif opcion == "7":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
