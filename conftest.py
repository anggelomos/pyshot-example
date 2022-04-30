import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pyshot import pyshot_driver


@pytest.fixture(scope="module", autouse=True)
@pyshot_driver
def chrome_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
