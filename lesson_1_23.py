applicants = [
    {"name": "Anna", "job": "Warehouse Worker", "status": "New"},
    {"name": "David", "job": "Cleaner", "status": "Reviewing"},
    {"name": "Sarah", "job": "Hotel Assistant", "status": "New"}
]


def show_applicants():
    print("\n--- All Applicants ---")

    for applicant in applicants:
        print(
            f"Name: {applicant['name']} | "
            f"Job: {applicant['job']} | "
            f"Status: {applicant['status']}"
        )


def update_status():
    name = input("Enter the applicant's name: ").strip()

    for applicant in applicants:
        if applicant["name"].lower() == name.lower():
            print("Available statuses: New, Reviewing, Accepted")
            new_status = input("Enter the new status: ").strip().title()

            if new_status in ["New", "Reviewing", "Accepted"]:
                applicant["status"] = new_status
                print("Applicant status updated successfully!")
            else:
                print("Invalid status.")

            return

    print("Applicant not found.")


while True:
    print("\n=== Applicant Management ===")
    print("1. Show applicants")
    print("2. Update applicant status")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        show_applicants()
    elif choice == "2":
        update_status()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
