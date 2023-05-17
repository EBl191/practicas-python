def twentyfour_hours(twelve_hours):
    """Returns a string with the time in the format Hours:minutes."""
    list_hour = twelve_hours.split(":")
    if twelve_hours[-2:].lower() == "pm":
        if list_hour[0] != "12":
            list_hour[0] = str(int(list_hour[0]) + 12)
    else:
        if list_hour[0]== "12":
            list_hour[0] = "00"
    converted_hour = ":".join(list_hour)
    return converted_hour[:-2]

print(twentyfour_hours("12:40AM"))
print(twentyfour_hours("04:40pm"))
print(twentyfour_hours("10:00PM"))