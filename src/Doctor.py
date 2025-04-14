from CC2.src.Person import Person
from abc import ABC, abstractmethod

class Doctor(Person,ABC):
    def __init__(self, name,surname,age):
        super().__init__(name,surname,age)
        self.available = True

    @abstractmethod
    def can_vaccinate(self,patient) -> bool:
        return True

    def vaccinate(self,patient):
        if not patient.vaccinated:
            patient.vaccinated = True
            print (f"{patient.name} has been vaccinated by doctor {self.name} {self.surname}")

class Urgentiste(Doctor):

    def __init__(self, name,surname,age):
        super().__init__(name,surname,age)
        self.speciality = "urgentiste"

    def can_vaccinate(self,patient) -> bool:
        return True if patient.diagnosis == "urgency" else False


class MedecinGeneraliste(Doctor):

    def __init__(self, name,surname, age):
        super().__init__(name,surname,age)
        self.speciality = "Doctor Generaliste"

    def can_vaccinate(self,patient) -> bool:
        return True if patient.age >= 12 else False

class Pediatre(Doctor):
    def __init__(self, name,surname,age):
        super().__init__(name,surname,age)
        self.speciality = "Pediatre"

    def can_vaccinate(self,patient) -> bool:
        return True if 12 > patient.age >= 0 else False

