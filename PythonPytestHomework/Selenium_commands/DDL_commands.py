import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

drivers = ["chrome", "edge", "firefox"]


def for_ddl(driver, expected_text="Purple"):
    driver.maximize_window()
    driver.get("https://demoqa.com/")
    widget_part_btn = driver.find_element(By.XPATH, '(//*[@xmlns="http://www.w3.org/2000/svg"])[4]')
    driver.execute_script("arguments[0].scrollIntoView();", widget_part_btn)
    widget_part_btn.click()
    time.sleep(10)
    select_btn = driver.find_element(By.XPATH, '(//*[@id="item-8"])[2]')
    driver.execute_script("arguments[0].scrollIntoView();", select_btn)
    select_btn.click()
    select = Select(driver.find_element(By.ID, 'oldSelectMenu'))
    select.select_by_index(4)
    selected_option = select.first_selected_option
    print("Selected option is" + " " + selected_option.text)
    assert selected_option.text == expected_text
    time.sleep(5)
    select.select_by_value("3")
    time.sleep(5)
    select.select_by_visible_text("Green")
    time.sleep(5)


def get_driver_by_name(driver_name):
    if driver_name == "chrome":
        return webdriver.Chrome()
    elif driver_name == "edge":
        return webdriver.ChromiumEdge()
    elif driver_name == "firefox":
        return webdriver.Firefox()
    else:
        print("Driver name is missing")


driver = get_driver_by_name("chrome")
for_ddl(driver)