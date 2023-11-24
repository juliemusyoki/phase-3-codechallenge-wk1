
def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02d}{minute:02d}"

#Example tests
print(convert_to_24_hour(8, 30, "am")) 
print(convert_to_24_hour(8, 30, "pm")) 