from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime('%Y-%m-%d %H:%M:%S')

def calculate_future_date():
    days = int(input("Enter the number of days as iteger: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')

print(display_current_datetime())