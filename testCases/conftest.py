import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")

def pytest_addoption(parser): #predefined method for adopting parser
    parser.addoption("--browser")
@pytest.fixture()
def setup(request):
    browser=request.config.getoption("--browser")
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    elif browser=='edge':
        driver=webdriver.Edge()
    else:
        driver=webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

@pytest.fixture(params=
[
    ("Admin","admin123","Login_Pass"),
    ("Admin1","admin123","Login_Fail"),
    ("Admin","admin1234","Login_Fail"),
    ("Admin1","admin1234","Login_Fail")
])

def getDataForLogIn(request):
    return request.param

