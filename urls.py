# Здесь собраны API-ручки для автотестов сервиса Яндекс Самокат

BASE_URL = "https://qa-scooter.praktikum-services.ru"

# Courier
# Создание курьера
CREATE_COURIER = f"{BASE_URL}/api/v1/courier"

# Логин курьера в системе
LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login"

# Удаление курьера
DELETE_COURIER = f"{BASE_URL}/api/v1/courier"

# Orders
# Создание заказа
CREATE_ORDER = f"{BASE_URL}/api/v1/orders"

# Принять заказ
ACCEPT_ORDER = f"{BASE_URL}/api/v1/orders/accept"

# Отменить заказ
CANCEL_ORDER = f"{BASE_URL}/api/v1/orders/cancel"

# Получить заказ по его номеру
GET_ORDER_BY_NUMBER = f"{BASE_URL}/api/v1/orders/track"

# Получение списка заказов
GET_LIST_OF_ORDERS = f"{BASE_URL}/api/v1/orders"

# Завершить заказ
COMPLETE_ORDER = f"{BASE_URL}/api/v1/orders/finish"
