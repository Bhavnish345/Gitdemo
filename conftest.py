import pytest
import time

from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browsername=request.config.getoption("browser_name")
    if browsername =="Chrome":
      driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browsername =="Firefox":
      driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    driver.implicitly_wait(10)
    # Wait until 5 seconds if Object is not displayed
    # Global Wait
    # 1.5 seconds to reach next page execution will resume in 1.5 seconds
    # if object do not show up at all , then max time your test waits for 5 seconds
    driver.maximize_window()
    #driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver=driver
    #yield
    #driver.close()




