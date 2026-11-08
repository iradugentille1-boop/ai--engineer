
applicants = [
    {"name": "Anna", "job": "Warehouse Worker", "status": "New"},
    {"name": "David", "job": "Cleaner", "status": "Reviewing"}
]


def show_applicants():
    print("\n--- All Applicants ---")

    for applicant in applicants:
        print(
            f"Name: {applicant['name']} | "
            f"Job: {applicant['job']} | "
            f"Status: {applicant['status']}"
        )


def add_applicant():
    print("\n--- Add a New Applicant ---")

    name = input("Enter applicant's name: ").strip()
    job = input("Enter the job they want: ").strip()

    if name == "" or job == "":
        print("Name and job cannot be empty.")
        return

    new_applicant = {
        "name": name,
        "job": job,
        "status": "New"
    }

    applicants.append(new_applicant)

    print(f"{name} has been added successfully!")


while True:
    print("\n=== Applicant Management ===")
    print("1. Show applicants")
    print("2. Add applicant")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        show_applicants()
    elif choice == "2":
        add_applicant()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
