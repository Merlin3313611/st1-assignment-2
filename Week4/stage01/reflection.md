# Reflection

Before using AI, I built a very simple human-written prototype that stored two hard‑coded appointments and printed them. It worked, but it had no validation, no structure, and no way to detect mistakes such as duplicate bookings. Writing it myself helped me understand the basic data needed: patient name, practitioner name, and appointment time.

AI helped me understand how to organise the code into functions, how to validate inputs properly, and how to think about edge cases such as blank names or strange time formats. It also highlighted limitations I hadn’t considered, like duplicate bookings for the same practitioner and time. The AI did make some assumptions, such as suggesting extra validation and time parsing, but these were reasonable and easy to adapt.

To verify the AI output, I ran the program with normal inputs, blank names, duplicate bookings, and `None` values. I checked that errors were raised correctly and that the appointment list updated as expected. Even with AI assistance, I still had to test, adjust, and integrate the code myself. The engineering work- debugging, verifying behaviour, and making sure the program met the assignment constraints—remained my responsibility.
