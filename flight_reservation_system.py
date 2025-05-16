# Import the necessary standard libraries
import copy    # To create deep copies of complex data structures
import re      # For regular expression operations (input validation)
import datetime  # For handling date and time, used in report generation

# Dictionary containing flight data with details such as origin, destination, available seats, and departure time
flights:dict = {
    "AV-201": {
        "origin": "London",
        "destination": "Paris",
        "seats": ["A1", "A2", "B1", "B2", "C1", "C2"],
        "time": (9, 45)
    },
    "AV-305": {
        "origin": "New York",
        "destination": "Miami",
        "seats": ["A1", "A2", "B1", "B2", "E1", "E2"],
        "time": (14, 15)
    },
    "AV-408": {
        "origin": "Tokyo",
        "destination": "Seoul",
        "seats": ["A1", "A2", "B1", "B2", "D1", "D2"],
        "time": (21, 30)
    }
}

# Deep copy of flight dictionary to keep track of available seats without altering original data
flights_copy:dict = copy.deepcopy(flights)

# Dictionary to store reserved seats per flight (keys are flight codes, values are lists of reserved seat IDs)
reserved_seats:dict = {}


def validate_code() -> str:
    """
    Prompts the user to enter a flight code in the format XX-###.

    The code must consist of two uppercase letters, a dash, and three digits (e.g., AV-123).
    The input is automatically converted to uppercase to ensure it matches the pattern.

    Returns:
        str: A valid flight code that matches the required format.
    """
    pattern:str = r"^[A-Z]{2}-[0-9]{3}$"
    while True:
        code:str = input("\nEnter the flight code (format: XX-###): ").upper()
        if re.match(pattern, code):
            return code
        print("\033[93m⚠️ Invalid format. Please enter two letters, a dash, and three digits (e.g., AV-123).\033[0m")


def validate_seat() -> str:
    """
    Prompts the user to enter a seat identifier in the format Letter+Number (e.g., A1 or D12).

    The input is automatically converted to uppercase and validated using a regex pattern.

    Returns:
        str: A valid seat identifier.
    """
    pattern:str = r"^[A-Z][0-9]{1,2}$"  # Seat must start with a letter followed by 1 or 2 digits (e.g., A1, D12)
    while True:
        seat:str = input("\nEnter the seat you wish to reserve (e.g., A1 or D12): ").strip().upper()
        if re.match(pattern, seat):
            return seat
        else:
            print("\033[93m⚠️ Invalid format. Use a letter followed by one or two digits (e.g., A1 or D12).\033[0m")


def reserve_seats() -> None:
    """
    Handles the seat reservation process for a selected flight.

    The user is prompted to enter a valid flight code and then select an available seat.
    Reserved seats are stored in a dictionary, and the flight's available seat list is updated accordingly.
    """
    while True:  # Main loop for multiple reservations
        flight_code:str = validate_code()

        if flight_code not in flights:
            print(f"\033[91m❌ Flight code '{flight_code}' not found. Please try again.\033[0m")
            continue

        # Sub-loop to handle seat reservation for the selected flight
        while True:
            print(f"\033[96m\nAvailable seats for flight {flight_code}: {', '.join(flights_copy[flight_code]['seats'])}\033[0m")
            seat:str = validate_seat()

            if seat not in flights_copy[flight_code]['seats']:
                print(f"\033[91m❌ Seat {seat} is not available. Please try a different one.\033[0m")
                continue

            # Remove the reserved seat from the copy
            flights_copy[flight_code]['seats'].remove(seat)

            # Initialize the seat list if first reservation for this flight
            if flight_code not in reserved_seats:
                reserved_seats[flight_code]: list = []

            reserved_seats[flight_code].append(seat)
            print(f"\033[92m✅ Seat {seat} has been successfully reserved for flight {flight_code}.\033[0m")
            break  # Exit inner seat reservation loop

        # Ask a user if they want to make another reservation
        print(f"\033[93m\nWould you like to reserve another seat? (y/n): \033[0m", end="")
        if input().strip().lower() != 'y':
            break


