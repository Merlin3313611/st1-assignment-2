# smartcare_v01.py
# Simple SmartCare appointment prototype (beginner-friendly, no DB, no GUI)

from typing import List, Dict, Optional
from datetime import datetime

appointments: List[Dict[str, str]] = []

def parse_time(timestr: str) -> Optional[str]:
    """Try to parse common datetime formats and return ISO-like string, else return original."""
    if timestr is None:
        return None
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d %I:%M %p", "%d/%m/%Y %H:%M", "%Y-%m-%d %H:%M:%S"):
        try:
            dt = datetime.strptime(timestr, fmt)
            return dt.strftime("%Y-%m-%d %H:%M")
        except Exception:
            continue
    # fallback: return trimmed string
    return timestr.strip()

def book_appointment(patient_name: str, practitioner_name: str, appointment_time: str) -> Dict[str, str]:
    """Book an appointment. Raises ValueError for missing patient name."""
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    time_parsed = parse_time(appointment_time)
    appt = {"patient": patient_name.strip(), "practitioner": practitioner_name.strip(), "time": time_parsed}
    appointments.append(appt)
    return appt

def find_conflicts(practitioner_name: str, appointment_time: str) -> List[Dict[str, str]]:
    """Return list of appointments that match practitioner and time exactly."""
    matches = []
    for a in appointments:
        if a["practitioner"].lower() == practitioner_name.strip().lower() and a["time"] == appointment_time:
            matches.append(a)
    return matches

def display_appointments() -> None:
    if not appointments:
        print("No appointments recorded.")
        return
    print("Current appointments:")
    for i, a in enumerate(appointments, start=1):
        print(f"{i}. Patient: {a['patient']} | Practitioner: {a['practitioner']} | Time: {a['time']}")

def run_demo():
    print("Welcome to SmartCare: The Clinical Appointment Booking System!")
    # sample bookings
    book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00")
    book_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30")
    display_appointments()

if __name__ == "__main__":
    run_demo()
