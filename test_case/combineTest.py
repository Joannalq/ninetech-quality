import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome","firefox"], scope='class')
def driver_init(request):
    if request.params == "chrome":
        driver = webdriver.Chrome()
    if request.params == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    driver.close()

# @pytest.fixture(scope='class')
# def driver_init_2(request):
#     driver = webdriver.Firefox()
#     request.cls.driver = driver
#     yield
#     driver.close()

