import copy
import re
import datetime

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
flights_copy = copy.deepcopy(flights)
reserved_seats:dict = {}


def validate_code() -> str:
    pattern:str = r"^[A-Z]{2}-[0-9]{3}$"
    while True:
        code:str = input("\nEnter the flight code (format: XX-###): ")
        if re.match(pattern, code):
            return code
        print("\033[93m⚠️ Invalid format. Use two uppercase letters, dash, and three numbers (e.g., AV-123)\033[0m")


def validate_seat() -> str:
    condition:bool = True
    seat:str = ""
    while condition:
        seat = input(f"\nEnter the seat you wish to reserve (e.g., A1 or D2): ")
        if not re.match(r"^[A-Z][0-9]$", seat):
            print("\033[93m⚠️ A uppercase letter followed by a number must be entered.\033[0m")
        else:
            condition = False
    return seat


def validate_seat() -> str:
    pattern:str = r"^[A-Z][0-9]$"
    while True:
        seat:str = input("\nEnter the seat you wish to reserve (e.g., A1 or D12): ").strip().upper()
        if not seat_pattern.match(seat):
            print("\033[93m⚠️ You must enter an uppercase letter followed by a single number (e.g., A1).\033[0m")
        else:
            return seat


def validate_time() -> tuple[int, int]:
    condition:bool = True
    time:tuple[int, int] = (0, 0)
    while condition:
        try:
            time_str:str = (input("\nEnter flight time (HH(0-23), MM(0-59) format): "))
            time_dt:datetime = datetime.datetime.strptime(time_str, "%H, %M")
            time = (time_dt.hour, time_dt.minute)
            condition = False
        except ValueError:
            print("\033[91m❌ Invalid time format. Use HH, MM format (example: 13, 30)\033[0m")
    return time


def reserve_seats() -> None:
    while True:  # Main loop for multiple reservations
        flight_code:str = validate_code()

        if flight_code not in flights.keys():
            print(f"\033[93m⚠️ Flight code {flight_code} not found. Please try again.\033[0m")
            continue

        # Loop to handle seat reservation for the selected flight
        while True:
            print(f"\033[96m\nThe available seats for {flight_code} are: {', '.join(flights_copy[flight_code]['seats'])}\033[0m")
            seat:str = validate_seat()

            if seat not in flights_copy[flight_code]['seats']:
                print(f"\033[91m❌ The seat {seat} is not available. Please try again.\033[0m")
                continue

            # Reserve the seat
            flights_copy[flight_code]['seats'].remove(seat)

            # Initialize the list if it's the first seat for this flight
            if flight_code not in reserved_seats:
                reserved_seats[flight_code]:list = []

            reserved_seats[flight_code].append(seat)
            print(f"\033[92m\nSeat {seat} reserved for {flight_code} flight.\033[0m")
            break  # Exit seat selection loop

        # Ask if a user wants to reserve more seats
        print(f"\033[93m\nDo you want to reserve another seat? (y/n): \033[0m", end="")
        if input().strip().lower() != 'y':
            break


def calculate_occupancy_percentage_per_flight() -> None:
    for flight_code, flight_data in flights.items():  # Use original flights dict for total seats count
        total_seats:int = len(flight_data['seats'])
        occupied_seats:int = 0

        # Check if there are any reserved seats for this flight
        if flight_code in reserved_seats:
            occupied_seats:int = len(reserved_seats[flight_code])

        # Calculate the occupancy percentage
        occupancy_percentage:float = (occupied_seats / total_seats) * 100

        print(f"\033[96m\nFlight {flight_code}:\033[0m")
        print(f"""\033[92mTotal seats: {total_seats} 
        \rOccupied seats: {occupied_seats} 
        \rOccupancy percentage: {occupancy_percentage:.2f}%\033[0m""")


def generate_flight_schedule_report():
    # Sort flights by departure time
    sorted_flights = dict(sorted(flights.items(),
                                 key = lambda x: x[1]['time']))

    try:
        # Open a file in writing mode with UTF-8 encoding
        with open('flight_schedule_report.txt', 'w', encoding = 'utf-8') as file:
            file.write("FLIGHT SCHEDULE REPORT\n")
            file.write("=" * 50 + "\n\n")

            for flight_code, flight_data in sorted_flights.items():
                # Calculate occupancy for this flight
                total_seats = len(flight_data['seats'])
                occupied_seats = len(reserved_seats.get(flight_code, []))
                occupancy_percentage = (occupied_seats / total_seats) * 100

                # Write flight information
                file.write(f"Flight Code: {flight_code}\n")
                file.write(f"Departure Time: {flight_data['time'][0]:02d}:{flight_data['time'][1]:02d}\n")
                file.write(f"Origin: {flight_data['origin']}\n")
                file.write(f"Destination: {flight_data['destination']}\n")
                file.write(f"Available Seats: {len(flights_copy[flight_code]['seats'])}\n")
                file.write(f"Occupancy: {occupancy_percentage:.2f}%\n")
                file.write("-" * 50 + "\n\n")

            file.write("\nReport generated at: " +
                       datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        print("\033[92m✅ Flight schedule report has been generated successfully!\033[0m")

    except Exception as e:
        print(f"\033[91m❌ Error generating report: {str(e)}\033[0m")


def menu() -> str:
    print("\033[96m\n---------- 📊 Reservation Flight System ----------\033[0m")
    print("""\n1. Reserve seat
           \r2. Calculate occupancy percentage per flight
           \r3. Export sorted flights report
           \r4.🚪 Exit""")
    option:str = input("\n👉 Enter the number of the action you want to perform: ")
    return option


def main() -> None:
    condition:bool = True
    while condition:
        option:str = menu()

        if option == "1":
            print("\033[96m\n -------------------- RESERVE SEAT --------------------\033[0m")
            reserve_seats()

        elif option == "2":
            print("\033[96m\n ----------------- CALCULATE OCCUPANCY PERCENTAGE ------------------\033[0m")
            calculate_occupancy_percentage_per_flight()

        elif option == "3":
            print("\033[96m\n ------------------ EXPORT SORTED FLIGHTS REPORT -------------------\033[0m")
            generate_flight_schedule_report()

        elif option == "4":
            condition = False
            print("\033[92m\n👋 Thank you for using the Reservation Flight System. Goodbye!\033[0m")
        else:
            print("\033[91m\n❌ Invalid option. Please enter a number between 1 and 4.\033[0m")


if __name__ == "__main__":
    main()

















