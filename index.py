from CC2.src.CentreVacination import CentreVacination
from CC2.src.Person import Person
from CC2.src.Doctor import Pediatre, Urgentiste, MedecinGeneraliste
from CC2.src.Patient import Patient

CentreSante = CentreVacination('Centre place Verte - Valenciennes')

urgentist = Urgentiste('John', 'Doe',"32")
pediatrist = Pediatre('Anna', 'Smith',"41")
generalist1 = MedecinGeneraliste('Mary', 'Johnson', "39")
generalist2 = MedecinGeneraliste('Robert', 'Brown', "45")

CentreSante.add_doctor(urgentist)
CentreSante.add_doctor(pediatrist)
CentreSante.add_doctor(generalist1)
CentreSante.add_doctor(generalist2)

patients = [
    Patient("Hollywood",'Alice', 5, 'common cold'),
    Patient("Ross",'Bob', 35, 'urgency'),
    Patient("Chaplin",'Charlie', 10, 'flu'),
    Patient("Princess",'Diana', 3, 'fever'),
    Patient("Adam",'Eve', 28, 'headache'),
    Patient("Ocean",'Frank', 20, 'urgency'),
    Patient("Field",'Grace', 15, 'sore throat'),
    Patient("Tom",'Hank', 11, 'chickenpox'),
    Patient("Cambridge",'Ivy', 7, 'rash'),
    Patient("Black",'Jack', 40, 'urgency')
]

for patient in patients:
    CentreSante.add_patient(patient)


CentreSante.print_awaiting()

CentreSante.treat()

CentreSante.print_awaiting()

