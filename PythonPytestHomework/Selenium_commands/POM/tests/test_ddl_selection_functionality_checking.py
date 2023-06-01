import pytest

from PythonPytestHomework.Selenium_commands.POM.tests.base_test import BaseTest


class TestDDLSelection(BaseTest):

    @pytest.mark.parametrize("text", ["Yellow", "Green", "Black"])
    def test_ddl_functionality_checking(self, text):
        self.navigate_to_home_page_widget_part()
        self.check_ddl_functionality_on_select_menu_page(text=text)
