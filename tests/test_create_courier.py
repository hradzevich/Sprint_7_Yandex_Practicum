import allure
from courier_methods import CourierMethods
from data import *


class TestCreateCourier:
    @allure.title("Регистрация нового курьера проходит успешно")
    @allure.description(
        "Тест проверяет успешное создание учетной записи курьера через API с передачей всех обязательных полей. "
        "Запрос возвращает статус-код 201 и тело ответа {'ok': True}. "
    )
    def test_create_new_courier_success(self):
        with allure.step("Создание нового курьера"):
            data = courier_registration_body()
            register_response, courier_data = (
                CourierMethods.register_new_courier_and_return_courier_data(data)
            )

        with allure.step("Проверяем код ответа"):
            assert (
                register_response.status_code == 201
            ), f"Ожидали статус-код 201, получили {register_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert register_response.json() == {
                "ok": True
            }, f"Ожидали тело ответа {{'ok': True}}, получили {register_response.json()}"
