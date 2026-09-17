Week 6 \| 60 minutes

# Candidate Concepts

| Candidate    | Class?            | Reason                                                                                                                                                   |
|--------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Patient      | Yes               | Has identity (name) and state; required by FR-01, FR-07, and FR-10; participates directly in booking and search workflows.                               |
| Practitioner | Yes               | Has identity (name, specialty) and state; required by FR-02, FR-04, and FR-08                                                                            |
| Appointment  | Yes               | Has identity, relationships (links Patient + Practitioner), state (status), and lifecycle behavior; required by FR-03, FR-04, FR-05, FR-06, FR-09, FR-11 |
| Name         | No                | It is an attribute belonging to Patient or Practitioner, so it is not a class of its own                                                                 |
| Clinic       | Optional          | No FR gives Clinic its own responsibility or state; current requirements do not justify a Clinic class.                                                  |
| Database     | No domain Class   | Infrastructure concern behind FR-06 and FR-12; it is a persistence mechanism, not a business concept.                                                    |
| Cancellation | No separate Class | A state transition of Appointment (FR-05/FR-06); represented as a status change, not an independent entity.                                              |
| Status       | No ordinary class | Finite set of values (booked/completed/cancelled/no-show), it is best modeled as a string on Appointment rather than being full class                    |

# 

# CRC Cards

## Patient

| Responsibilities                                                                                                                                                                                                           | Collaborators |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Holds the patient's own name and contact info; makes sure that data isn't left blank/invalid before it's used elsewhere, and it is what the appointment points to when it needs to know who the patient is.(FR-01, FR-07). | Appointment   |
|                                                                                                                                                                                                                            |               |

## Practitioner

| Responsibilities                                                                                                                                    | Collaborators |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| To know the practitioner’s name/specialty; provide practitioner details for scheduling; and support duplicate-booking checks (FR-02, FR-04, FR-08). | Appointment   |
|                                                                                                                                                     |               |

## Appointment

| Responsibilities                                                                                                                                                                             | Collaborators         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| To know the linked patient, practitioner, date/time, and status; manage valid cancellation and status transitions; and prevent duplicate bookings (FR-03, FR-04, FR-05, FR-06, FR-09, FR-11) | Patient; Practitioner |
|                                                                                                                                                                                              |                       |

# Relationship Reasoning

Patient to Appointment: Which relationship and why?  
Answer: Association. A Patient may have zero or many Appointments (FR-10
requires full appointment history), but each Appointment has exactly one
Patient. Not composition, since a Patient exists independently of any
single Appointment.

Practitioner to Appointment: what multiplicity?  
Answer: A Practitioner may have zero or many Appointments (FR-08 lists
all appointments for a practitioner); each Appointment has exactly one
Practitioner. Multiplicity: Practitioner 1 \<-\> 0..\* Appointment.

Should Appointment inherit from Patient?  
Ans - No. An Appointment is not a Patient; inheritance of it would
violate is-a semantics. Appointment only references a Patient
(association); it does not extend it.

Does Clinic need to own every object?  
  
Ans: Not in the current model. No FR justifies a Clinic 'God object'
with strong composition ownership over Patient, Practitioner, and
Appointment.

# AI Model Critique

Critique AI proposals: PatientManager, PractitionerManager,
AppointmentManager, ClinicController, NotificationManager,
ScheduleEngine.

| AI proposals        | Decision       | Reason                                                                                                                                                                       |
|---------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PatientManager      | Reject for now | Patient's job is just holding its own identity/contact data; there's nothing here that needs a separate coordinating class.                                                  |
| PractitionerManager | Reject for now | Same problem; this jumps to a coordination layer before any requirement actually calls for one.                                                                              |
| AppointmentManager  | Partially keep | FR-04/FR-11 needs something to check across a practitioner's whole appointment list, so a service-style class may eventually be needed, but 'Manager' as a name is too vague |
| ClinicController    | Reject for now | This is UI/application-layer naming; it has no place inside the domain model.                                                                                                |
| NotificationManager | Reject for now | Nothing in the confirmed FRs mentions notifications, so this is invented scope                                                                                               |
| ScheduleEngine      | Reject for now | FR-04's conflict rule is real, but SmartCare's scale doesn't call for a dedicated engine class; therefore, that logic can live inside Appointment or a later service         |
