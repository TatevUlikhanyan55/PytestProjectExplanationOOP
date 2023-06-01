import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Selenium_commands.POM.pages.home_page import HomePage
from Selenium_commands.POM.pages.select_menu_page import SelectMenuPage
from Selenium_commands.TestingData import test_data

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=test_data.browser)


@pytest.fixture
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture
def get_driver(request, get_browser):
    global driver
    if get_browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    elif get_browser == "firefox":
        driver = webdriver.Firefox()
    elif get_browser == "headless":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Driver not supported")
    driver.implicitly_wait(10)
    ## Add in here each page from the POM in order to initialize the driver for each one.
    request.cls.home_page = HomePage(driver)
    request.cls.select_menu_page = SelectMenuPage(driver)
    driver.get(test_data.url)
    yield driver
    driver.quit()
