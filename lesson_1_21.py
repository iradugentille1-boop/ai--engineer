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


def show_new_applicants():
    print("\n--- New Applicants ---")

    for applicant in applicants:
        if applicant["status"] == "New":
            print(applicant["name"])   


def show__applicants():
    print("\n--- Reviewing Applicants ---")

    for applicant in applicants:
        if applicant["status"] == "Reviewing":
            print(applicant["name"])                      


while True:
    print("\n=== Applicant Management ===")
    print("1. Show all applicants")
    print("2. Show new applicants")
    print("3. Exit")
    print("4. show reviewing applicants")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_applicants()
    elif choice == "2":
        show_new_applicants()
    elif choice == "3":
        print("Goodbye!")
    elif choice == "4": 
        show_reviewing_applicants()   
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
