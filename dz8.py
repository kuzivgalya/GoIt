from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    
    current_date = datetime.now()

    monday = current_date + timedelta(7 - current_date.weekday())

    workdays = [monday]
    for i in range(1, 5):
        workdays.append(monday + timedelta(days=i))

    weekends = [monday-timedelta(days=1), monday-timedelta(days=2)]

    mon = ['Monday']
    tue = ['Tuesday']
    wed = ['Wednesday']
    thu = ['Thursday']
    fri = ['Friday']

    for user in users:
        if user["birthday"].month == workdays[0].month and user["birthday"].day == workdays[0].day:
            mon.append(user["name"])
        elif user["birthday"].month == workdays[1].month and user["birthday"].day == workdays[1].day:
            tue.append(user["name"])
        elif user["birthday"].month == workdays[2].month and user["birthday"].day == workdays[2].day:
            wed.append(user["name"])
        elif user["birthday"].month == workdays[3].month and user["birthday"].day == workdays[3].day:
            thu.append(user["name"])
        elif user["birthday"].month == workdays[4].month and user["birthday"].day == workdays[4].day:
            fri.append(user["name"])
        elif user["birthday"].month == weekends[0].month and user["birthday"].day == weekends[0].day:
            mon.append(user["name"])
        elif user["birthday"].month == weekends[1].month and user["birthday"].day == weekends[1].day:
            mon.append(user["name"])

    birthdays_list = [mon, tue, wed, thu, fri]

    for day in birthdays_list:
        if len(day) > 1:
            print(day[0], end=': ')
            print(', '.join(day[1:]))


coworkers = [
    {"name": "Mila", "birthday": datetime(2001, 9, 27)},
    {"name": "Emma", "birthday": datetime(1988, 9, 24)},
    {"name": "Mike", "birthday": datetime(2008, 9, 24)},
    {"name": "Boris", "birthday": datetime(1999, 9, 26)},
    {"name": "Ivan", "birthday": datetime(1995, 9, 30)},
    {"name": "Viktor", "birthday": datetime(2000, 9, 28)},
    {"name": "Elza", "birthday": datetime(1998, 9, 26)},
    {"name": "Kate", "birthday": datetime(2003, 9, 28)},
    {"name": "Stephan", "birthday": datetime(2001, 9, 27)},
    {"name": "Solomia", "birthday": datetime(1997, 1, 6)}
]

if __name__ == '__main__':
    get_birthdays_per_week(coworkers)