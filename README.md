# Автоматизированное тестирование API сервиса «Яндекс Самокат»

Проект содержит автоматизированные тесты для учебного API **Яндекс Самокат**  
(документация: [qa-scooter.praktikum-services.ru/docs](https://qa-scooter.praktikum-services.ru/docs/)).


## Описание проекта
Задача — протестировать основные ручки API: убедиться, что они корректно работают и обрабатывают ошибки.  
Перед написанием автотестов API было исследовано вручную в Postman.

Тесты написаны на **Python + Pytest** с использованием **Allure** для формирования отчётов.

## Проверяемые сценарии
### 1. Создание курьера

Успешное создание курьера при передаче всех возможных данных ***`test_create_new_courier_with_all_fields_success`***

Успешное создание курьера при передаче только обязательных данных(login, password) ***`test_create_new_courier_with_all_required_fields_success`***

Ошибка при создании курьера с уже существующим логином ***`test_create_courier_existing_login_error`***

Ошибка при создании курьера с отсутствующим обязательным полем ***`test_create_new_courier_without_reqiured_login_or_password`***


### 2. Логин курьера

Успешный логин существующего курьера ***`test_login_existing_courier_success`***

Ошибка при логине курьера с неверным логином или паролем ***`test_login_courier_with_wrong_login_or_password_error`***

Ошибка при логине курьера без логина или пароля ***`test_login_courier_with_no_login_or_password_error`***


### 3. Создание заказа

Успешное создание нового заказа ***`test_create_new_order_success`***

### 4.  Список заказов

Получение списка всех заказов без фильтров ***`test_get_list_of_orders_without_any_params`***


### 5. Удалить курьера:

Успешное удаление курьера ***`test_delete_courier_success`***

Ошибка при удаления курьера без указания ID ***`test_delete_courier_without_id_error`***

Ошибка при удалении несуществующего курьера ***`test_delete_nonexisting_courier_error`***

### 6. Принять заказ:

Успешное принятие заказа курьером  ***`test_accept_order_success`***

Ошибка при принятии заказа с несуществующим order_id ***`test_accept_order_invalid_order_id_error`***

Ошибка при принятии заказа с несуществующим courier_id ***`test_accept_order_invalid_courier_id_error`***

Ошибка при принятии заказа без order_id ***`test_accept_order_without_order_id_error`***

Ошибка при принятии заказа без courier_id ***`test_accept_order_without_courier_id_error`***

Ошибка при попытке принять заказ повторно ***`test_accept_already_accepted_order_error`***

### 7. Получить заказ по номеру:

Успешное получение информации о заказе по номеру ***`test_get_order_info_by_number_success`***

Ошибка при попытке получить заказ без номера ***`test_get_order_info_no_number_error`***

Ошибка при попытке получить заказ с несуществующим номером ***`test_get_order_info_nonexisting_number_error`***

## Технологии

+ Python 3.13.5

+ Pytest

+ Faker (для генерации тестовых данных)

+ Random (для генерации тестовых данных)

+ Allure (отчёты о тестировании)


## Запуск тестов

1. Клонировать репозиторий:<br/>
    ```git clone https://github.com/hradzevich/Sprint_7.git  ```

2. Установить зависимости:<br/>
    ```pip install -r requirements.txt```

3. Запустить тесты с сохранением результатов для Allure:<br/>
    ```pytest --alluredir=allure-results```

4. Сгенерировать html-отчёт в папку allure_report:<br/>
    ```allure generate allure-results -o allure_report --clean```

5. Открыть готовый отчёт в браузере:<br/>
    ```allure open allure_report```


## Полезные команды 

Очистить результаты прошлых запусков:<br/>
    ```rm -rf allure-results allure_report```

Перегенерировать отчёт без запуска тестов (если тесты уже запускались и в папке allure_results есть данные):<br/>
    ```allure generate allure-results -o allure_report --clean```
    ```allure open allure_report```

Быстрый просмотр отчёта без сохранения (отчёт откроется во временном режиме, готовая папка не создаётся):<br/>
    ```allure serve allure-results```