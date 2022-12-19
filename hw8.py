from datetime import datetime, timedelta
import random
from collections import defaultdict



#hear i must try range and change time from calender to time

import random
from collections import defaultdict

users = defaultdict(int)
users = [{'name': 'Vika', 'birthday': '17.10.2000'},
        {"name": "Anna","birthday":"18.12.1985"},
        {"name": "Oleg","birthday":"07.09.1988"},
        {"name": "Sasha","birthday":"08.09.1980"},
        {"name": "Tanya","birthday":"03.11.1990"},
        {"name": "Nastya","birthday":"25.04.1991"},
        {"name": "Vlad","birthday":"30.03.2001"}]
        



work_days = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Next Monday": []}


def main(users):
    current_date = datetime.now().date()
    for user in users:
        birthday = datetime.strptime(user["birthday"],"%d.%m.%Y").date()
        current_birthday = birthday.replace(year=current_date.year)
        if current_date <= current_birthday <= current_date + timedelta(days=7):
            print(current_birthday.weekday())
        elif current_birthday.weekday() == 0:
                work_days['Monday'].append(user["name"])
        elif current_birthday.weekday() == 1:
                work_days['Tuesday'].append(user["name"])
        elif current_birthday.weekday() == 2:
                work_days['Wednesday'].append(user["name"])
        elif current_birthday.weekday() == 3:
                work_days["Thursday"].append(user["name"])
        elif current_birthday.weekday()==4:
                work_days["Friday"].append(user["name"])
        else:
             current_birthday.weekday() in [5,6]
             work_days["Next Monday"].append(user["name"])
    
                # v - це ім'я нашого імениника, ми звертаємось в словник work_days # та записуємо в список імениника
                # тут логіку додавання інші ключі словника
    counter =0
    for key, value in work_days.items():  # після того як наповнили словник імениниками, ітеруємося по ньому
        # та якщо є імениники принтуємо на єкран
        if value:
            print(f'{key}: {", ".join(value)}')
            counter+= 1
        if counter ==0:
             print('Not users with birthday in next 7 days!')   


# це виводиться номер дня тиждня, зробіть перевірку якщо 0 то додавайте в список work_days по ключу Monday
# якщо суботта та неділя - то в список по ключу Next Monday
# потім зробіть вивід в консоль якщо в списку є імениники

if __name__ == '__main__':
        main(users)
