Stage 1 \| Introducing Software Technology Case Study with Python and
Guided AI use

# Learning goals

- Explain why software engineering is broader than coding.

- Identify stakeholders in a simple software problem.

- Recognise missing requirements.

- Critically evaluate AI-generated feature suggestions.

- Explain why AI output should not automatically be treated as correct.

# Activity 1 - Think-Pair-Share (10 minutes)

If ChatGPT or Copilot can produce a 100-line Python application very
quickly, what knowledge does a software engineer still need?

1\. Understanding what the actual business problem is and what the
client needs, as AI can't read between the lines of vague requirements.

2\. They have to have an actual understanding of the code to verify
whether it is secure and maintainable, as AI can produce code that runs
but still has bugs, poor design etc.

3\. System designs and decision-making are based on cost, user
experience, and scalability, as AI often doesn’t understand the external
factors.

# Activity 2 - Is This Software Engineering? (10 minutes)

Scenario A: A student writes a 50-line Python calculator.  
Scenario B: A team develops a payroll system used by 5,000 employees.  
Scenario C: An AI assistant generates a simple appointment application
from one prompt.

| Scenario | Programming? | Software engineering? | Why?                                                                                                                                                                                           |
|----------|--------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A        | YES          | NO                    | It is a single script with no requirements or stakeholders                                                                                                                                     |
| B        | YES          | YES                   | It's a full engineering process that includes analyzing requirements, working with stakeholders, testing the system, meeting reliability requirements, and planning for long-term maintenance. |
| C        | YES          | NO                    | Generating code from a prompt is programming, but it only becomes engineering once the person verifies requirements, tests, and takes responsibility for it.                                   |

# Activity 3 - SmartCare Problem Analysis (20 minutes)

Client statement: SmartCare Community Clinic currently uses spreadsheets
and paper records to manage patients and appointments. The clinic wants
new software to improve these processes.

## Task 1 - Identify stakeholders

| Stakeholder     | What do they need?                                                                                           |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Patients        | An easy way to book, view, and cancel appointments while ensuring their records remain private and accurate. |
| Practitioners   | Easy access to their own schedule and availability, with accurate appointment and patient records.           |
| Receptionist    | A simple way to manage bookings and cancellations while avoiding duplicate or conflicting appointments.      |
| Clinic Managers | Reliable operational reports and reduced errors from manual or spreadsheet-based processes.                  |

## Task 2 - Identify current problems

1.  Duplicate appointments occur due to there not being a central system
    to detect scheduling conflicts.

2.  Patient records are difficult to find because they are stored across
    spreadsheets and paper files.

3.  Appointment statuses are inconsistent, making it unclear whether
    appointments are confirmed, cancelled, or completed.

4.  Practitioners’ availability is unclear, making it difficult to
    identify which practitioners are available at a specific time.

## Task 3 - Ask client questions

1\. How many practitioners and patients does the system need to support
initially

2\. Will practitioners manage their own schedules directly, or will it
be only through reception

3\. What reports does clinic management currently use, and so will the
important information need to be duplicated?

4\. Which appointment statuses need to be recorded, such as booked,
completed, cancelled, or when the patient didn’t show up?

5\. Does existing patient or appointment data need to be transferred to
the new system?

# Activity 4 - Critique an AI Response (15 minutes)

An AI assistant suggests: appointment management; facial-recognition
login; AI diagnosis recommendations; patient search; online payment;
practitioner schedule view; insurance processing; automatic
treatment-plan generation.

| Suggestion                   | Client evidence?                                   | In scope? | Decision                                                                                             |
|------------------------------|----------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------|
| Appointment management       | Yes, directly requested                            | Yes       | Keep: directly addresses duplicate bookings and cancellation problems.                               |
| Facial recognition login     | No                                                 | No        | Reject: not requested; adds cost/complexity for a small clinic.                                      |
| AI diagnosis recommendations | No                                                 | No        | Reject: clinical decision support is outside a simple admin system and raises safety/liability risk. |
| Patient search               | Yes, implied by difficulty locating records        | Yes       | keep: directly solves a stated problem.                                                              |
| Online payment               | No                                                 | No        | Rejected for version 1: not mentioned by the client if requested, can be added later.                |
| Practitioner schedule view   | Yes, implied by limited visibility of availability | Yes       | Reject: directly solves a stated problem.                                                            |
| Insurance processing         | No                                                 | No        | Reject: significant added complexity not requested by client.                                        |
| Treatment-plan generation    | No                                                 | No        | Reject: clinical function; client explicitly ruled out a complex hospital system.                    |

# Exit question

Write one activity that a software engineer must perform and that cannot
safely be delegated entirely to AI.  
  
Ensuring the software meets the stakeholder’s actual needs. For example,
confirm with SmartCare staff that the double-booking prevention works as
expected for both reception staff and practitioners. AI can generate
code quickly, but it cannot take responsibility for whether the solution
is correct, safe, and feasible for the real business environment. This
requires human engineers who understand the domain and can work with
stakeholders to make informed decisions.
