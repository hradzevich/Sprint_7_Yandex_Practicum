import pytest
from generators import *
from courier_methods import CourierMethods
from orders_methods import OrderMethods


# Фикстура, которая генерирует данные для создания курьера и возращает в тест для создания курьера.
# Затем логинится с его логином и паролем, получает courier_id для удаления курьера и удаляет курьера после теста.
@pytest.fixture
def temporary_courier():
    data = generate_courier_data()

    yield data

    credentials = {
        "login": data["login"],
        "password": data["password"],
    }
    login_response = CourierMethods.login_courier(credentials)
    courier_id = login_response.json().get("id")

    if courier_id:
        CourierMethods.delete_courier(courier_id)


# Фикстура для создания нового курьера, которая регистрирует курьера через API и возвращает его логин и пароль
# для использования в тестах.
@pytest.fixture
def registered_courier(temporary_courier):
    _, courier_data = CourierMethods.register_new_courier_and_return_courier_data(
        temporary_courier
    )
    credentials = {
        "login": courier_data["login"],
        "password": courier_data["password"],
    }

    return credentials


# Фикстура для создания нового курьера, которая регистрирует курьера через API, логинится с его логином и паролем,
# получает courier_id и возвращает для использования в тестах.
@pytest.fixture
def logged_in_courier(registered_courier):
    login_response = CourierMethods.login_courier(registered_courier)
    courier_id = login_response.json().get("id")

    return courier_id


# Фикстура для подготовки данных нового заказа.
# Возвращает словарь с телом заказа и пустым треком.
# После теста, если трек не присвоен. то отменяет заказ, если присвоен - завершает заказ через API.
# 0 — заказ создан, 1 — принят.
@pytest.fixture
def temporary_order():
    data = generate_order_data()
    holder = {"body": data, "track": None}

    yield holder

    track = holder["track"]
    if track is not None:
        response, order_id = OrderMethods.get_order_by_number(track)
        if response.status_code == 200:
            order_info = response.json().get("order", {})
            status = order_info.get("status")
            if status == 0:
                OrderMethods.cancel_order(track)
            elif status == 1 and order_id is not None:
                OrderMethods.complete_order(order_id)


# Фикстура для создания заказа через API.
# Возвращает номер заказа (track) для использования в тестах.
@pytest.fixture
def created_order_track(temporary_order):
    _, track = OrderMethods.create_new_order(temporary_order["body"])
    temporary_order["track"] = track

    return track


# Фикстура для получения ID заказа по номеру track.
# Использует созданный заказ и возвращает его order_id для тестов.
@pytest.fixture
def created_order_id(created_order_track):
    _, order_id = OrderMethods.get_order_by_number(created_order_track)

    return order_id
