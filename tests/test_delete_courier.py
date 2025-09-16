from generators import *
from data import CourierMessages
from courier_methods import CourierMethods
import allure
from helper import *


@allure.parent_suite("API тесты Яндекс.Самокат")
@allure.suite("Courier")
@allure.sub_suite("Удаление курьера")
class TestDeleteCourier:
    @allure.title("Успешное удаление курьера")
    @allure.description(
        "Тест проверяет успешное удаление курьера через API. "
        "Проверяется, что возвращается статус-код 200 и тело ответа соответствует ожидаемому сообщению о успешном удалении."
    )
    def test_delete_courier_success(self, logged_in_courier):
        with allure.step("Удаление учетной записи курьера"):
            delete_response = CourierMethods.delete_courier(logged_in_courier)

        with allure.step("Проверяем код ответа"):
            assert (
                delete_response.status_code == 200
            ), f"Ожидали статус-код 200, получили {delete_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                delete_response.json() == CourierMessages.COURIER_SUCCESS_MESSAGE
            ), f"Ожидали тело ответа: {CourierMessages.COURIER_SUCCESS_MESSAGE}, получили: {delete_response.json()}"

    @allure.title("Ошибка при удаления курьера без указания ID")
    @allure.description(
        "Тест проверяет негативный сценарий удаления курьера без передачи ID. "
        "Ожидается, что сервер вернёт статус-код 400 и сообщение об ошибке."
    )
    def test_delete_courier_without_id_error(self):
        with allure.step("Удаление учетной записи курьера без ID"):
            delete_response = CourierMethods.delete_courier(courier_id=None)

        with allure.step("Проверяем код ответа"):
            assert (
                delete_response.status_code == 400
            ), f"Ожидали статус-код 400, получили {delete_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                delete_response.json()["message"]
                == CourierMessages.DELETE_WITHOUT_ID_ERROR_MESSAGE
            ), f"Ожидали тело ответа: {CourierMessages.DELETE_WITHOUT_ID_ERROR_MESSAGE}, получили: {delete_response.json()["message"]}"

    @allure.title("Ошибка при удалении несуществующего курьера")
    @allure.description(
        "Тест проверяет негативный сценарий удаления курьера, которого нет в системе. "
        "ID берётся из фикстуры, затем модифицируется, чтобы гарантировать, что курьер не существует. "
        "Ожидается статус-код 404 и соответствующее сообщение об ошибке."
    )
    def test_delete_nonexisting_courier_error(self, logged_in_courier):
        with allure.step(
            "Подготовка данных: создаем ID курьера,которого нет в системе"
        ):
            nonexisting_id = get_nonexisting_value(logged_in_courier)

        with allure.step("Удаление учетной записи курьера, ID которого нет в системе"):
            delete_response = CourierMethods.delete_courier(nonexisting_id)

        with allure.step("Проверяем код ответа"):
            assert (
                delete_response.status_code == 404
            ), f"Ожидали статус-код 404, получили {delete_response.status_code}"

        with allure.step("Проверяем тело ответа"):
            assert (
                delete_response.json()["message"]
                == CourierMessages.DELETE_NONEXISTING_COURIER_ERROR_MESSAGE
            ), f"Ожидали тело ответа: {CourierMessages.DELETE_NONEXISTING_COURIER_ERROR_MESSAGE}, получили: {delete_response.json()["message"]}"
