from generators import *


# Функция генерирует данные для курьера и заменяет значение указанного ключа на пустую строку.
# Используется для тестирования сценариев с отсутствующими полями
def modify_courier_data(key):
    courier_data = generate_courier_data()
    courier_data[key] = ""
    return courier_data
