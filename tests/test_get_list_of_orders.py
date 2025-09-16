import allure
from orders_methods import OrderMethods


@allure.parent_suite("API тесты Яндекс.Самокат")
@allure.suite("Orders")
@allure.sub_suite("Список заказов")
class TestGetListOfOrders:
    @allure.title("Получение списка всех заказов без фильтров")
    @allure.description(
        "Тест проверяет, что API возвращает полный список заказов при вызове без каких-либо параметров. "
        "Ожидается статус-код 200 и тело ответа содержит ключ 'orders', который является списком."
    )
    def test_get_list_of_orders_without_any_params(self):
        with allure.step("Получение списка всех заказов"):
            get_list_of_orders_response = OrderMethods.get_list_of_orders()

        with allure.step("Проверяем код ответа"):
            assert (
                get_list_of_orders_response.status_code == 200
            ), f"Ожидали статус-код 200, получили {get_list_of_orders_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                type(get_list_of_orders_response.json()["orders"]) == list
            ), f"Ожидали в ответе список 'orders',  получили {type(get_list_of_orders_response.json()["orders"])}"
