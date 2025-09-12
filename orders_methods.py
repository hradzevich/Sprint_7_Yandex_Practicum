import requests
import allure
from urls import *


class OrderMethods:
    @staticmethod
    @allure.step("Создание нового заказа")
    def create_new_order(data):
        create_order_response = requests.post(CREATE_ORDER, json=data)
        # track = None
        # if create_order_response.status_code == 201:
        #     track = create_order_response.json()["track"]
        return create_order_response
