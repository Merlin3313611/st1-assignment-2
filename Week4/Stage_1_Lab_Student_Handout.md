# Learning objectives

- Create and run a simple Python file with basic input,output and
  processing statements

- Use lists, dictionaries and functions to enhance the Python file

- Build a small SmartCare appointment prototype.

- Use AI as a tutor rather than a replacement.

- Compare human-written and AI-generated code.

- Verify AI-generated code through execution and test inputs.

- Document a short AI-use reflection.

# Files to create and commit in GitHub

stage01/  
smartcare_v01.py  
comparison.md  
reflection.md  
ai_usage.md

# Part A - Understand the Problem: AI OFF

SmartCare needs a small prototype that allows a receptionist to record
patient appointments. Each appointment records patient name,
practitioner name and appointment time.

What data must be stored?

Ans:

- Patient name

- Practitioner name

- Appointment date and time

- Appointment type

What functions might be useful?

Ans:

- A function to book or add new appointments.

- A function to display all recorded appointments.

- Functions to cancel or edit an appointment.

What could go wrong?

Ans:

- Double Booking

- Duplicate patient names can create confusion

- Data may get lost easily

- Is the appointment confirmation meant to be free text, or does it need
  a strict date or time format

What requirements are unclear?

Ans:

- Can one patient hold multiple simultaneous appointments

- Is the appointment time meant to be a text format, or does it need to
  have a strict date and time format?

- What counts as a duplicate appointment, and should the system prevent
  it?

# Part B - Build a Human-Written Prototype: AI OFF

**\#task 1**

**\# Create and run a simple Python file with basic input,output
statements**

**print("Welcome to SmartCare: Community Clinic Appointment Booking
System!")**

**\# First Appointment**

**patient1_name = 'Alice Smith'**

**practitioner1_name = 'Dr. John Doe'**

**appointment1_time = '2024-07-20 10:00 AM'**

**print(f"Patient: {patient1_name} \| Practitioner: {practitioner1_name}
\| Time: {appointment1_time}")**

**\# Second Appointment**

**patient2_name = 'Bob Johnson'**

**practitioner2_name = 'Dr. Jane Roe'**

**appointment2_time = '2024-07-20 11:30 AM'**

**print(f"Patient: {patient2_name} \| Practitioner: {practitioner2_name}
\| Time: {appointment2_time}")**

**\#task1enhanced**

**\# Use lists, dictionaries and functions to enhance the Python file**

**appointments = \[\]**

**def book_appointment(patient_name, practitioner_name,
appointment_time):**

**    if not patient_name:**

**        raise ValueError("Patient name cannot be empty")**

**    appointment = {**

**        "patient": patient_name,**

**        "practitioner": practitioner_name,**

**        "time": appointment_time**

**    }**

**    appointments.append(appointment)**

**def display_appointments():**

**    if not appointments:**

**        print("No appointments recorded.")**

**        return**

**    for appointment in appointments:**

**        print(f"Patient: {appointment\['patient'\]} \| Practitioner:
{appointment\['practitioner'\]} \| Time: {appointment\['time'\]}")**

**print("Welcome to SmartCare: The Clinical Appointment Booking
System!")**

**book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00
AM')**

**book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30
AM')**

**display_appointments()**

^ Now, run both programs , and identify at least five limitations.

- Comparison part is in the comparision.md file

# Part C - Use AI as Tutor: AI ON (Use only UC approved GenAI Tool such as Microsoft CoPilot)

<u>Suggested prompt structure:</u>  
Act as a Python tutor.  
I am learning introductory software technology.  
Here is a small appointment-booking function.  
1. Explain what the code does.  
2. Identify three limitations.  
3. Suggest improvements.  
4. Do not rewrite the whole application.  
5. Ask me two questions to test my understanding.  
  
-answer as AI tutor is in ai_usage.md file

# Part D - Generate an Alternative: AI ON

Ask AI to create a simple beginner-friendly Python function that stores
patient name, practitioner name and appointment time. Explicitly
prohibit a database or GUI.  
  
- Code is in smartcare_v01

# Part E - Compare Human and AI Versions

| Question                         | Human version                                                                | AI version                                                                                                                                                     |
|----------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Easy to understand?**          | Yes, it was a simple list of dictionaries with two clear functions           | Yes, though it introduced a few extra concepts (e.g. more detailed error handling) that took a moment to follow                                                |
| **Runs successfully?**           | Yes, once tested with normal input                                           | Yes                                                                                                                                                            |
| **Uses only required features?** | Yes, only patient name, practitioner name, and time, no database or GUI      | Mostly, stayed within the constraints given in the prompt (no database, no GUI)                                                                                |
| **Adds assumptions?**            | No extra assumptions, but only checked patient name for emptiness originally | Yes, assumed practitioner name and appointment time should also be validated, and suggested checking for duplicate bookings, which wasn't explicitly requested |
| **Handles errors?**              | Only handled empty patient name in the original version                      | Handled empty patient name, practitioner name, and time, plus flagged the duplicate-booking gap                                                                |
| **Could I explain it?**          | Yes; it's simple code                                                        | Mostly yes, after reviewing it against the human version; the validation logic was the same idea just applied more broadly                                     |

# Part F - Verify Behavior

- Test 1: Normal appointment

<!-- -->

- input: patient name="Alice Smith", practitioner name="Dr. John Doe",
  appointment time="2024-07-20 10:00 AM"

- output: The appointment booking was successfully

  Standard response.

<!-- -->

- Test 2: Blank patient name

<!-- -->

- input: patient name="", practitioner name="Dr. John Doe", appointment
  time="2024-07-20 10:00 AM"

- output: ValueError as the patient name cannot be empty

  Error handling response.

<!-- -->

- Test 3: Two appointments for the same practitioner/time

<!-- -->

- input: patient name="Bob Johnson", practitioner name="Dr. Jane Roe",
  appointment time="2024-07-20 11:30 AM"

- output: The appointment booking was successfully!

- input: patient name="Ram Prasad", practitioner name="Dr. Jane Roe",
  appointment time="2024-07-20 11:30 AM"

  output: The appointment booking was successfully.

  Despite the clash the appointment was booked so error was not handled.

<!-- -->

- Test 4: Strange input (None values)

<!-- -->

- input: patient name=” ”, practitioner name="Dr. John Doe", appointment
  time="2024-07-20 10:00 AM"

- output: ValueError as the patient name cannot be empty

  Error handling response.

# Part G - Improve One Thing

Choose exactly one controlled improvement, for example: if not
patient_name: raise ValueError("Patient name cannot be empty")

\- I added one controlled improvement to the program: validation for
empty patient names.

Previously, the program allowed an appointment to be created even if the
patient name was blank.

I improved the \`book_appointment()\` function by adding:

if not patient_name:

raise ValueError("Patient name cannot be empty")

# Part H - Reflection (150-250 words)

What did you build before using AI?

What did AI help you understand?

Did AI make assumptions?

How did you verify the AI output?

What engineering work remained for you?

# Submission checklist \[GitHub Commit\]

- Python file runs.

- Comparison table completed.

- Normal and unusual inputs tested.

- AI assistance documented.

- Reflection completed.

- I can explain my code.
