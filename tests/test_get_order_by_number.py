import allure
from orders_methods import OrderMethods
from generators import *
from helper import *
from data import OrderMessages


class TestGetOrderInfoByNumber:
    @allure.title("Успешное получение информации о заказе по номеру")
    @allure.description(
        "Тест проверяет, что заказ можно получить по его трек-номеру. "
        "Проверяется статус-код ответа и что поле 'order' присутствует и является списком."
    )
    def test_get_order_info_by_number_success(self, created_order_track):
        with allure.step("Получить заказ по его номеру"):
            get_order_info_response, _ = OrderMethods.get_order_by_number(
                created_order_track
            )

        with allure.step("Проверяем код ответа"):
            assert (
                get_order_info_response.status_code == 200
            ), f"Ожидали статус-код 200, получили {get_order_info_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                "order" in get_order_info_response.json()
                and type(get_order_info_response.json()["order"]) == dict
            ), f"Ожидали, что 'order' будет словарем, получили {type(get_order_info_response.json()["order"])}"

    @allure.title("Ошибка при попытке получить заказ без номера")
    @allure.description(
        "Тест проверяет, что запрос на получение информации о заказе без указания номера заказа"
        "возвращает ошибку с кодом 400 с соответствующим сообщением."
    )
    def test_get_order_info_no_number_error(self, created_order_track):
        with allure.step("Подготовка данных: удаляем трек из заказа"):
            order_without_track = set_track_in_order_data_new_value(
                created_order_track, ""
            )

        with allure.step("Получить заказ без номера заказа"):
            get_order_info_response, _ = OrderMethods.get_order_by_number(
                order_without_track
            )
        with allure.step("Проверяем код ответа"):
            assert (
                get_order_info_response.status_code == 400
            ), f"Ожидали статус-код 400, получили {get_order_info_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                get_order_info_response.json()["message"]
                == OrderMessages.GET_ORDER_INFO_WITHOUT_TRACK_ERROR_MESSAGE
            ), f"Ожидали тело ответа: {OrderMessages.GET_ORDER_INFO_WITHOUT_TRACK_ERROR_MESSAGE}, получили: {get_order_info_response.json()["message"]}"

    @allure.title("Ошибка при попытке получить заказ с несуществующим номером")
    @allure.description(
        "Тест проверяет, что запрос на получение информации о заказе с несуществующим номером "
        "возвращает ошибку с кодом 404 с соответствующим сообщением."
    )
    def test_get_order_info_nonexisting_number_error(self, created_order_track):
        with allure.step("Подготовка данных: заменяем значение на несуществующее"):
            nonexisting_track_value = created_order_track + 99999
            order_with_nonexisting_track = set_track_in_order_data_new_value(
                created_order_track, nonexisting_track_value
            )

        with allure.step("Получить заказ c несуществующим номером"):
            get_order_info_response, _ = OrderMethods.get_order_by_number(
                order_with_nonexisting_track
            )

        with allure.step("Проверяем код ответа"):
            assert (
                get_order_info_response.status_code == 404
            ), f"Ожидали статус-код 404, получили {get_order_info_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                get_order_info_response.json()["message"]
                == OrderMessages.GET_ORDER_INFO_NONEXISTING_TRACK_ERROR_MESSAGE
            ), f"Ожидали тело ответа: {OrderMessages.GET_ORDER_INFO_NONEXISTING_TRACK_ERROR_MESSAGE}, получили: {get_order_info_response.json()["message"]}"
