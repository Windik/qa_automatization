from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckboxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:

    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablesPageLocators:

    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table data
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')

    # Search data
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    PARENT_ROW = './/ancestor::div[@class="rt-tr-group"]'

    # Update person
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    ROWS_NOT_FOUND_MESSAGE = (By.CSS_SELECTOR, 'div[class="rt-noData"]')

    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')
    COUNT_OPTION_5 = (By.CSS_SELECTOR, 'option[value="5"]')
    COUNT_OPTION_10 = (By.CSS_SELECTOR, 'option[value="10"]')
    COUNT_OPTION_20 = (By.CSS_SELECTOR, 'option[value="20"]')
    COUNT_OPTION_25 = (By.CSS_SELECTOR, 'option[value="25"]')
    COUNT_OPTION_50 = (By.CSS_SELECTOR, 'option[value="50"]')
    COUNT_OPTION_100 = (By.CSS_SELECTOR, 'option[value="100"]')


class ButtonsPageLocators:

    # Buttons to click
    DOUBLE_CLICK_ME_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_ME_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button') #

    # Result messages
    DOUBLE_CLICK_SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    CLICK_SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')
