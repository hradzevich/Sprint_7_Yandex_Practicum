import allure
from orders_methods import OrderMethods
from generators import *
from helper import *
from data import OrderMessages


class TestAcceptOrder:
    @allure.title("Успешное принятие заказа курьером")
    @allure.description(
        "Тест проверяет, что курьер может принять заказ. "
        "Проверяется статус-код 200 и корректное тело ответа."
    )
    def test_accept_order_success(self, order, registered_courier):
        with allure.step("Получаем идентификатор заказа по номеру"):
            order_id = OrderMethods.get_order_by_number(order)

        with allure.step("Присваиваем курьеру заказ"):
            courier_id = registered_courier
            accept_order_response = OrderMethods.accept_order(order_id, courier_id)

        with allure.step("Проверяем код ответа"):
            assert (
                accept_order_response.status_code == 200
            ), f"Ожидали статус-код 200, получили {accept_order_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                accept_order_response.json()
                == OrderMessages.ORDER_ACCEPTED_SUCCESS_MESSAGE
            ), f"Ожидали тело ответа: {OrderMessages.ORDER_ACCEPTED_SUCCESS_MESSAGE}, получили: {accept_order_response.json()}"
