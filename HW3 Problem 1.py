# Base class for patients
class Patient(object):
    def __init__(self, name):
        self.name = name
    def discharge(self):
        pass

class EmergencyPatient(Patient):
    def __init__(self, name):
        self.name = name
    def discharge(self):
        print("Name", self.name)
        print("type:", "Emergency Patient")
        return "ER"

class HospitalizedPatient(Patient):
    def __init__(self, name):
        self.name = name
    def discharge(self):
        print("Name", self.name)
        print("type:", "Hospitalized Patient")
        return "HOS"

class Hospital(object):
    def __init__(self):
        self.cost = 0
        self.patients = []
    def admit(self, patient):
        self.patients.append(patient)
    def discharge_all(self):
        for patient in self.patients:
            type = patient.discharge()
            if type == "ER":
                self.cost += 1000
            if type == "HOS":
                self.cost += 2000
    def get_total_cost(self):
        print("Total cost is",str(self.cost))
        return self.cost


H = Hospital()
P1 = EmergencyPatient("John")
H.admit(P1)
P2 = EmergencyPatient("Joao")
H.admit(P2)
P3 = HospitalizedPatient("Jan")
H.admit(P3)
P4 = EmergencyPatient("Yuehan")
H.admit(P4)
P5 = HospitalizedPatient("Juan")
H.admit(P5)

H.discharge_all()
H.get_total_cost()


