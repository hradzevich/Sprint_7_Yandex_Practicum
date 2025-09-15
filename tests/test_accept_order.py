import pytest
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
    def test_accept_order_success(self, logged_in_courier, created_order_id):

        with allure.step("Присваиваем курьеру заказ"):
            accept_order_response = OrderMethods.accept_order(
                logged_in_courier, created_order_id
            )

        with allure.step("Проверяем код ответа"):
            assert (
                accept_order_response.status_code == 200
            ), f"Ожидали статус-код 200, получили {accept_order_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                accept_order_response.json()
                == OrderMessages.ORDER_ACCEPTED_SUCCESS_MESSAGE
            ), f"Ожидали тело ответа: {OrderMessages.ORDER_ACCEPTED_SUCCESS_MESSAGE}, получили: {accept_order_response.json()}"

    @allure.title("Ошибка при принятии заказа с несуществующим order_id")
    @allure.description(
        "Проверяет, что присвоение курьеру заказа с несуществующим id"
        "возвращает код 404 и ожидаемое сообщение об ошибке."
    )
    def test_accept_order_invalid_order_id_error(
        self, logged_in_courier, created_order_id
    ):
        with allure.step(
            "Подготовка данных: заменяем значение order_id на несуществующее"
        ):
            nonexisting_order_id = get_nonexisting_value(created_order_id)

        with allure.step("Присваиваем курьеру заказ"):
            courier_id = logged_in_courier
            accept_order_response = OrderMethods.accept_order(
                courier_id, nonexisting_order_id
            )

        with allure.step("Проверяем код ответа"):
            assert (
                accept_order_response.status_code == 404
            ), f"Ожидали статус-код 404, получили {accept_order_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                accept_order_response.json()["message"]
                == OrderMessages.ACCEPT_ORDER_WITH_INVALID_ORDER_ID_ERROR_MESSAGE
            ), f"Ожидали тело ответа: {OrderMessages.ACCEPT_ORDER_WITH_INVALID_ORDER_ID_ERROR_MESSAGE}, получили: {accept_order_response.json()["message"]}"

    @allure.title("Ошибка при принятии заказа с несуществующим courier_id")
    @allure.description(
        "Проверяет, что присвоение курьеру заказа с несуществующим id курьера"
        "возвращает код 404 и ожидаемое сообщение об ошибке."
    )
    def test_accept_order_invalid_courier_id_error(
        self, created_order_id, logged_in_courier
    ):

        with allure.step(
            "Подготовка данных: заменяем значение courier_id на несуществующее"
        ):
            nonexisting_courier_id = get_nonexisting_value(logged_in_courier)

        with allure.step("Присваиваем курьеру заказ"):
            accept_order_response = OrderMethods.accept_order(
                nonexisting_courier_id, created_order_id
            )

        with allure.step("Проверяем код ответа"):
            assert (
                accept_order_response.status_code == 404
            ), f"Ожидали статус-код 404, получили {accept_order_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                accept_order_response.json()["message"]
                == OrderMessages.ACCEPT_ORDER_WITH_INVALID_COURIER_ID_ERROR_MESSAGE
            ), f"Ожидали тело ответа: {OrderMessages.ACCEPT_ORDER_WITH_INVALID_COURIER_ID_ERROR_MESSAGE}, получили: {accept_order_response.json()["message"]}"

    @allure.title("Ошибка при принятии заказа без order_id")
    @allure.description(
        "Проверяет, что присвоение курьеру заказа без указания order_id"
        "возвращает код 400 и ожидаемое сообщение об ошибке."
    )
    def test_accept_order_without_order_id_error(
        self, logged_in_courier, order_id=None
    ):
        with allure.step("Присваиваем курьеру заказ"):
            accept_order_response = OrderMethods.accept_order(logged_in_courier)

        with allure.step("Проверяем код ответа"):
            assert (
                accept_order_response.status_code == 400
            ), f"Ожидали статус-код 400, получили {accept_order_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                accept_order_response.json()["message"]
                == OrderMessages.ACCEPT_ORDER_WITHOUT_ID_ERROR_MESSAGE
            ), f"Ожидали тело ответа: {OrderMessages.ACCEPT_ORDER_WITHOUT_ID_ERROR_MESSAGE}, получили: {accept_order_response.json()["message"]}"

    @allure.title("Ошибка при принятии заказа без courier_id")
    @allure.description(
        "Проверяет, что присвоение курьеру заказа без указания courier_id"
        "возвращает код 400 и ожидаемое сообщение об ошибке."
    )
    def test_accept_order_without_courier_id_error(
        self, created_order_id, courier_id=None
    ):

        with allure.step("Присваиваем курьеру заказ"):
            accept_order_response = OrderMethods.accept_order(
                courier_id, created_order_id
            )

        with allure.step("Проверяем код ответа"):
            assert (
                accept_order_response.status_code == 400
            ), f"Ожидали статус-код 400, получили {accept_order_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                accept_order_response.json()["message"]
                == OrderMessages.ACCEPT_ORDER_WITHOUT_ID_ERROR_MESSAGE
            ), f"Ожидали тело ответа: {OrderMessages.ACCEPT_ORDER_WITHOUT_ID_ERROR_MESSAGE}, получили: {accept_order_response.json()["message"]}"
