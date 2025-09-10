import pytest
from data import courier_registration_body
from courier_methods import CourierMethods


# Фикстура для создания нового курьера, которая регистрирует курьера через APIБ логинится с его логином и паролем,
# получает courier_id и возвращает кортеж (login, password, courier_id) для использования в тестах.
# После завершения теста удаляет курьера из системы.
@pytest.fixture
def courier():
    data = courier_registration_body()
    registered_courier_data = CourierMethods.register_new_courier_and_return_login_pass(
        data
    )
    credentials = {
        "login": registered_courier_data["login"],
        "password": registered_courier_data["password"],
    }
    login_response = CourierMethods.login_courier(credentials)
    courier_id = login_response.json().get("id")

    yield credentials["login"], credentials["password"], courier_id

    CourierMethods.delete_courier(courier_id)
