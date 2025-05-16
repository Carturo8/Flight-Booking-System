# ✈️ Flight Booking System

### Versión en español
[Haz clic aquí para ver el README en español](https://github.com/Carturo8/Flight-Reservation-System/blob/main/README_ES.md)

---

This is a simple terminal-based **Flight Booking System** written in Python. It allows users to:

- Reserve available seats on predefined flights.
- View occupancy percentages for each flight.
- Export a sorted report with flight schedules and availability.
- Interact via a friendly text-based menu.

---

## 📁 Project Structure

```bash
flight_reservation/
├── flight_reservation.py # Main script
└── flight_schedule_report_example.txt # Auto-generated report file
```

---

## 🧰 Features

- ✅ **Seat Reservation**: Select a flight and reserve an available seat.
- 📊 **Occupancy Calculation**: View how full each flight is.
- 📝 **Report Generation**: Export a structured report sorted by departure time.
- 💬 **Interactive Menu**: Friendly command-line interface for user input.

---

## 🧪 Input Validation

- **Flight Code** must follow the format: `XX-123`.
- **Seat** must follow the format: Letter + 1 or 2 digits (e.g., `A1`, `D12`).

If an invalid format is entered, the system will show a warning and ask again.

---

## 🚀 How to Run

1. Make sure you have **Python 3.12** or later installed.
   
2. Clone this repository or download the script:

   - Using Git:
     ```bash
     git clone https://github.com/your-username/flight-reservation-system.git
     cd flight-reservation-system
     ```

   - Or download the ZIP file:
     
     1. Click on the green "Code" button above
     2. Select "Download ZIP"
     3. Extract the downloaded file
     4. Navigate to the extracted folder
 
3. Run the main script:

    ```bash
    python flight_reservation_system.py
    ```
    
---

## 💡 Usage Examples

### ✈️ Available Flights

The system starts with three preloaded flights:

| Flight Code | Origin   | Destination | Departure Time | Seats               |
|-------------|----------|-------------|----------------|---------------------|
| AV-201      | London   | Paris       | 09:45          | A1, A2, B1, B2, C1, C2 |
| AV-305      | New York | Miami       | 14:15          | A1, A2, B1, B2, E1, E2 |
| AV-408      | Tokyo    | Seoul       | 21:30          | A1, A2, B1, B2, D1, D2 |

### 📋 Sample Menu

Once the script runs, you'll see the main menu:

```bash
---------- ✈️ Flight Reservation System ----------

1. Reserve a seat
2. Calculate occupancy percentage per flight
3. Export sorted flights report
4.🚪 Exit

👉 Enter the number of the action you want to perform:
```

### ✅ Reserve a Seat

```bash
👉 Enter the number of the action you want to perform: 1

 -------------------- RESERVE A SEAT --------------------

Enter the flight code (format: XX-###): av-201

Available seats for flight AV-201: A1, A2, B1, B2, C1, C2

Enter the seat you wish to reserve (e.g., A1 or D12): a2

✅ Seat A2 has been successfully reserved for flight AV-201.

Would you like to reserve another seat? (y/n): n
```

### 📊 Calculate Occupancy Percentage

```bash
👉 Enter the number of the action you want to perform: 2

 -------- CALCULATE OCCUPANCY PERCENTAGE --------

Flight AV-201:
Total seats: 6 
Occupied seats: 1 
Occupancy rate: 16.67%

Flight AV-305:
Total seats: 6 
Occupied seats: 0 
Occupancy rate: 0.00%

Flight AV-408:
Total seats: 6 
Occupied seats: 0 
Occupancy rate: 0.00%
```

### 📝 Generate Report

```bash
👉 Enter the number of the action you want to perform: 3

 --------- EXPORT SORTED FLIGHTS REPORT ---------

✅ Flight schedule report has been generated successfully!
```

The file `flight_schedule_report_example.txt` will be created with detailed, sorted flight information, like:

```bash
FLIGHT SCHEDULE REPORT
==================================================

Flight Code: AV-201
Departure Time: 09:45
Origin: London
Destination: Paris
Available Seats: 5
Occupancy Rate: 16.67%

...

Report generated at: 2025-05-16 10:42:31
```

---

## 🛠️ Technologies Used

- Python 3.
- Standard Libraries:
  - `copy` for data integrity.
  - `re` for regex-based input validation.
  - `datetime` for timestamping reports.

---

## 📜 License

This project is licensed under the [MIT License](https://github.com/Carturo8/Flight-Reservation-System/blob/main/LICENSE).
