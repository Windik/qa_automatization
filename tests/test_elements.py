import time
from pages.elements_page import TextBoxPage, CheckboxPage, RadioButtonPage, WebTablesPage
from conftest import driver


def missmatch_message(field_name):
    return f"Field {field_name} does not match"


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            field_names = [
                "full_name",
                "email",
                "current_address",
                "permanent_address",
            ]

            input_data = {key: value for key, value in zip(field_names, text_box_page.fill_all_fields())}
            output_data = {key: value for key, value in zip(field_names, text_box_page.check_filled_form())}

            assert input_data["full_name"] == output_data["full_name"], missmatch_message(field_names[0])
            assert input_data["email"] == output_data["email"], missmatch_message(field_names[1])
            assert input_data["current_address"] == output_data["current_address"], missmatch_message(field_names[2])
            assert input_data["permanent_address"] == output_data["permanent_address"], missmatch_message(field_names[3])

    class TestCheckbox:
        def test_checkbox(self, driver):
            checkbox_page = CheckboxPage(driver, 'https://demoqa.com/checkbox')
            checkbox_page.open()
            checkbox_page.open_full_list()
            checkbox_page.click_random_checkbox()

            input_checkbox = checkbox_page.get_checked_checkboxes()
            output_result = checkbox_page.get_output_result()

            assert input_checkbox == output_result, "Checkboxes have not been selected correctly!"

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()

            radio_button_page.click_on_radio_button('yes')
            output_yes = radio_button_page.get_output_result()

            radio_button_page.click_on_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()

            radio_button_page.click_on_radio_button('no')
            output_no = radio_button_page.get_output_result()

            assert output_yes == 'Yes', "'Yes' has been selected, but output got another value!"
            assert output_impressive == 'Impressive', "'Impressive' has been selected, but output got another value!"
            assert output_no == 'No', "'No' has been selected, but output got another value!"

    class TestWebTables:

        def test_web_table_add_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()

            new_person = web_tables_page.add_new_person(1)

            table_result = web_tables_page.check_new_added_person()

            assert new_person in table_result, ("There is no new person in table, "
                                                "or data of generated and added person are different!")
