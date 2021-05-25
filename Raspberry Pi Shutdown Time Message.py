"""
This script is supposed to run with the telegram-boot-alert script for the Raspberry Pi.
"""
import datetime

now = datetime.datetime.now()
current_day = now.strftime("%A")
current_hour = now.strftime("%H")
current_minute = now.strftime("%M")

if current_day == "Saturday":
    time_on = 16
    shutdown_hour = int(current_hour) + time_on
    if shutdown_hour >= 24 and shutdown_hour < 36:
        am_or_pm = "AM"
    elif shutdown_hour < 24 or shutdown_hour >= 36:
        am_or_pm = "PM"
        shutdown_hour = shutdown_hour - 12
    if shutdown_hour >= 24:
        shutdown_hour = shutdown_hour - 24
        if shutdown_hour == 0:
            shutdown_hour = 12
    shutdown_time = f"{shutdown_hour}:{current_minute}{am_or_pm}"
    print(f"Today is {current_day}, I will automatically shutdown at {shutdown_time}")
elif current_day == "Sunday":
    time_on = 16
    shutdown_hour = int(current_hour) + time_on
    if shutdown_hour >= 24 and shutdown_hour < 36:
        am_or_pm = "AM"
    elif shutdown_hour < 24 or shutdown_hour >= 36:
        am_or_pm = "PM"
        shutdown_hour = shutdown_hour - 12
    if shutdown_hour >= 24:
        shutdown_hour = shutdown_hour - 24
        if shutdown_hour == 0:
            shutdown_hour = 12
    shutdown_time = f"{shutdown_hour}:{current_minute}{am_or_pm}"
    print(f"Today is {current_day}, I will automatically shutdown at {shutdown_time}")
elif current_day == "Monday":
    time_on = 5
    shutdown_hour = int(current_hour) + time_on
    if shutdown_hour >= 24 and shutdown_hour < 36:
        am_or_pm = "AM"
    elif shutdown_hour < 24 or shutdown_hour >= 36:
        am_or_pm = "PM"
        shutdown_hour = shutdown_hour - 12
    if shutdown_hour >= 24:
        shutdown_hour = shutdown_hour - 24
        if shutdown_hour == 0:
            shutdown_hour = 12
    shutdown_time = f"{shutdown_hour}:{current_minute}{am_or_pm}"
    print(f"Today is {current_day}, I will automatically shutdown at {shutdown_time}")
elif current_day == "Tuesday":
    time_on = 5
    shutdown_hour = int(current_hour) + time_on
    if shutdown_hour >= 24 and shutdown_hour < 36:
        am_or_pm = "AM"
    elif shutdown_hour < 24 or shutdown_hour >= 36:
        am_or_pm = "PM"
        shutdown_hour = shutdown_hour - 12
    if shutdown_hour >= 24:
        shutdown_hour = shutdown_hour - 24
        if shutdown_hour == 0:
            shutdown_hour = 12
    shutdown_time = f"{shutdown_hour}:{current_minute}{am_or_pm}"
    print(f"Today is {current_day}, I will automatically shutdown at {shutdown_time}")
elif current_day == "Wednesday":
    time_on = 5
    shutdown_hour = int(current_hour) + time_on
    if shutdown_hour >= 24 and shutdown_hour < 36:
        am_or_pm = "AM"
    elif shutdown_hour < 24 or shutdown_hour >= 36:
        am_or_pm = "PM"
        shutdown_hour = shutdown_hour - 12
    if shutdown_hour >= 24:
        shutdown_hour = shutdown_hour - 24
        if shutdown_hour == 0:
            shutdown_hour = 12
    shutdown_time = f"{shutdown_hour}:{current_minute}{am_or_pm}"
    print(f"Today is {current_day}, I will automatically shutdown at {shutdown_time}")
elif current_day == "Thursday":
    time_on = 5
    shutdown_hour = int(current_hour) + time_on
    if shutdown_hour >= 24 and shutdown_hour < 36:
        am_or_pm = "AM"
    elif shutdown_hour < 24 or shutdown_hour >= 36:
        am_or_pm = "PM"
        shutdown_hour = shutdown_hour - 12
    if shutdown_hour >= 24:
        shutdown_hour = shutdown_hour - 24
        if shutdown_hour == 0:
            shutdown_hour = 12
    shutdown_time = f"{shutdown_hour}:{current_minute}{am_or_pm}"
    print(f"Today is {current_day}, I will automatically shutdown at {shutdown_time}")
elif current_day == "Friday":
    time_on = 5
    shutdown_hour = int(current_hour) + time_on
    if shutdown_hour >= 24 and shutdown_hour < 36:
        am_or_pm = "AM"
    elif shutdown_hour < 24 or shutdown_hour >= 36:
        am_or_pm = "PM"
        shutdown_hour = shutdown_hour - 12
    if shutdown_hour >= 24:
        shutdown_hour = shutdown_hour - 24
        if shutdown_hour == 0:
            shutdown_hour = 12
    shutdown_time = f"{shutdown_hour}:{current_minute}{am_or_pm}"
    print(f"Today is {current_day}, I will automatically shutdown at {shutdown_time}")
