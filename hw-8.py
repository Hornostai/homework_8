from datetime import datetime, timedelta
import random
from collections import defaultdict

USERS = defaultdict(str)

USERS[26.08] :"Sacha",
    30.02 :"Olia",
    05.09 :"Peter",
    10.11 :"Ivan",
    23.10 :"Vlad",

NAME=[]
BIRTHDAY=[]

USERS={
    26.08 :"Sacha",
    30.02 :"Olia",
    05.09 :"Peter",
    10.11 :"Ivan",
    23.10 :"Vlad",
}

total =0
for i in BIRTHDAY:
    total

def get_birthdays_per_week(n):
    current_date = datetime.now()
    oldest_date = current_date-timedelta(days=365*80)#порівнює дату +-.
    birthdays_list = []
    for i in range(5):
        fake_year = random.randrange(oldest_date.year, current_date.year)
        fake_month = random.randint(1,12)
        fake_day = random.randint(1,31)
        try:
            fake_birthday = datetime(year=fake_year,month=fake_month, day=fake_day)
        except ValueError:
            continue
        if current_date>=fake_birthday:
            birthdays_list.append(fake_birthday.date())
    return birthdays_list

print(USERS)
#def main():
    
if __name__ == '__main__':
    print(get_birthdays_per_week(USERS))
