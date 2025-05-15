import re
from datetime import datetime

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
flights_2 = flights.copy()
reserved_seats:dict = {}

def validate_code() -> str:
    condition:bool = True
    code:str = ""
    while condition:
        code = input("\nEnter the flight code (format: XX-###): ")
        if not re.match(r"^[A-Z]{2}-[0-9]{3}$", code):
            print("\033[93m⚠️ Invalid format. Use two uppercase letters, dash, and three numbers (e.g., AV-123)\033[0m")
        else:
            condition = False
    return code

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

def validate_time() -> tuple[int, int]:
    condition: bool = True
    time:tuple[int, int] = (0, 0)
    while condition:
        try:
            time_str:str = (input("\nEnter flight time (HH(0-23), MM(0-59) format): "))
            time_dt:datetime = datetime.strptime(time_str, "%H, %M")
            time = (time_dt.hour, time_dt.minute)
            condition = False
        except ValueError:
            print("\033[91m❌ Invalid time format. Use HH, MM format (example: 13, 30)\033[0m")
    return time

# def validate_city() -> str:
#     condition:bool = True
#     origin:str = ""
#     while condition:
#         origin = " ".join(input("\nEnter the origin city: ").split())
#         if len(origin) > 25:
#             print("\033[91m❌ The origin city must not exceed 25 characters.\033[0m")
#         elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", origin):
#             print("\033[93m⚠️ Only letters and spaces are allowed (including accents like á, é, ñ).\033[0m")
#         else:
#             condition = False
#     return origin

def reserve_seats() -> dict:
    condition:bool = True
    while condition:

        flight_code:str = validate_code()

        if flight_code in flights.keys():
            print(f"\nThe available seats for {flight_code} are: {', '.join(flights_2[flight_code]['seats'])}")
            seat:str = validate_seat()

            if seat in flights_2[flight_code]['seats']:
                flights_2[flight_code]['seats'].remove(seat)
                reserved_seats[flight_code]:list = []
                reserved_seats[flight_code].append(seat)
                print(f"\nSeat {seat} reserved for {flight_code} flight.")
                condition = False
            else:
                print(f"\nThe seat {seat} is not available. Please try again.")

        else:
            print(f"\nFlight code {flight_code} not found. Please try again.")
    return reserved_seats

def calculate_occupancy_percentage_per_flight():
    for flight_code, flight_data in flights.items():
        if flight_code in reserved_seats.keys():
            print(f"\nFlight {flight_code} occupancy percentage: {len(reserved_seats[flight_code]) / len(flight_data['seats']) * 100:.2f}%")
        else:
            print(f"\nFlight {flight_code} occupancy percentage: 0%")

def continue_or_exit() -> bool:
    condition:bool = True
    while condition:
        option:str = input(f"\033[93m\nPress 'y' to continue / any other key to return to menu): \033[0m").lower()
        if option == "yes":
            condition = False
        elif option == "no":
            condition = False
            return False

def menu() -> str:
    print("\033[96m\n---------- 📊 Reservation Flight System ----------\033[0m")
    print("""
1. Reserve seat
2. Calculate occupancy percentage per flight
3. Export sorted flights report
4.🚪 Exit
    """)
    option:str = input("👉 Enter the number of the action you want to perform: ")
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
            print(reserved_seats)

        elif option == "3":
            print("\033[96m\n ------------------ EXPORT SORTED FLIGHTS REPORT -------------------\033[0m")

        elif option == "4":
            condition = False
            print("\033[92m\n👋 Thank you for using the Reservation Flight System. Goodbye!\033[0m")
        else:
            print("\033[91m\n❌ Invalid option. Please enter a number between 1 and 4.\033[0m")


if __name__ == "__main__":
    main()

















