import pytest
from generators import *
from courier_methods import CourierMethods
from orders_methods import OrderMethods


# Фикстура для генерации данных нового курьера для теста, которые возращает в тест для создания курьера.
# Затем логинится с его логином и паролем, получает courier_id для удаления курьера и удаляет.
@pytest.fixture
def courier_registration_body():
    data = generate_courier_data()

    yield data

    credentials = {
        "login": data["login"],
        "password": data["password"],
    }
    login_response = CourierMethods.login_courier(credentials)
    courier_id = login_response.json().get("id")

    if courier_id is not None:
        CourierMethods.delete_courier(courier_id)


# Фикстура для создания нового курьера, которая регистрирует курьера через API, логинится с его логином и паролем,
# получает courier_id и возвращает для использования в тестах.
@pytest.fixture
def courier():
    data = generate_courier_data()
    _, courier_data = CourierMethods.register_new_courier_and_return_courier_data(data)
    credentials = {
        "login": courier_data["login"],
        "password": courier_data["password"],
    }
    login_response = CourierMethods.login_courier(credentials)
    courier_id = login_response.json().get("id")

    return courier_id


# Фикстура для создания нового заказа, которая готовит данные для заказа и возвращает для использования в тестах.
# Затем получает номер заказа 'track' и отменяет заказ.
@pytest.fixture
def order_body():
    data = generare_order_data()
    holder = {"body": data, "track": None}

    yield holder

    if holder["track"] is not None:
        OrderMethods.cancel_order(str(holder["track"]))


# Фикстура для создания нового заказа, которая готовит данные для заказа, создает новый заказ и возвращает
# номер заказа 'track' для использования в тестах.
@pytest.fixture
def order():
    data = generare_order_data()
    _, track = OrderMethods.create_new_order(data)

    return track
