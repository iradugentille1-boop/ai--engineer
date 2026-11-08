
applicants = [
    {"name": "Anna", "job": "Warehouse Worker", "status": "New"},
    {"name": "David", "job": "Cleaner", "status": "Reviewing"},
    {"name": "Sarah", "job": "Hotel Assistant", "status": "New"},
    {"name": "Mchael", "job": "Delivery Driver", "status": "New"}
]


def show_applicants():
    print("\n--- All Applicants ---")

    for applicant in applicants:
        print(f"Name: {applicant['name']}")
        print(f"Job: {applicant['job']}")
        print(f"Status: {applicant['status']}")
        print("----------------------")


def find_new_applicants():
    print("\n--- New Applicants ---")

    for applicant in applicants:
        if applicant["status"] == "New":
            print(applicant["name"])


show_applicants()
find_new_applicants()
