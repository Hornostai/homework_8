from datetime import datetime, timedelta
import random
from collections import defaultdict



#hear i must try range and change time from calender to time

import random
from collections import defaultdict

users = defaultdict(str)
# рекомендую створити дні народження які будуть на наступних 7 днях для тестування
users["18.12.1985"] = "Anna"
users["17.10.2000"] = "Vika"
users["7.09.1988"] = "Oleg"
users["8.09.1996"] = "Sasha"
users["9.09.1980"] = "Tanya"
users["10.09.1999"] = "Nastya"
users["11.09.1990"] = "Vlad"

# hear i must try range and change time from calender to time


work_days = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Next Monday": []}


def main(users):
    current_date = datetime.now().date()
    for k, v in users.items():
        birthday = datetime.strptime(k, "%d.%m.%Y").date()
        current_birthday = birthday.replace(year=current_date.year)
        if current_date <= current_birthday <= current_date + timedelta(days=7):
            print(current_birthday.weekday())
        elif current_birthday.weekday() == 0:
                work_days['Monday'].append(v)
        elif current_birthday.weekday() == 1:
                work_days['Tuesday'].append(v)
        elif current_birthday.weekday() == 2:
                work_days['Wednesday'].append(v)
        elif current_birthday.weekday() == 3:
                work_days["Thursday"].append(v)
        elif current_birthday.weekday()==4:
                work_days["Friday"].append(v)
        else:
                current_birthday.weekday() in [5,6]
                work_days["Next Monday"].append(v)
        print(work_days)
                # v - це ім'я нашого імениника, ми звертаємось в словник work_days # та записуємо в список імениника
                # тут логіку додавання інші ключі словника

    for key, value in work_days.items():  # після того як наповнили словник імениниками, ітеруємося по ньому
        # та якщо є імениники принтуємо на єкран
        if value:
            print(f'{key}: {", ".join(value)}')


# це виводиться номер дня тиждня, зробіть перевірку якщо 0 то додавайте в список work_days по ключу Monday
# якщо суботта та неділя - то в список по ключу Next Monday
# потім зробіть вивід в консоль якщо в списку є імениники

if __name__ == '__main__':
    main(users)
