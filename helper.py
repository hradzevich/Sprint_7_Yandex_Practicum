from generators import *
from faker import Faker
import random as r


fake = Faker("ru_RU")


# Функция изменяет данные зарегистрированного курьера и заменяет значение указанного ключа на другое.
# Используется для тестирования сценариев с неправильным логином/паролем
def modify_courier_data(original_data, key):
    data = original_data.copy()
    if key == "login":
        data[key] = fake.name() + str(r.randint(101, 200))
    elif key == "password":
        data[key] = fake.password(
            length=7,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        )
    return data


# Функция изменяет данные зарегистрированного курьера и заменяет значение указанного ключа на пустое.
# Используется для тестирования сценариев с пустым логином/паролем
def set_required_field_of_courier_data_empty(original_data, key):
    data = original_data.copy()
    data[key] = ""
    return data
