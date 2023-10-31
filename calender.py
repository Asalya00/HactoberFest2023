import calendar

# Create a dictionary to store events
events = {}

def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

def add_event():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    event = input("Enter the event: ")

    date = f"{year}-{month:02d}-{day:02d}"
    
    if date in events:
        events[date].append(event)
    else:
        events[date] = [event]

def view_events():
    date = input("Enter the date (YYYY-MM-DD) to view events: ")
    
    if date in events:
        print(f"Events on {date}:")
        for event in events[date]:
            print(event)
    else:
        print("No events found for this date.")

while True:
    print("\nOptions:")
    print("1. Display Calendar")
    print("2. Add Event")
    print("3. View Events")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        display_calendar(year, month)
    elif choice == "2":
        add_event()
    elif choice == "3":
        view_events()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
