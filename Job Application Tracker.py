import csv
import os


def create_csv_file(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Company", "Position", "Status", "Notes"])


def add_application(file_name, date, company, position, status, notes):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, company, position, status, notes])


def view_applications(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Date:", row[0])
            print("Company:", row[1])
            print("Position:", row[2])
            print("Status:", row[3])
            print("Notes:", row[4])
            print("=" * 40)


def main():
    file_name = "job_applications.csv"

    if not os.path.exists(file_name):
        create_csv_file(file_name)

    while True:
        print("\nJob Application Tracker")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            company = input("Enter company name: ")
            position = input("Enter position applied for: ")
            status = input("Enter application status: ")
            notes = input("Enter notes (optional): ")
            add_application(file_name, date, company, position, status, notes)
            print("Application added successfully.")
        elif choice == "2":
            print("\nAll Applications:")
            view_applications(file_name)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
