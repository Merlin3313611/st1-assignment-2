 1. Problem and Scope SmartCare is a small community Clinic that currently relies on spreadsheets and paper records to manage patients, practitioners, and appointments. This approach has caused duplicate bookings, lost or hard-to-find patient records, unclear practitioner availability, and unreliable appointment history. The client wants a software system to improve patient, practitioner, and appointment management. 

In Scope: patient records, practitioner records, appointment
booking/cancellation, appointment status tracking, appointment history,
and basic operational reporting

Out of Scope – billing and payments, clinical treatment records, facial
recognition or biometric login, sms or email notification, and patient
self-service booking.

# 2. Stakeholders

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Stakeholder</th>
<th>Need</th>
<th>Evidence</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Receptionist</td>
<td>Fast and error-free booking to avoid duplication</td>
<td><p>Case study:</p>
<p>“Duplicate appointment booking”</p></td>
</tr>
<tr class="even">
<td>Patient</td>
<td>Correctly booked and trackable appointment</td>
<td><p>Case study: -</p>
<p>“inconsistent appointment status information”</p></td>
</tr>
<tr class="odd">
<td>Practitioner</td>
<td>Clear and reliable view of their own schedule and availability</td>
<td><p>Case Study:-</p>
<p>“Inconsistent appointment status information”</p></td>
</tr>
<tr class="even">
<td>Clinic Management</td>
<td>Maintainable system with appointment history and basic reports</td>
<td><p>Case Study:-</p>
<p>“Lack of reliable appointment history;”</p>
<p>“Difficulty producing basic operational reports.”</p></td>
</tr>
<tr class="odd">
<td>IT support</td>
<td>Simple, low-maintenance system</td>
<td>Case study:<br />
"manageable application", not a complex system</td>
</tr>
</tbody>
</table>

# 3. Functional Requirements

FR-01: Allow the staff to create a new patient record with name and
contact details

FR-02: Allow the staff to create a new practitioner record

FR-03: Allow staff to book a follow-up appointment for a patient or
practitioner with a date and time slot

FR-04: Prevent duplication of appointment for the same practitioner at
the same time.

FR-05: Allow staff to cancel an existing appointment.

FR-06: Retain cancelled appointments in the history database for 30 days
rather than deleting them

FR-07: Allow staff to search for a patient record by their name or ID

FR-08: Display a list of appointments and availability for a given
practitioner.

FR-09: Allow staff to update the status of an appointment, like showing
them completed or cancelled.

FR-10: Shall allow staff to view patients' full appointment history

FR-11: System shall display an error when a booking attempt would create
a duplication or clash

FR-12: Allows staff to generate a basic report of appointments with a
selected range.

# 4. Non-Functional Requirements

NFR-01: Reliability- The system shall not lose appointment data if the
program closes unexpectedly.

NFR-02: Maintainability – The code should use functions and data
structures organized for easy modification by future developers.

NFR-03: Usability - A staff member should be able to book an appointment
within less than 5 steps.

NFR-04: Data Integrity- The system should validate that the patient’s
name and practitioner name fields are not left empty before saving the
record

NFR-05: Testability – Core Booking logic will be separated into
functions that can be tested independently to display the output code

NFR-06: Performance- The system will return search results within 2
seconds for a dataset of up to 500 appointments

# 5. User Stories

US-01: As a Receptionist, I want to book an appointment for a patient,
so that their visit can be recorded correctly.

US-02: As a receptionist, I want the system to warn me about duplicate
bookings, so that I don't double-book a practitioner.  
  
US-03: As a practitioner, I want to view my own daily schedule and
availability, so that I know who I'm seeing and when.

US-04: As a receptionist, I want to cancel an appointment, so that the
slot becomes available again.

US-05: As clinic management, I want to view a patient's appointment
history and generate basic reports, so that I can track care and clinic
operations over time.  
  
US-06: As a receptionist, I want to search for a patient by name, so
that I can quickly find their record without scrolling through
everything.

# 6. Acceptance Criteria

GIVEN a practitioner already has an appointment at 10:00 AM on 20 July  
WHEN a receptionist tries to book another appointment for that same
practitioner at 10:00 AM on 20 July  
THEN the system shall reject the booking and display an error message.

GIVEN an appointment has already been cancelled  
WHEN a receptionist attempts to cancel it again  
THEN the system shall display a message indicating the appointment is
already cancelled and take no further action

GIVEN a patient named "Mrs Samantha Smith" exists in the system  
WHEN a receptionist searches for "Samantha”  
THEN the system shall display Samantha Smith's record in the results

# 7. Assumptions and Open Questions 

Assumption: Only one clinic location is in scope as multi-site is not mentioned.

Assumption: No login/user-role system is required yet; provisional, pending client confirmation.

Open question: Should patients be able to book their own appointments, or is this staff-only?

Open question: Is a maximum number of appointments per day per practitioner needed?

Open question: What fields are required in the basic operational report (e.g., by practitioner, date/time, or by status)

# 8. AI Requirements Review Record

| AI suggestion                                      | Evidence? | Decision   | Reason                                                                               | Verification                 |
|----------------------------------------------------|-----------|------------|--------------------------------------------------------------------------------------|------------------------------|
| Add SMS reminders                                  | NO        | Rejected   | Not in the case study, and it adds scope that Is beyond a small, maintainable system | Flagged as out of scope      |
| Add duplicate booking check                        | YES       | Accepted   | Directly address the stated problem: duplicate appointment bookings                  | Matches FR-04                |
| Add patient login or self-booking                  | NO        | Unverified | It is a feature that can be added but is not yet confirmed by the client's brief.    | Needs stakeholder follow- up |
| Retains cancelled appointments in history database | YES       | Accepted   | Directly solves the problem “lack of reliable appointment history”                   | Matches FR-06                |
| Add a treatment recommendation feature             | NO        | Rejected   | No clinic requirement exists in the brief; therefore, it is beyond scope             | Flagged as out of scope      |
