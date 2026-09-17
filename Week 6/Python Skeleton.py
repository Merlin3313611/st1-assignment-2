from datetime import datetime


class Patient:
    def __init__(self, name: str, contact: str = "") -> None:
        self.name: str = name
        self.contact: str = contact

    def validate(self) -> bool:
        return bool(self.name)


class Practitioner:
    def __init__(self, name: str, specialty: str = "") -> None:
        self.name: str = name
        self.specialty: str = specialty


class Appointment:
    def __init__(self, patient: Patient, practitioner: Practitioner, date_time: datetime) -> None:
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.date_time: datetime = date_time
        self.status: str = "booked"

    def cancel(self) -> None:
        self.status = "cancelled"

    def update_status(self, new_status: str) -> None:
        self.status = new_status