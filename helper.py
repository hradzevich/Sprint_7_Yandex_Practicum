from generators import *
from faker import Faker
import random as r


fake = Faker("ru_RU")


# Функция изменяет данные на нужное значение.
# Используется для тестирования негативных сценариев.
def get_nonexisting_value(existing_value, offset=999999):

    return existing_value + offset


# Функция в копии словаря original_data заменяет значение указанного ключа на другое.
# Используется для тестирования сценариев с неправильным логином/паролем.
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


# Функция в копии словаря original_data заменяет значение ключа на нужное значение.
# Используется для тестирования сценария создания заказа с разными цветами самоката.
def modify_data(original_data, key, value):
    data = original_data.copy()
    data[key] = value

    return data


# Удаляет из копии словаря original_data поле с именем key.
# Используется для тестирования негативных сценариев.
def prepare_data_without_field(original_data, key):
    data = original_data.copy()
    data.pop(key, None)
    return data
