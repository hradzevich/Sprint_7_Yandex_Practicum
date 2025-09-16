from faker import Faker
import random as r
import string
from datetime import datetime, timedelta
from transliterate import translit


fake = Faker("ru_RU")


# Генерирует необходимые для данные создания курьера
def generate_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(r.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "firstName": first_name,
    }


# Генерирует необходимые для данные создания заказа без цвета
def generate_order_data():
    first_name = translit(fake.first_name(), "ru", reversed=True)
    last_name = translit(fake.last_name(), "ru", reversed=True)
    address = translit(fake.address(), "ru", reversed=True)
    metro_station = r.randint(1, 237)
    phone = fake.numerify("+7 ### ### ## ##")
    rent_time = r.randint(1, 7)
    delivery_date = (datetime.now() + timedelta(days=r.randint(1, 7))).strftime(
        "%Y-%m-%d"
    )
    comment = r.choice([fake.sentence(nb_words=6), ""])

    return {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": delivery_date,
        "comment": comment,
    }
