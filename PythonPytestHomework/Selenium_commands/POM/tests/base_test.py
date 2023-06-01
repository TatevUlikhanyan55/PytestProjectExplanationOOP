import pytest

@pytest.mark.usefixtures("get_driver")
class BaseTest:

    def navigate_to_home_page_widget_part(self):
        self.home_page.click_on_widget_part_btn()

    def check_ddl_functionality_on_select_menu_page(self, text="Green"):
        self.select_menu_page.click_on_select_btn()
        self.select_menu_page.select_item_from_ddl_via_index()
        self.select_menu_page.select_item_from_ddl_via_value()
        self.select_menu_page.select_item_from_ddl_via_text(text=text)


