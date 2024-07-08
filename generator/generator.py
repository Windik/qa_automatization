from data.data import PersonTextBox, PersonWebTables
from faker import Faker
from providers import custom_provider


faker_ru = Faker('ru_RU')
faker_ru.add_provider(custom_provider.CustomProvider)


def generated_person_text_box():
    yield PersonTextBox(
        full_name=faker_ru.full_name(),
        email=faker_ru.email(),
        current_address=faker_ru.current_address(),
        permanent_address=faker_ru.current_address(),
    )


def generated_person_web_tables():
    yield PersonWebTables(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=faker_ru.age(18, 90),
        salary=faker_ru.salary(5000, 250000),
        department=faker_ru.job(),
    )
