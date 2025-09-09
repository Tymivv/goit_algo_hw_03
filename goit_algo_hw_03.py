from datetime import datetime
import random 


def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return None   # або можна повернути повідомлення "Невірний формат"

def get_days_from_today(date_str):
    d = string_to_date(date_str)
    if d is None:
        return "Неправильний формат дати. Використовуйте YYYY-MM-DD"
    return (datetime.today().date() - d).days

# print(get_days_from_today("13.14.2000"))

def get_numbers_ticket(min, max, quantity):
    cards = []
    if min <0 or max > 1000 :
        return cards
    if quantity > (max - min + 1):
        return cards
    cards = sorted(random.sample(range(min, max + 1), quantity))
    return cards


# print(get_numbers_ticket(1, 49000, 5))
