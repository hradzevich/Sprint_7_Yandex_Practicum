import allure
from helper import *


@allure.step("Получаем body для регистрации нового курьера")
def courier_registration_body():
    first_name, login, password = generate_courier_data()
    payload = {"login": login, "password": password, "firstName": first_name}
    return payload
