from faker import Faker
import random as r


fake = Faker("ru_RU")


# Генерирует необходимые для данные создания курьера
def generate_courier_data():
    first_name = fake.first_name()
    login = first_name + str(r.randint(1, 100))
    password = fake.password(
        length=10,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )
    return {
        "login": login,
        "password": password,
        "firstName": first_name,
    }
