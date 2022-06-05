def add_time(start, duration, day=None):
    """
    Write a function named add_time that takes in two required parameters and one optional parameter:

    a start time in the 12-hour clock format (ending in AM or PM)
    a duration time that indicates the number of hours and minutes
    (optional) a starting day of the week, case-insensitive
    The function should add the duration time to the start time and return the result.

    If the result will be the next day, it should show (next day) after the time.
    If the result will be more than one day later, it should show (n days later) after the time,
     where "n" is the number of days later.

    If the function is given the optional starting day of the week parameter, then the output should display the day
    of the week of the result. The day of the week in the output should appear
    after the time and before the number of days later.
    """
    isam = start.split()[1] == "AM"
    st_hour = int(start.split()[0].split(":")[0])
    st_min = int(start.split()[0].split(":")[1])

    end_hour = int(duration.split(":")[0])
    end_min = int(duration.split(":")[1])

    new_min = (st_min + end_min) % 60

    new_hour = st_hour + end_hour + (st_min + end_min) // 60

    days = new_hour // 24

    new_hour = new_hour % 24
    if not isam and new_hour >= 12:
        days += 1
        isam = True
    elif isam and new_hour >= 12:
        isam = False

    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12

    if isam:
        new_am_pm = "AM"
    else:
        new_am_pm = "PM"

    days_str = ""
    if days == 1:
        days_str = " (next day)"
    elif days > 1:
        days_str = f" ({days} days later)"

    if day is None:
        new_time = f"{new_hour}:{new_min:02d} {new_am_pm}{days_str}"
    else:
        new_time = f"{new_hour}:{new_min:02d} {new_am_pm}, {return_day_name(day, days)}{days_str}"

    return new_time


def return_day_name(day_str, day_pass):
    day_str = day_str.lower().capitalize()
    days = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }
    for k, v in days.items():
        if v == day_str:
            return days[(k + day_pass) % 7]
