import pytest
import allure
from courier_methods import CourierMethods
from data import CourierMessages
from helper import *


@allure.parent_suite("API тесты Яндекс.Самокат")
@allure.suite("Courier")
@allure.sub_suite("Логин курьера в системе")
class TestLoginCourier:
    @allure.title("Успешный логин существующего курьера")
    @allure.description(
        "Тест проверяет, что после создания курьера можно успешно выполнить логин "
        "с передачей всех обязательных полей (login, password). Ожидается код 200 и наличие поля 'id' в ответе."
    )
    def test_login_existing_courier_success(self, registered_courier):
        with allure.step("Логин нового курьера"):
            credentials = {
                "login": registered_courier["login"],
                "password": registered_courier["password"],
            }
            login_response = CourierMethods.login_courier(credentials)

        with allure.step("Проверяем код ответа"):
            assert (
                login_response.status_code == 200
            ), f"Ожидали статус-код 200, получили {login_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                "id" in login_response.json()
            ), f"Ожидали наличие ключа 'id' в ответе, получили {login_response.json()}"
            assert login_response.json()[
                "id"
            ], f"Ожидали, что 'id' не пустой, получили {login_response.json()['id']}"

    @allure.title("Ошибка при логине курьера с неверным логином или паролем")
    @allure.description(
        "Тест проверяет, что при попытке логина с неверным login или password "
        "API возвращает код 404 и корректное сообщение об ошибке."
    )
    @pytest.mark.parametrize("key", ["login", "password"])
    def test_login_courier_with_wrong_login_or_password_error(
        self, key, registered_courier
    ):
        with allure.step(f"Логин курьера c неправильным {key}"):
            credentials = {
                "login": registered_courier["login"],
                "password": registered_courier["password"],
            }
            invalid_credentials = modify_courier_data(credentials, key)
            login_response = CourierMethods.login_courier(invalid_credentials)

        with allure.step("Проверяем код ответа"):
            assert (
                login_response.status_code == 404
            ), f"Ожидали статус-код 404, получили {login_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                login_response.json()["message"]
                == CourierMessages.WRONG_CREDENTIALS_ERROR_MESSAGE
            ), f"Ожидали в теле ответа: {CourierMessages.WRONG_CREDENTIALS_ERROR_MESSAGE}, получили: {login_response.json()['message']}"

    @allure.title("Ошибка при логине курьера без логина или пароля")
    @allure.description(
        "Тест проверяет, что при попытке логина без login или password "
        "API возвращает код 404 и корректное сообщение об ошибке."
    )
    @pytest.mark.parametrize("key", ["login", "password"])
    def test_login_courier_with_no_login_or_password_error(
        self, key, registered_courier
    ):
        with allure.step(f"Логин курьера без {key}"):
            credentials = {
                "login": registered_courier["login"],
                "password": registered_courier["password"],
            }
            empty_credentials = prepare_data_without_field(credentials, key)
            login_response = CourierMethods.login_courier(empty_credentials)

        with allure.step("Проверяем код ответа"):
            assert (
                login_response.status_code == 400
            ), f"Ожидали статус-код 400, получили {login_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                login_response.json()["message"]
                == CourierMessages.EMPTY_CREDENTIALS_ERROR_MESSAGE
            ), f"Ожидали в теле ответа: {CourierMessages.EMPTY_CREDENTIALS_ERROR_MESSAGE}, получили: {login_response.json()['message']}"
