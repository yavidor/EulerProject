day = 1
week = 7
month = 1
year = 1900
count = 0
while year < 2022:
    if week == 8:
        week = 1
    if (month in (4, 6, 9, 11) and day == 31) or (month == 2 and (
            year % 4 == 0 and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0))) and day == 30) or (
            month == 2 and year % 4 == 0 and day == 29) or day == 32:
        month += 1
        day = 1
    if month == 13:
        year += 1
        month = 1
    if year >= 1901 and week == 1 and day == 1:
        count += 1
    print(week, day, month, year)
    day += 1
    week += 1
print(count)


