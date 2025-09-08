from datetime import datetime
import random 


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date):
    return (datetime.today().date() - string_to_date(date)).days

# print(get_days_from_today("2021-10-09"))

def get_numbers_ticket(min, max, quantity):
    cards = []
    if min <0 or max > 1000 :
        return "Неприпустимі значення"
    return sorted(random.sample(range(min, max + 1), quantity))


# print(get_numbers_ticket(1, 49, 6))
