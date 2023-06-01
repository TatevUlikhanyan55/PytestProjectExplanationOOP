from hamcrest import equal_to
from PythonPytestHomework.Selenium_commands.POM.lib.assertions import assert_that
from selenium.webdriver.common.by import By
from PythonPytestHomework.Selenium_commands.POM.lib.helpers import Helpers


class SelectMenuPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    select_btn = (By.XPATH, '(//*[@id="item-8"])[2]')
    select_menu = (By.ID, 'oldSelectMenu')

    def click_on_select_btn(self):
        self.find_and_click(self.select_btn)

    def select_item_from_ddl_via_index(self, index=1):
        self.select_item(self.select_menu, by_index=True, text=index)

    def select_item_from_ddl_via_value(self, value="3"):
        self.select_item(self.select_menu, by_value=True, value=value)

    def select_item_from_ddl_via_text(self, text="Green"):
        selected_item = self.select_item(self.select_menu, by_text=True, text=text)
        assert_that(selected_item, equal_to(text))
