A2 Case Study Stage 1 student resource

# SmartCare scenario

SmartCare Community Clinic currently uses spreadsheets and paper records
to manage patients and appointments. The client says: 'We need software
to help manage patients, practitioners and appointments.' This is not
yet a complete specification.

# Initial Engineering Brief

## Problem summary

SmartCare Community currently relies on spreadsheet and paper records to
manage their patients, practitioners, and appointments. This approach
has caused duplicate bookings, lost or hard-to-find patient records,
unclear practitioner availability, and unreliable appointment history.
The client wants a software system to improve the management of
patients, practitioners and appointments. However, specific requirements
including features, user numbers, reporting needs, and data migration
have not been defined.

## 2. Initial stakeholders

| Patients           | Quick way to book, view, and cancel appointments while keeping records accurate and private.    |
|--------------------|-------------------------------------------------------------------------------------------------|
| Practitioners      | Clear view of their own schedule and availability along with an accurate appointment history.   |
| Receptionist staff | Quick and reliable way to manage bookings and cancellations while preventing duplicate entries. |
| Clinic managers    | Reliable operational reports and fewer errors from manual processes.                            |
| Patients           | Simple way to book, view, and cancel appointments while keeping records accurate and private.   |

## 3. Initial features

| Feature                 | Confirmed or provisional? | Why?                                                                                                                     |
|-------------------------|---------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Appointment booking     | Confirmed                 | Addresses the client’s specific concern about preventing duplicate appointment bookings.                                 |
| Appointment cancelation | Provisional               | Suggested by the stated problem of manual cancellation processes but not yet explicitly requested as a system feature.   |
| Patient management      | Provisional               | Implied by the requirement to manage patients, but the specific information and fields needed have not yet been defined. |
| Practitioner management | Provisional               | Suggested by the requirement to manage practitioners, but the specific details have not yet been confirmed.              |

## 4. Questions for the client

1.  What patient information needs to be stored, such as contact details
    or medical history?

2.  Is there a need to prevent double-booking the same practitioner at
    the same time?

3.  How should practitioner availability be managed and updated, such as
    through a fixed weekly schedule or on a daily basis?

4.  Who should have permission to cancel or change existing appointments
    and should the prototype support cancelling an existing appointment?

5.  What format should the operational reports use, and who should
    receive them?

## 5. What we do not yet know

1.  The number of patients, practitioners, and appointments the system
    needs to support.

2.  Whether practitioners need their own login or if the reception
    managers handle everything centrally

3.  Any legal, regulatory, or data-privacy requirements the clinic must
    follow, particularly for handling health records.

# AI Activity Card - Ask, Check, Explain

## Before AI

What do I think the code does? What problems can I already identify?  
  
- I think book_appointment() checks the patient name, practitioner name,
and appointment time before saving the appointment as a dictionary in a
list and displaying the complete list to the user. Problems I can see is
that the original version did not prevent two different patients from
being booked with the same practitioner at the same time it only
displays one appointment instead of showing all appointments, and there
is also no way to cancel or edit an appointment.

## AI request

Act as a tutor. Explain this code and identify potential problems. Do
not provide a complete replacement. Ask me questions that help me reason
about the solution.

## Evaluate

| Suggestion                                                          | Useful | Unclear | Incorrect | Out of scope |
|---------------------------------------------------------------------|--------|---------|-----------|--------------|
| Check for duplicate booking function                                | Yes    |         |           |              |
| Store appointments in a database instead of a list                  |        |         |           | Yes          |
| Use a list of dictionaries to store appointments                    | Yes    |         |           |              |
| Add validation for practitioner name and time not just patient name | Yes    |         |           |              |

## Decide

For each significant suggestion: Accept / Modify / Reject / Keep
unverified.

- Check for duplicate booking function – Accept

- Store appointments in a database instead of a list - Reject

- Use a list of dictionaries to store appointments – Accept

- Add validation for practitioner name and time not just patient name –
  Accept

## Verify

- Run the code

- Test normal input

- Test unusual input

- Compare with requirements

- Ask tutor/peer

- Check documentation

## Explain

Can I explain the final code without reading the AI response? What do I
still need to understand?  
  
Yes, I can explain the final code without needing the AI's response; it
is a simple list of dictionaries with functions like checks the new
appointment against existing bookings for practitioner and time
conflicts and only add complex the new appointment to the list if no
clash is found. What I still need to understand is how cleanly it should
check for a duplicate practitioner without making the function.
