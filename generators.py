from faker import Faker
import random as r
from data import *
from datetime import datetime, timedelta
from transliterate import translit


fake = Faker("ru_RU")


# Генерирует необходимые для данные создания курьера
def generate_courier_data():
    first_name = fake.first_name()
    login = first_name + str(r.randint(1, 100))
    password = fake.password(
        length=10,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )
    return {
        "login": login,
        "password": password,
        "firstName": first_name,
    }


# Генерирует необходимые для данные создания заказа
def generare_order_data():
    first_name = translit(fake.first_name(), "ru", reversed=True)
    last_name = translit(fake.last_name(), "ru", reversed=True)
    address = translit(fake.address(), "ru", reversed=True)
    metro_station = r.randint(1, 20)
    phone = fake.numerify("+7 ### ### ## ##")
    rent_time = r.randint(1, 7)
    delivery_date = (datetime.now() + timedelta(days=r.randint(1, 7))).strftime(
        "%Y-%m-%d"
    )
    comment = r.choice([fake.sentence(nb_words=6), ""])
    color = ""

    return {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": delivery_date,
        "comment": comment,
        "color": [color],
    }
