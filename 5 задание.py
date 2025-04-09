def convert_to_12_hour_format(hours, minutes):
    if hours < 0 or hours >= 24 or minutes < 0 or minutes >= 60:
        return "Некорректное время"

    if hours == 0:
        period = "AM"
        hours_12 = 12
    elif 1 <= hours < 12:
        period = "AM"
        hours_12 = hours
    elif hours == 12:
        period = "PM"
        hours_12 = 12
    else:
        period = "PM"
        hours_12 = hours % 12

    return f"{hours_12}:{minutes:02d} {period}"

print(convert_to_12_hour_format(14, 30))
print(convert_to_12_hour_format(0, 45))
