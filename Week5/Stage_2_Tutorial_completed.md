Week 5 \| 60 minutes

# Learning goals

- Analyse stakeholders.

- Distinguish functional and non-functional requirements.

- Recognise ambiguity and unsupported requirements.

- Define scope.

- Develop user stories and acceptance criteria.

- Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

| Stakeholder       | Need                                                                           | Potential conflict                                                                                               |
|-------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Receptionist      | Fast and error-free booking to avoid duplication and checking the appointments | Could want a simple screen; it can conflict with management wanting detailed reporting                           |
| Patient           | Correctly booked and trackable appointment, with easy rescheduling available.  | Could want flexible and last-minute changes, which would conflict with practitioners' need for stable schedules. |
| Practitioner      | Clear and reliable view of their own schedule and availability                 | May want control over their own availability; this could conflict with the receptionist's need to book freely    |
| Clinic Management | Maintainable system with appointment history and basic reports                 | Would want more data reporting fields, which can conflict with the small and maintainable system goal            |
| IT support        | Simple, low-maintenance system                                                 | Would want minimal features that could conflict with staff wanting more functionality                            |

# Activity 2 - Functional or Non-Functional?

□ <span class="mark">**Functional**</span> □ Non-functional The system shall
allow staff to cancel an appointment.

□ Functional □ <span class="mark">**Non-functional**</span> The system
should remain responsive for the course-scale dataset.

□ <span class="mark">**Functional**</span> □ Non-functional The system shall
retain cancelled appointments.

□ Functional □ <span class="mark">**Non-functional**</span> Core business
logic should be independently testable.

□ <span class="mark">**Functional**</span> □ Non-functional The system shall
search for a patient by ID.

# Activity 3 - Repair Ambiguous Requirements

The system should be easy to use.

Problem: “Easy to use” has no measurable standard.

Clarification question: What specific task should a new user complete or
what criteria should be used to measure easy

Patient search should be fast.

Problem: “Fast” usually has no defined threshold.

Clarification question: What is the maximum acceptable response time for
a patient search?

The system should securely manage data.

Problem: Doesn’t specify what security means; is it access control,
encryption, etc?

Clarification question: Which specific data needs protecting and from
whom (e.g., restrict records to only logged-in staff)?

Appointments should normally be easy to cancel.

Problem: What does normally imply, and how should “easy” be measured?

Clarification question: Are there conditions under which cancellations
should be restricted, such as 15 min or same-day cancellations, and what
does easy mean? Is it in terms of the steps and clicks?

# Activity 4 - AI Requirements Audit

Classify each suggestion: Confirmed / Assumption requiring validation /
Unsupported / Out of scope.

| AI suggestion                             | Classification                  | Evidence/reason                                                                                              |
|-------------------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------|
| Patients receive SMS reminders.           | Assumption requiring validation | Not mentioned in the case study; it's plausible but would need client confirmation                           |
| Facial recognition login.                 | Out of Scope                    | There was no mention of biometric security, and the study calls it a manageable application, not complicated |
| Receptionists create appointments.        | Confirmed                       | It is directly implied – Staff currently do booking via spreadsheet                                          |
| Online payment.                           | Out of Scope                    | No mention of billing or payment in the requirement                                                          |
| Practitioners view schedules.             | Confirmed                       | It is directly implied by “limited visibility of practitioner availability ”                                 |
| AI recommends treatments.                 | Unsupported                     | There was no clinical decision support requirement being mentioned anywhere. It is an overreach              |
| Cancelled appointments remain in history. | Confirmed                       | It directly addresses the problem of “lack of reliable appointment history ”                                 |

# Exit question

Why is 'AI suggested it' not sufficient evidence for a requirement?  
  
It is not a sufficient requirement because AI can generate
plausible-sounding features that were never asked for by the actual
client or stakeholder; it also has no access to the real business
context, budget, or constraints.AI always needs to trace back to an
actual stakeholder need or a documented problem in the brief; otherwise,
it would be wasted effort and would build features nobody asked for.
