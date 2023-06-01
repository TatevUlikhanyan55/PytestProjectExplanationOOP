from selenium.webdriver.common.by import By
from PythonPytestHomework.Selenium_commands.POM.lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    widget_part_btn = (By.XPATH, '(//*[@xmlns="http://www.w3.org/2000/svg"])[4]')

    def click_on_widget_part_btn(self):
        self.find_and_click(self.widget_part_btn)


