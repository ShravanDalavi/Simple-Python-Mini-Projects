import datetime
import time

alarm_time = input("Enter the time for the alarm in 'HH:MM' format: ")
alarm_hour, alarm_minute = map(int, alarm_time.split(':'))

while True:
    now = datetime.datetime.now()
    current_hour, current_minute = now.hour, now.minute
    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("Time to wake up!")
        break
    time.sleep(60)  # check every minute
