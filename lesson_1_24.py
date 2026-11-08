applicants = [
    {"name": "Alice", "skills": ["Python", "SQL"], "score": 85},
    {"name": "David", "skills": ["Excel", "Power BI"], "score": 72},
    {"name": "Sarah", "skills": ["Python", "Machine Learning"], "score": 92},
    {"name": "John", "skills": ["SQL", "Python"], "score": 60}
]


def show_applicants():
    print("\n--- All Applicants ---")

    for applicant in applicants:
        print(
            f"Name: {applicant['name']} | "
            f"Skills: {', '.join(applicant['skills'])} | "
            f"Score: {applicant['score']}"
        )


def find_python_applicants():
    print("\n--- Applicants with Python Skills ---")

    for applicant in applicants:
        if "Python" in applicant["skills"]:
            print(applicant["name"])


def analyze_scores():
    scores = [applicant["score"] for applicant in applicants]

    average = sum(scores) / len(scores)
    highest = max(scores)

    print(f"\nAverage score: {average:.2f}")
    print(f"Highest score: {highest}")


def find_high_scores():
    print("\n--- High scores (80 or higher) ---")
    for applicant in applicants:
        if applicant["score"] >= 80:
            print(f"Name: {applicant['name']} | score: {applicant['score']}")

def find_low_scores():
    print("\n--- Low scores (65 or lower)---")
    for applicant in applicants:
        if applicant ["score"] <= 65:
            print(f"Name: {applicant['name']} | score: {applicant['score']}")
scores = [applicant["score"] for applicant in applicants]    
lowest = min(scores)
print(f"\nLowest score is: {lowest}")       


show_applicants()
find_python_applicants()
analyze_scores()
find_high_scores()
find_low_scores()