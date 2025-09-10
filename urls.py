# Здесь собраны API-ручки для автотестов сервиса Яндекс Самокат

BASE_URL = "https://qa-scooter.praktikum-services.ru"

# Courier
# Создание курьера
CREATE_COURIER = "{BASE_URL}/api/v1/courier"

# Логин курьера в системе
LOGIN_COURIER = "{BASE_URL}/api/v1/courier/login"

# Удаление курьера
DELETE_COURIER = "{BASE_URL}/api/v1/courier"

# Orders
# Создание заказа
CREATE_ORDER = "{BASE_URL}/api/v1/orders"

# Принять заказ
ACCEPT_ORDER = "{BASE_URL}/api/v1/orders/accept/{order_id}"

# Получить заказ по его номеру
GET_ORDER_BY_NUMBER = "{BASE_URL}/api/v1/orders/track"

# Получение списка заказов
GET_LIST_OF_ORDERS = "{BASE_URL}/api/v1/orders"
