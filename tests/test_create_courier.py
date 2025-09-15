import pytest
import allure
from courier_methods import CourierMethods
from generators import *
from data import CourierMessages


class TestCreateCourier:
    @allure.title("Успешное создание курьера при передаче всех возможных данных")
    @allure.description(
        "Тест проверяет успешное создание учетной записи курьера через API с передачей всех полей. "
        "Запрос возвращает статус-код 201 и тело ответа {'ok': True}. "
    )
    def test_create_new_courier_with_all_fields_success(
        self, courier_registration_data
    ):
        with allure.step("Создание нового курьера"):
            register_response, _ = (
                CourierMethods.register_new_courier_and_return_courier_data(
                    courier_registration_data
                )
            )

        with allure.step("Проверяем код ответа"):
            assert (
                register_response.status_code == 201
            ), f"Ожидали статус-код 201, получили {register_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                register_response.json() == CourierMessages.COURIER_SUCCESS_MESSAGE
            ), f"Ожидали тело ответа: {CourierMessages.COURIER_SUCCESS_MESSAGE}, получили: {register_response.json()}"

    @allure.title(
        "Успешное создание курьера при передаче только обязательных данных(login, password)"
    )
    @allure.description(
        "Тест проверяет успешное создание учетной записи курьера через API с передачей всех обязательных полей. "
        "Запрос возвращает статус-код 201 и тело ответа {'ok': True}. "
    )
    def test_create_new_courier_with_all_required_fields_success(
        self, courier_registration_data
    ):
        with allure.step("Создание нового курьера без имени"):
            data_without_login = courier_registration_data
            data_without_login["firstName"] = ""
            register_response, _ = (
                CourierMethods.register_new_courier_and_return_courier_data(
                    data_without_login
                )
            )

        with allure.step("Проверяем код ответа"):
            assert (
                register_response.status_code == 201
            ), f"Ожидали статус-код 201, получили {register_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                register_response.json() == CourierMessages.COURIER_SUCCESS_MESSAGE
            ), f"Ожидали тело ответа: {CourierMessages.COURIER_SUCCESS_MESSAGE}, получили: {register_response.json()}"

    @allure.title("Ошибка при создании курьера с уже существующим логином")
    @allure.description(
        "Попытка создать курьера с логином, который уже используется в системе."
        "Запрос возвращает 409 и сообщение об ошибке."
    )
    def test_create_courier_existing_login_error(self, courier_registration_data):
        with allure.step("Создаём курьера с уникальными данными"):
            _, courier_data = (
                CourierMethods.register_new_courier_and_return_courier_data(
                    courier_registration_data
                )
            )
            existing_login = courier_data["login"]
        with allure.step("Пробуем создать второго курьера с тем же логином"):
            data_existing_login = generate_courier_data()
            data_existing_login["login"] = existing_login
            register_response, _ = (
                CourierMethods.register_new_courier_and_return_courier_data(
                    data_existing_login
                )
            )

        with allure.step("Проверяем код ответа"):
            assert (
                register_response.status_code == 409
            ), f"Ожидали статус-код 409, получили {register_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                register_response.json()["message"]
                == CourierMessages.EXISTING_LOGIN_ERROR_MESSAGE
            ), f"Ожидали в теле ответа: {CourierMessages.EXISTING_LOGIN_ERROR_MESSAGE}, получили: {register_response.json()['message']}"

    @allure.title("Проверка создания курьера с отсутствующим обязательным полем")
    @allure.description(
        "Тест проверяет, что при попытке создать курьера без обязательного поля "
        "(login или password) API возвращает код 400 и корректное сообщение об ошибке."
    )
    @pytest.mark.parametrize("key", ["login", "password"])
    def test_create_new_courier_without_reqiured_login_or_password(
        self, key, courier_registration_data
    ):
        with allure.step(f"Создание нового курьера без {key}"):
            data_with_empty_required = courier_registration_data
            data_with_empty_required[key] = ""
            register_response, _ = (
                CourierMethods.register_new_courier_and_return_courier_data(
                    data_with_empty_required
                )
            )
        with allure.step("Проверяем код ответа"):
            assert (
                register_response.status_code == 400
            ), f"Ожидали статус-код 400, получили {register_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                register_response.json()["message"]
                == CourierMessages.NOT_ALL_INFO_FOR_REG_ERROR_MESSAGE
            ), f"Ожидали в теле ответа: {CourierMessages.NOT_ALL_INFO_FOR_REG_ERROR_MESSAGE}, получили: {register_response.json()['message']}"
