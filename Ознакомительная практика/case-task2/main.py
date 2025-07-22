import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

def getUserInput():
    day = input("Введите день рождения: ")
    month = input("Введите месяц рождения: ")
    year = input("Введите год рождения: ")
    return {
        "day": day,
        "month": month,
        "year": year
    }

def convertInputToDateData(dict):
    date = datetime.date(int(dict["year"]), int(dict["month"]), int(dict["day"]))
    return {
        "formattedDate":formatDate(date),
        "weekday": getDayName(date.weekday()),
        "isLeapYear": isYearLeap(date.year),
        "age": getAge(date)
    }

def drawBirthDate(dateTime):
    digits = {
    '-': [
        "     ",
        "     ",
        " *** ",
        "     ",
        "     "
    ],
    '0': [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        "*****"
    ],
    '2': [
        " *** ",
        "*   *",
        "   * ",
        "  *  ",
        "*****"
    ],
    '3': [
        " *** ",
        "*   *",
        "   **",
        "*   *",
        " *** "
    ],
    '4': [
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *"
    ],
    '5': [
        "*****",
        "*    ",
        "**** ",
        "    *",
        "**** "
    ],
    '6': [
        " *** ",
        "*    ",
        "**** ",
        "*   *",
        " *** "
    ],
    '7': [
        "*****",
        "    *",
        "   * ",
        "  *  ",
        "  *  "
    ],
    '8': [
        " *** ",
        "*   *",
        " *** ",
        "*   *",
        " *** "
    ],
    '9': [
        " ****",
        "*   *",
        " ****",
        "    *",
      	" *** "
    ]
}
    date_str = dateTime
    output_lines = [""] * 5

    for digit_char in date_str:
        digit_pattern = digits[digit_char]
        for i in range(5):
            output_lines[i] += digit_pattern[i] + "  "

    for line in output_lines:
        print(line)

def getAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def getDayName(dayNumber):
    return calendar.day_name[dayNumber]

def isYearLeap(year):
    return calendar.isleap(year)

def formatDate(date):
    return date.strftime('%d-%m-%Y')

inputData = getUserInput()
dateData = convertInputToDateData(inputData)

drawBirthDate(dateData["formattedDate"])