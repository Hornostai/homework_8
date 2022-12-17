from datetime import datetime, timedelta
import random
from collections import defaultdict


users = defaultdict(str)

users["5.09.1985"] ="Anna"
users["6.09.2000"] ="Vika"
users["7.09.1988"] ="Oleg"
users["8.09.1996"] ="Sasha"
users["9.09.1980"] ="Tanya"
users["10.09.1999"] ="Nastya"
users["11.09.1990"] ="Vlad"

#hear i must try range and change time from calender to time


work_days = {"Monday":[],"Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], "Next Monday": []}

def main(users):
    current_date = datetime.now().date()
    for k,v in users.items():
        birthday=datetime.strptime(k,"%d.%m.%Y").date()
        current_birthday = birthday.replace(year=current_date.year)
        if current_date<= current_birthday<= current_date+timedelta(days=7):
            print(current_birthday.weekday()) 
            if current_birthday.weekday() == 0:
                uppend_users = users.append(current_birthday.weekday(work_days))
                for key in uppend_users:
                    key += ["Monday"]
                    print(key)
                    if current_birthday == [5] or [6]:
                        work_days+=["Next Monday"]
                        if users in work_days:
                            print (users)

#Там де перевірка current_birthday.weekday() == 0 чи іншій цифрі ,
# треба робити операції додавання цих користувачів в списки з днями тижня

# це виводиться номер дня тиждня, зробіть перевірку якщо 0 то додавайте в список work_days по ключу Monday
# якщо суботта та неділя - то в список по ключу Next Monday
# потім зробіть вивід в консоль якщо в списку є імениники

if __name__ == '__main__':
    main(users)
