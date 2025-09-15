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
    def test_accept_order_success(self, logged_in_courier, created_order_track):
        with allure.step("Получаем идентификатор заказа по номеру"):
            _, order_id = OrderMethods.get_order_by_number(created_order_track)

        with allure.step("Присваиваем курьеру заказ"):
            courier_id = logged_in_courier
            accept_order_response = OrderMethods.accept_order(courier_id, order_id)

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
        self, created_order_track, logged_in_courier
    ):
        with allure.step("Получаем идентификатор заказа по номеру"):
            _, order_id = OrderMethods.get_order_by_number(created_order_track)

        with allure.step(
            "Подготовка данных: заменяем значение order_id на несуществующее"
        ):
            nonexisting_order_id = order_id + 99999
            order_with_nonexisting_id = set_in_data_new_value(
                created_order_track, nonexisting_order_id
            )

        with allure.step("Присваиваем курьеру заказ"):
            courier_id = logged_in_courier
            accept_order_response = OrderMethods.accept_order(
                courier_id, order_with_nonexisting_id
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
        self, created_order_track, logged_in_courier
    ):
        with allure.step("Получаем идентификатор заказа по номеру"):
            _, order_id = OrderMethods.get_order_by_number(created_order_track)

        with allure.step(
            "Подготовка данных: заменяем значение courier_id на несуществующее"
        ):
            nonexisting_courier_id = logged_in_courier + 99999
            courier_with_nonexisting_id = set_in_data_new_value(
                logged_in_courier, nonexisting_courier_id
            )

        with allure.step("Присваиваем курьеру заказ"):
            accept_order_response = OrderMethods.accept_order(
                courier_with_nonexisting_id, order_id
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
        self, created_order_track, courier_id=None
    ):
        with allure.step("Получаем идентификатор заказа по номеру"):
            _, order_id = OrderMethods.get_order_by_number(created_order_track)

        with allure.step("Присваиваем курьеру заказ"):
            accept_order_response = OrderMethods.accept_order(courier_id, order_id)

        with allure.step("Проверяем код ответа"):
            assert (
                accept_order_response.status_code == 400
            ), f"Ожидали статус-код 400, получили {accept_order_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                accept_order_response.json()["message"]
                == OrderMessages.ACCEPT_ORDER_WITHOUT_ID_ERROR_MESSAGE
            ), f"Ожидали тело ответа: {OrderMessages.ACCEPT_ORDER_WITHOUT_ID_ERROR_MESSAGE}, получили: {accept_order_response.json()["message"]}"
