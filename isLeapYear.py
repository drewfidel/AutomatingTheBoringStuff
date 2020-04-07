'''
A year is a leap year if it is divisible by 4 but not by 100, or it is divisible by 400.
Examples of input/output: * isLeapYear(-1600); → should return false since the parameter is not in the range (1-9999)
* isLeapYear(1600); → should return true since 1600 is a leap year
* isLeapYear(2017); → should return false since 2017 is not a leap year
* isLeapYear(2000); → should return true because 2000 is a leap year

Write another method getDaysInMonth with two parameters month and year.Both of type int.
If parameter month is < 1 or > 12 return -1. If parameter year is < 1 or > 9999 then return -1.
This method needs to return the number of days in the month. Be careful about leap years they have 29 days in month 2 (February).
You should check if the year is a leap year using the method isLeapYear described above.
Examples of input/output: * getDaysInMonth(1, 2020); → should return 31 since January has 31 days.

getDaysInMonth(2, 2020); → should return 29 since February has 29 days in a leap year and 2020 is a leap year.
getDaysInMonth(2, 2018); → should return 28 since February has 28 days if it's not a leap year and 2018 is not a leap year.
getDaysInMonth(-1, 2020); → should return -1 since the parameter month is invalid.
getDaysInMonth(1, -2020); → should return -1 since the parameter year is outside the range of 1 to 9999.

The parameter needs to be greater than or equal to 1 and less than or equal to 9999.
If the parameter is not in that range return false.
Otherwise, if it is in the valid range,

calculate if the year is a leap year and return true if it is, otherwise return false.
'''

def calculateLeapYear(year):
    try:
        assert year in range(1, 9999)
        if year % 4 == 0 or year % 400 == 0:
            return True
        elif year % 100 != 0:
            return False
        else:
            return False

    except AssertionError:
        print('number is not in range')


def getDaysInMonth(month, year):
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    if month < 1 or month > 12 or year < 1 or year > 9999:
        return -1

    if calculateLeapYear(year):
        num = months[month] + 1
        return num

    elif not calculateLeapYear(year):
        num = months[month]
        return num

# run
print(getDaysInMonth(2, 2020))
print(getDaysInMonth(2, 2019))
print(getDaysInMonth(-2, 2020))
print(getDaysInMonth(2, -2020))




