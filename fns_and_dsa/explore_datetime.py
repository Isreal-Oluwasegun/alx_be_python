from datetime import date, timedelta

def display_current_datetime():
    current_date = date.today()
    return current_date

def calculate_future_date():
    days = int(input("Enter the number of days as iteger: "))
    future_date = date.today() + timedelta(days=days)
    return future_date

print(calculate_future_date())