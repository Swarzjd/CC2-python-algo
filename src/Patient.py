from CC2.src.Person import Person

class Patient(Person):

    def __init__(self, name,surname,age, diagnosis):
        super().__init__(name,surname, age)
        self.diagnosis = diagnosis
        self.is_treated = False
        self.vaccinated = False