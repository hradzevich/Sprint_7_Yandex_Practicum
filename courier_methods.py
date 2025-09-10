import requests
import allure
from urls import *
from data import *


class CourierMethods:
    @staticmethod
    @allure.step("Регистрация нового курьера")
    def register_new_courier_and_return_courier_data(payload):
        register_response = requests.post(CREATE_COURIER, data=payload)
        if register_response.status_code == 201:
            return {
                "login": payload["login"],
                "password": payload["password"],
                "first_name": payload["firstName"],
            }

    @staticmethod
    @allure.step("Логин курьера в системе")
    def login_courier(credentials):
        return requests.post(LOGIN_COURIER, data=credentials)

    @staticmethod
    @allure.step("Удаление курьера по ID")
    def delete_courier(courier_id):
        return requests.delete(f"{DELETE_COURIER}/{courier_id}")