def calculate_occupancy_percentage_per_flight() -> None:
    """
    Calculates and displays the seat occupancy percentage for each flight.

    For every flight in the system, this function compares the number of reserved seats
    with the total number of seats to calculate the occupancy rate.
    The results are printed to the console.
    """
    for flight_code, flight_data in flights.items():  # Use the original dict to get the total seat count
        total_seats:int = len(flight_data['seats'])
        occupied_seats:int = 0

        # Check if any seats have been reserved for this flight
        if flight_code in reserved_seats:
            occupied_seats:int = len(reserved_seats[flight_code])

        # Calculate the percentage of seats that are occupied
        occupancy_percentage:float = (occupied_seats / total_seats) * 100

        # Display the occupancy information
        print(f"\033[96m\nFlight {flight_code}:\033[0m")
        print(f"""\033[92mTotal seats: {total_seats} 
        \rOccupied seats: {occupied_seats} 
        \rOccupancy rate: {occupancy_percentage:.2f}%\033[0m""")


def generate_flight_schedule_report() -> None:
    """
    Generates a text report with flight information sorted by departure time.

    The report includes:
    - Flight code
    - Departure time
    - Origin and destination
    - Number of available seats
    - Occupancy rate

    The report is saved as 'flight_schedule_report.txt' in UTF-8 encoding.
    """
    # Sort flights by departure time (hour, minute)
    sorted_flights = dict(sorted(flights.items(), key=lambda x: x[1]['time']))

    try:
        # Open the output file in writing mode using UTF-8 encoding
        with open('flight_schedule_report.txt', 'w', encoding='utf-8') as file:
            file.write("FLIGHT SCHEDULE REPORT\n")
            file.write("=" * 50 + "\n\n")

            for flight_code, flight_data in sorted_flights.items():
                # Calculate total and reserved seats for the flight
                total_seats = len(flight_data['seats'])
                occupied_seats = len(reserved_seats.get(flight_code, []))
                occupancy_percentage = (occupied_seats / total_seats) * 100

                # Write all flight information into the report
                file.write(f"Flight Code: {flight_code}\n")
                file.write(f"Departure Time: {flight_data['time'][0]:02d}:{flight_data['time'][1]:02d}\n")
                file.write(f"Origin: {flight_data['origin']}\n")
                file.write(f"Destination: {flight_data['destination']}\n")
                file.write(f"Available Seats: {len(flights_copy[flight_code]['seats'])}\n")
                file.write(f"Occupancy Rate: {occupancy_percentage:.2f}%\n")
                file.write("-" * 50 + "\n\n")

            # Add a timestamp at the end of the report
            file.write("\nReport generated at: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        print("\033[92m\n✅ Flight schedule report has been generated successfully!\033[0m")

    except Exception as e:
        print(f"\033[91m❌ Error generating report: {str(e)}\033[0m")


def menu() -> str:
    """
    Displays the main menu and prompts the user to select an option.

    Returns:
        str: The selected option as a string.
    """
    print("\033[96m\n---------- 📊 Flight Reservation System ----------\033[0m\n")
    print("""1. Reserve a seat
           \r2. Calculate occupancy percentage per flight
           \r3. Export sorted flights report
           \r4.🚪 Exit""")

    # Prompt the user to select a menu option
    option:str = input("\n👉 Enter the number of the action you want to perform: ")
    return option


def main() -> None:
    """
    Main function that runs the flight reservation system.
    Handles user interaction through a menu and executes the selected action.
    """
    running: bool = True
    while running:
        try:
            option:str = menu()

            if option == "1":
                print("\033[96m\n -------------------- RESERVE A SEAT --------------------\033[0m")
                reserve_seats()

            elif option == "2":
                print("\033[96m\n -------- CALCULATE OCCUPANCY PERCENTAGE --------\033[0m")
                calculate_occupancy_percentage_per_flight()

            elif option == "3":
                print("\033[96m\n --------- EXPORT SORTED FLIGHTS REPORT ---------\033[0m")
                generate_flight_schedule_report()

            elif option == "4":
                # Exit the program
                running = False
                print("\033[92m\n👋 Thank you for using the Flight Reservation System. Goodbye!\033[0m")

            else:
                # Invalid option entered by the user
                print("\033[91m\n❌ Invalid option. Please enter a number between 1 and 4.\033[0m")

        except KeyboardInterrupt:
            # Handles user interruption (Ctrl+C)
            print("\n\033[91m\n❌ Program interrupted. Exiting...\033[0m")
            running = False


# Run the main function only if this script is executed directly (not imported as a module)
if __name__ == "__main__":
    main()