from selenium.webdriver.common.by import By

from generator.generator import generated_person_text_box, generated_person_web_tables
from locators.elements_page_locators import (TextBoxPageLocators,
                                             CheckboxPageLocators,
                                             RadioButtonPageLocators,
                                             WebTablesPageLocators, ButtonsPageLocators)
from pages.base_page import BasePage
from faker import Faker
from providers import custom_provider
import random


class TextBoxPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person_text_box())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permanent_address


class CheckboxPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.locators = CheckboxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = random.choice(item_list)
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM).text.lower().replace(' ', '').split('.')[
                0]
            data.append(title_item)
        return data

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text.lower())
        return data


class RadioButtonPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.locators = RadioButtonPageLocators()

    def click_on_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON, }

        radio = self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablesPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.locators = WebTablesPageLocators()

    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person_web_tables())

            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)

            self.element_is_visible(self.locators.SUBMIT).click()

            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []

        for item in people_list:
            data.append(item.text.splitlines())

        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.PARENT_ROW)

        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person_web_tables())
        age = person_info.age

        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()

        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.ROWS_NOT_FOUND_MESSAGE).text

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

    def select_rows_amount(self):
        amount_locators = [
                    self.locators.COUNT_OPTION_5,
                    self.locators.COUNT_OPTION_10,
                    self.locators.COUNT_OPTION_20,
                    self.locators.COUNT_OPTION_25,
                    self.locators.COUNT_OPTION_50,
                    self.locators.COUNT_OPTION_100,
                  ]

        amount_values = []
        data = []

        for amount_value_locator in amount_locators:
            amount_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)

            self.go_to_element(amount_row_button)
            amount_row_button.click()
            self.element_is_visible(amount_value_locator).click()

            rows_button_value = self.element_is_visible(amount_value_locator).text.split()[0]

            amount_values.append(int(rows_button_value))
            data.append(self.check_count_rows())

        return amount_values, data


class ButtonsPage(BasePage):

    def __init__(self, driver, url) -> None:
        super().__init__(driver, url)
        self.locators = ButtonsPageLocators()

    def clicks_on_different_buttons(self, type_click) -> str:
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_ME_BUTTON))
            return self.check_clicked_on_button(self.locators.DOUBLE_CLICK_SUCCESS_MESSAGE)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_ME_BUTTON))
            return self.check_clicked_on_button(self.locators.RIGHT_CLICK_SUCCESS_MESSAGE)

        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_button(self.locators.CLICK_SUCCESS_MESSAGE)

        return "Something went wrong"

    def check_clicked_on_button(self, element):
        return self.element_is_present(element).text