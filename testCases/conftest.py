import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver_path = ".\\drivers\\chromedriver.exe"

@pytest.fixture()
def setup():
    chrome_service = ChromeService(driver_path)
    driver = webdriver.Chrome(service=chrome_service)
    print("Launching chrome browser...")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

