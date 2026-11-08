from datetime import date

today = date(2026, 10, 22).today()
deadline = date(2026, 11, 15)

days_left = (deadline - today).days

if days_left > 0:
    print(f"You have {days_left} days left to apply.")
elif days_left == 0:
    print("The application deadline is today!")
else:
    print("The application deadline has passed.")
