# Counting Sundays

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False
    else:
        return False

def get_days_in_month(mo_label, year):
    if mo_label == 1:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif mo_label in [3, 5, 8, 10]:
        return 30
    else:
        return 31

def get_next_date(day, month, year):
    if day % get_days_in_month(month, year) == 0:
        day = 1
        if month == 11:
            month = 0
            year += 1
        else:
            month += 1
    else:
        day += 1
    return (day, month, year)


# Initialize start_date to 1,1, 1901
# need to figure out 1,1, 1901's day label since we are only given 1,1,1900's day label
start_date = (1, 0, 1900, 0)
day, month, year, day_name = start_date

while day != 1 or month != 0 or year != 1901:
    day, month, year = get_next_date(day, month, year)
    day_name = (day_name + 1) % 7

# Starting counting sundays
num_sundays = 0
while day != 31 or month != 11 or year != 2000:
    if day_name == 6 and day == 1:
        num_sundays += 1
    day, month, year = get_next_date(day, month, year)
    day_name = (day_name + 1) % 7

print day_name
print day, month, year
print num_sundays