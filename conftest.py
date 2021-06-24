import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome('./venv/lib/python3.9/site-packages/selenium/webdriver/chrome/chromedriver')
    yield driver
    driver.close()