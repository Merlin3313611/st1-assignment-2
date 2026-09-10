# Comparison 

1. No user inputs-everything was hardcoded, meaning it books whatever is typed into the source cod, not what a real user enters, neither version takes input from actual users.
2. No memory Database- appointments just live only in memory such as appointment list while the program runs, meaning once teh program is closed everything is gone, there is no file, database or save option.
3. No duplicate,clash or double booking check-we could book two patients with the same practitioner at the same time and it wouldnt complain. book_appointment only checks that patient_name isn't empty.
4. No cancel or edit function-you can add appointments and display them but you cannot cancel teh time or look up a specific patient booking.
5. No error handling around teh raise-book_appointment raises ValueError, if the name is empty,but nothing in the script catches it, so an empty name would just crash the entire program 