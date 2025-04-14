class CentreVacination:
    def __init__(self, centre):
        self.centre = centre
        self.awaiting_list = []
        self.doctors = []

    def clear_list(self):
        new_list = [patient for patient in self.awaiting_list if patient.vaccinated == False]
        self.awaiting_list = new_list

    def add_doctor(self,doctor):
        return self.doctors.append(doctor)

    def doctor_available(self):
        return [[doc.name,doc.speciality] for doc in self.doctors]

    def add_patient(self,patient):
        return self.awaiting_list.append(patient)

    def print_awaiting(self):
        for patient in self.awaiting_list:
            print(patient.name, patient.surname,patient.age,patient.vaccinated)

    def treat(self):
        for patient in self.awaiting_list:
            if patient.vaccinated:
                continue
            for doctor in self.doctors:
                if doctor.can_vaccinate(patient):
                    doctor.vaccinate(patient)
            if not patient.vaccinated:
                print(f"Patient {patient.name} {patient.surname} could not be vaccinated")
        self.clear_list()
