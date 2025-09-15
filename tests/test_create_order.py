import pytest
import allure
from orders_methods import OrderMethods
from generators import *
from helper import *


class TestCreateOrder:
    @allure.title("Успешное создание нового заказа")
    @allure.description(
        "Тест проверяет успешное создание нового заказа с разными цветами самоката. "
        "В параметрах передаются: один цвет, несколько цветов или пустой список. "
        "Проверяется, что заказ создаётся с кодом ответа 201 и возвращается ключ 'track'."
    )
    @pytest.mark.parametrize(
        "color_option",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK, GREY"],
            [],
        ],
    )
    def test_create_new_order_success(self, color_option, temporary_order):
        with allure.step("Создание нового заказа"):
            order_body_with_scooter_color = modify_order_data(
                temporary_order, color_option
            )
            create_order_response, track = OrderMethods.create_new_order(
                order_body_with_scooter_color
            )
            temporary_order["track"] = track

        with allure.step("Проверяем код ответа"):
            assert (
                create_order_response.status_code == 201
            ), f"Ожидали статус-код 201, получили {create_order_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                "track" in create_order_response.json() and track != ""
            ), f"Ожидали наличие ключа 'track' с непустым значением в ответе, получили {create_order_response.json()}"
