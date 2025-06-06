from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date():
    days = int(input("Enter the number of days as iteger: "))
    current_date = display_current_datetime()
    future_date = current_date.date() + timedelta(days=days)
    return future_date

print(calculate_future_date())