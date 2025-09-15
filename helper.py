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


# Функция изменяет данные в заказе и заменяет значение ключа 'color' на нужное значение.
# Используется для тестирования сценария создания заказа с разными цветами самоката
def modify_order_data(original_data, value):
    data = original_data.copy()
    data["color"] = value
    return data


# Функция изменяет данные о номере заказа на нужное значение.
# Используется для тестирования негативного сценария получения информации о заказе без номера заказа
# и с несуществующим номером заказа
def set_track_in_order_data_new_value(original_track,value):
    new_track = original_track
    new_track = value
    return new_track
