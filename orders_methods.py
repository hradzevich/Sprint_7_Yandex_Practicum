import requests
import allure
import json
from urls import *


class OrderMethods:

    @staticmethod
    @allure.step("Принять заказ")
    def accept_order(courier_id=None, order_id=None):
        params = {}
        if courier_id is not None:
            params["courierId"] = courier_id
        if order_id is None:
            accept_order_response = requests.put(ACCEPT_ORDER, params=params)
        else:
            accept_order_response = requests.put(
                f"{ACCEPT_ORDER}/{order_id}", params=params
            )
        return accept_order_response

    @staticmethod
    @allure.step("Отменить заказ")
    def cancel_order(data):
        cancel_order_response = requests.put(CANCEL_ORDER, json=data)
        return cancel_order_response

    @staticmethod
    @allure.step("Создание нового заказа")
    def create_new_order(data, color=None):
        if color is not None:
            data["color"] = color
        create_order_response = requests.post(CREATE_ORDER, json=data)
        track = None
        if create_order_response.status_code == 201:
            track = create_order_response.json()["track"]
        return create_order_response, track

    @staticmethod
    @allure.step("Завершить заказ")
    def complete_order(order_id):
        complete_order_response = requests.put(f"{COMPLETE_ORDER}/{order_id}")
        return complete_order_response

    @staticmethod
    @allure.step("Получение списка заказов с возможной фильтрацией")
    def get_list_of_orders(courierId=None, nearestStation=None, limit=30, page=0):
        params = {}
        if courierId is not None:
            params["courierId"] = courierId
        if nearestStation is not None:
            params["nearestStation"] = json.dumps(nearestStation)
        params["limit"] = limit
        params["page"] = page

        get_orders_response = requests.get(GET_LIST_OF_ORDERS, params=params)
        return get_orders_response

    @staticmethod
    @allure.step("Получить заказ по его номеру track")
    def get_order_by_number(track=None):
        params = {}
        order_id = None
        if track is not None:
            params["t"] = track
        get_order_response = requests.get(GET_ORDER_BY_NUMBER, params=params)
        if get_order_response.status_code == 200:
            order_id = get_order_response.json()["order"]["id"]
        return get_order_response, order_id
