import requests
import allure
from urls import *


class CourierMethods:

    @staticmethod
    @allure.step("Логин курьера в системе")
    def login_courier(credentials):
        return requests.post(LOGIN_COURIER, json=credentials)

    @staticmethod
    @allure.step("Удаление курьера по ID")
    def delete_courier(courier_id=None):
        if courier_id is None:
            delete_response = requests.delete(DELETE_COURIER)
        else:
            delete_response = requests.delete(f"{DELETE_COURIER}/{courier_id}")
        return delete_response

    @staticmethod
    @allure.step("Регистрация нового курьера")
    def register_new_courier_and_return_courier_data(data):
        register_response = requests.post(CREATE_COURIER, json=data)
        courier_data = None
        if register_response.status_code == 201:
            courier_data = {
                "login": data["login"],
                "password": data["password"],
                "first_name": data["firstName"],
            }
        return register_response, courier_data
