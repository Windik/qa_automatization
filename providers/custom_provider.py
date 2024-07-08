from faker.providers import BaseProvider
from faker import Faker
from random import randint


fake = Faker('ru_RU')


class CustomProvider(BaseProvider):
    __provider__ = "full_name"
    __provider__ = "current_address"
    __provider__ = "age"
    __provider__ = "salary"

    addresses = ["Россия, г. Елец, Сосновая ул., д. 9 кв.219",
                 "Россия, г. Жуковский, Центральная ул., д. 14 кв.187",
                 "Россия, г. Новошахтинск, Белорусская ул., д. 19 кв.25",
                 "Россия, г. Салават, Рабочая ул., д. 6 кв.157",
                 "Россия, г. Ульяновск, Новая ул., д. 21 кв.79",]

    first_names = [fake.first_name() for _ in range(10)]
    second_names = [fake.last_name() for _ in range(10)]

    full_names = [f"{first_name} {second_name}" for first_name, second_name in zip(first_names, second_names)]

    def current_address(self):
        return self.random_element(self.addresses)

    def full_name(self):
        return self.random_element(self.full_names)

    def age(self, min_age, max_age):
        return randint(min_age, max_age)

    def salary(self, min_salary, max_salary):
        return randint(min_salary, max_salary)
