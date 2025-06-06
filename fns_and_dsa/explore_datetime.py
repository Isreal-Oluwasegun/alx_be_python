from datetime import datetime, timedelta

def display_current_dattime():
    current_date = datetime.now()
    return current_date

def calculate_future_date():
    days = int(input("Enter the number of days as iteger: "))
    future_date = datetime.now() + timedelta(days=days)
    return future_date

print(calculate_future_date())