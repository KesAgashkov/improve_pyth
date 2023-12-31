import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("config.yaml") as f:
    data = yaml.safe_load(f)

browser = data["browser"]

#Первый пример
# service = Service(data["driver_path"])
# options = webdriver.ChromeOptions()


class Site:

    def __init__(self, address):
        if browser == "firefox":
            serv = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=serv,options=options)
        elif browser == "chrome":
            serv = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=serv, options=options)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(address)

        # self.driver = webdriver.Chrome(service=service, options=options)
        # self.driver.maximize_window()
        # self.driver.get(address)
        # time.sleep(data["sleep_time"])

    def find_el(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_el_property(self, mode, path, property):
        element = self.find_el(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver.close()
