import allure
from orders_methods import OrderMethods
from helper import *
from data import OrderMessages



@allure.parent_suite("API тесты Яндекс.Самокат")
@allure.suite("Orders")
@allure.sub_suite("Получить заказ по его номеру")
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
    def test_get_order_info_no_number_error(self):
        with allure.step("Получить заказ без номера track"):
            get_order_info_response, _ = OrderMethods.get_order_by_number(track=None)
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
            nonexisting_track_value = get_nonexisting_value(created_order_track)

        with allure.step("Получить заказ c несуществующим номером"):
            get_order_info_response, _ = OrderMethods.get_order_by_number(
                nonexisting_track_value
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
