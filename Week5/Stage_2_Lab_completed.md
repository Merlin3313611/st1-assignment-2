AI OFF -\> AI ON -\> VERIFY \| 1 hour

# Learning objectives

- Analyse the SmartCare client brief.

- Identify stakeholders and scope.

- Write functional and non-functional requirements.

- Develop user stories and Given-When-Then acceptance criteria.

- Use AI to critique requirements without allowing it to invent
  stakeholder needs.

- Produce SmartCare Requirements Specification v1.0.

# Part A - Client Brief: AI OFF

SmartCare uses spreadsheets and paper records. The key problems stated
in the brief are –

- Staff report duplicate bookings,

- difficulty finding patient information,

- inconsistent appointment status

- limited appointment history.

Stakeholders Management wants a small, maintainable patient,
practitioner, and appointment system.

# Part B - Stakeholders and Scope: AI OFF

Identify at least four stakeholders. Create In Scope and Out of Scope
lists. Label uncertain features as provisional rather than confirmed.  
: -

| **Stakeholder**   | **Need**                                                       | **Evidence**                                                                                         |
|-------------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Receptionist      | Fast, error-free booking to avoid duplicates                   | Case study: "duplicate appointment bookings"                                                         |
| Patient           | Correctly booked, trackable appointments                       | Case study: "inconsistent appointment status information"                                            |
| Practitioner      | Clear, reliable view of own schedule/availability              | Case study: "limited visibility of practitioner availability"                                        |
| Clinic management | Maintainable system with appointment history and basic reports | Case study: "lack of reliable appointment history"; "difficulty producing basic operational reports" |

**  
  
Scope**

**In Scope:** patient records, practitioner records, appointment
booking/cancellation, appointment status tracking, appointment history,
basic operational reporting.

**Out of Scope:** billing/payments, clinical treatment records, facial
recognition or biometric login.

**Provisional:** SMS/email notifications, patient self-service booking.

# Part C - Functional Requirements: AI OFF

Write 8-12 numbered functional requirements using FR-01, FR-02 and so
on. Each should describe one observable capability.  
***Ans:-  
***FR-01: Allow the staff to create a new patient record with name and
contact details

FR-02: Allow the staff to create a new practitioner record

FR-03: Allow staff to book a follow-up appointment for a patient or
practitioner with a date and time slot

FR-04: Prevent duplication of appointments for the same practitioner at
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

FR-11: The system shall display an error when a booking attempt would
create a duplication or clash

FR-12: Allows staff to generate a basic report of appointments with a
selected range.

# Part D - Non-Functional Requirements: AI OFF

Write 4-6 numbered non-functional requirements covering appropriate
qualities such as reliability, maintainability, usability, data
integrity or testability.  
***Ans:-***  
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

# Part E - User Stories and Acceptance Criteria: AI OFF

Write 4-6 user stories. For at least three, create Given-When-Then
acceptance criteria including one negative or failure scenario.  
***User Stories: -***  
  
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

# *Acceptance Criteria*

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

# Part F - AI Requirements Review: AI ON

Prompt: Act as a software requirements reviewer. Review the SmartCare
requirements for ambiguity, inconsistency, missing clarification
questions and testability. Do NOT invent new client requirements. For
every suggestion, state whether it is based on evidence or is only a
question/assumption requiring validation.

# Part G - VERIFY the AI Review

Classify each significant AI suggestion as Accepted, Modified, Rejected,
or Unverified. Explain the evidence used.

| AI suggestion                                      | Decision   | Reason/Evidence                                                                      |
|----------------------------------------------------|------------|--------------------------------------------------------------------------------------|
| Add SMS reminders                                  | Rejected   | Not in the case study, and it adds scope that Is beyond a small, maintainable system |
| Add duplicate booking check                        | Accepted   | Directly address the stated problem: duplicate appointment bookings                  |
| Add patient login or self-booking                  | Unverified | It is a feature that can be added but is not yet confirmed by the client's brief.    |
| Retains cancelled appointments in history database | Accepted   | Directly solves the problem “lack of reliable appointment history”                   |
| Add a treatment recommendation feature             | Rejected   | No clinic requirement exists in the brief; therefore, it is beyond scope             |

#  * Assumptions and Open Questions:- 
*Assumption: Only one clinic location is in scope as multi-site is not mentioned.

Assumption: No login/user-role system is required yet; provisional, pending client confirmation.

Open question: Should patients be able to book their own appointments, or is this staff-only?

Open question: Is a maximum number of appointments per day per practitioner needed?

Open question: What fields are required in the basic operational report (e.g., by practitioner, date/time, or by status)

# Part H - Finalize SmartCare v0.2

Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user
stories, acceptance criteria, assumptions/open questions and selected AI
review evidence.  
  
- Ans in Stage_2_SmartCare_v02_Requirements Specification. Md or is
submitted above

# Reflection

In 150-250 words: What did AI notice that you missed? What did AI invent
or overreach on? Which requirement changed after review? Why must
requirements have evidence?  
  
Ans:-

After reviewing the requirements against Microsoft Copilot, I didn’t
find much I had missed, except that history should be retained rather
than deleted after 30 days; this directly aligns with what was stated in
the problem brief. What was overreached were suggestions like AI-driven
treatment recommendations and facial recognition login; neither was
requested, and if implemented, would make the system more complicated,
which was the opposite of what they wanted. The requirement that changed
the most was the appointment cancellation feature; initially, it was
framed as deleting the appointment without memory retention, but now it
is marked as canceled and retained in the history database after the
review.  
This showed that requirements should be backed by evidence rather than
just plausibility, as a suggestion can sound reasonable and realistic
with no basis in what the client actually asked for. The only way to
avoid building the wrong system is to back every requirement with
evidence and not just make it sound like a nice feature to add.
