import pytest
from generators import generate_courier_data
from courier_methods import CourierMethods


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

    CourierMethods.delete_courier(courier_id)
