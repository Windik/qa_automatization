from data.data import Person
from faker import Faker
from providers import custom_provider


faker_ru = Faker('ru_RU')
faker_ru.add_provider(custom_provider.CustomProvider)

def generated_person():
    yield Person(
        full_name=faker_ru.full_name(),
        email=faker_ru.email(),
        current_address=faker_ru.current_address(),
        permanent_address=faker_ru.current_address()
    )