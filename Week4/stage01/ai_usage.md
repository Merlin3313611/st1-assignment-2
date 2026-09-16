# AI Usage (AI ON)

## **1. What the code does**
The program prints a welcome message and displays two appointments using simple variables.

In the enhanced version, it introduces:

### **`appointments` list**
A list that stores all booked appointments as dictionaries.

### **`book_appointment()` function**
- Validates that the patient name is not empty.  
- Creates a dictionary with:
  - `"patient"`
  - `"practitioner"`
  - `"time"`
- Appends the dictionary to the `appointments` list.

### **`display_appointments()` function**
- Checks if the list is empty.  
- If not, loops through each appointment and prints the details.

Finally, the program books two sample appointments and displays them.

---

## **2. Three limitations**
1. **Only patient name is validated**  
   Practitioner name and appointment time could be empty or invalid.

2. **No double‑booking protection**  
   A practitioner could be booked twice at the same time.

3. **No user interaction**  
   All appointments are hard‑coded; users cannot enter new ones.

---

## **3. Suggested improvements**
- Add validation for practitioner name and appointment time.  
- Add a check to prevent double‑booking the same practitioner at the same time.  
- Add user input (`input()`) so appointments can be entered interactively.  
- Add time formatting or parsing to ensure consistent appointment times.

---

## **4. No rewrite provided**
Only explanations and suggestions — the application is unchanged.

---

## **5. Two questions to test your understanding**
1. Why is a list of dictionaries more flexible than using separate variables for each appointment?  
2. What issue might occur if the system allows a practitioner to be booked for two appointments at the same time?

