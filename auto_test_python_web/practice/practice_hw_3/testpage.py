import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSeacrhLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_SUCCESS = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_ADD_POST = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_FIND_NEW_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    LOCATOR_BUTTON_TRANS_CONTACT = (By.XPATH,"""/html/body/div[1]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME_FIELD_CONTACT = (By.XPATH,"""/html/body/div/main/div/div/form/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD_CONTACT = (By.XPATH,"""/html/body/div/main/div/div/form/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD_CONTACT = (By.XPATH,"""/html/body/div/main/div/div/form/div[3]/label/span/textarea""")
    LOCATOR_BUTTON_CONTACT_SUBMIT = (By.XPATH,"""/html/body/div/main/div/div/form/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send '{word}' to element {TestSeacrhLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSeacrhLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send '{word}' to element {TestSeacrhLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSeacrhLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSeacrhLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        logging.info(f"Start find error text")
        error_field = self.find_element(TestSeacrhLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"We find text '{text}' in error field {TestSeacrhLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def login_success(self):
        logging.info(f"Start find success text")
        success_field = self.find_element(TestSeacrhLocators.LOCATOR_SUCCESS, time=2)
        text = success_field.text
        logging.info(f"We find text '{text}' in login field {TestSeacrhLocators.LOCATOR_SUCCESS[1]}")
        return text

    def click_add_post_button(self):
        logging.info("Click add post button")
        self.find_element(TestSeacrhLocators.LOCATOR_ADD_POST).click()

    def add_title(self, title):
        time.sleep(1)
        logging.info(f"Send '{title}' to element {TestSeacrhLocators.LOCATOR_TITLE_POST[1]}")
        title_field = self.find_element(TestSeacrhLocators.LOCATOR_TITLE_POST)
        title_field.clear()
        title_field.send_keys(title)


    def add_description(self, description):
        logging.info(f"Send '{description}' to element {TestSeacrhLocators.LOCATOR_DESCRIPTION_POST[1]}")
        description_field = self.find_element(TestSeacrhLocators.LOCATOR_DESCRIPTION_POST)
        description_field.clear()
        description_field.send_keys(description)


    def add_content(self, content):
        logging.info(f"Send '{content}' to element {TestSeacrhLocators.LOCATOR_CONTENT_POST[1]}")
        content_field = self.find_element(TestSeacrhLocators.LOCATOR_CONTENT_POST)
        content_field.clear()
        content_field.send_keys(content)


    def click_save_post_button(self):
        logging.info("Click save post button")
        self.find_element(TestSeacrhLocators.LOCATOR_SAVE_POST).click()


    def find_new_post_title(self):
        logging.info("Start find new post")
        time.sleep(1)
        new_post_field = self.find_element(TestSeacrhLocators.LOCATOR_FIND_NEW_POST, time=2)
        text = new_post_field.text
        logging.info(f"We find new post title '{text}' in field {TestSeacrhLocators.LOCATOR_SUCCESS[1]}")
        return text


    def click_contact_button(self):
        logging.info("Transition to page 'contact us'")
        self.find_element(TestSeacrhLocators.LOCATOR_BUTTON_TRANS_CONTACT).click()

    def add_name_block_contact(self, name):
        logging.info("Add your name in contact")
        content_field = self.find_element(TestSeacrhLocators.LOCATOR_YOUR_NAME_FIELD_CONTACT)
        content_field.clear()
        content_field.send_keys(name)

    def add_email_block_contact(self, mail):
        logging.info("Add email in contact")
        content_field = self.find_element(TestSeacrhLocators.LOCATOR_EMAIL_FIELD_CONTACT)
        content_field.clear()
        content_field.send_keys(mail)

    def add_content_block_contact(self, content):
        logging.info("Add content in contact")
        content_field = self.find_element(TestSeacrhLocators.LOCATOR_CONTENT_FIELD_CONTACT)
        content_field.clear()
        content_field.send_keys(content)

    def click_save_contact_us(self):
        logging.info("Transition to page 'contact us'")
        self.find_element(TestSeacrhLocators.LOCATOR_BUTTON_CONTACT_SUBMIT).click()

    def get_allert_text(self):
        return self.driver.switch_to.alert.text




