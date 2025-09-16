import pytest
import allure
from orders_methods import OrderMethods
from generators import *
from helper import *


class TestCreateOrder:
    @allure.title("Успешное создание нового заказа")
    @allure.description(
        "Тест проверяет успешное создание нового заказа с разными цветами самоката. "
        "В параметрах можно указать один цвет, несколько цветов или вовсе не указывать цвет. "
        "Проверяется, что заказ создаётся с кодом ответа 201 и в теле ответа возвращается ключ 'track'."
    )
    @pytest.mark.parametrize(
        "color_option",
        [["BLACK"], ["GREY"], ["BLACK, GREY"], None],
    )
    def test_create_new_order_success(self, color_option, temporary_order):
        with allure.step("Создание нового заказа"):
            create_order_response, _ = OrderMethods.create_new_order(
                temporary_order, color_option
            )

        with allure.step("Проверяем код ответа"):
            assert (
                create_order_response.status_code == 201
            ), f"Ожидали статус-код 201, получили {create_order_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                "track" in create_order_response.json()
            ), f"Ожидали наличие ключа 'track' в ответе, получили {create_order_response.json()}"
            assert create_order_response.json()[
                "track"
            ], f"Ожидали, что 'track' не пустой, получили {create_order_response.json()["track"]}"
