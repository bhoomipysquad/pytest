import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(params=["chrome","firefox","edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver= webdriver.Chrome()

    elif request.param == "firefox":
        driver=webdriver.Firefox()

    elif request.param == "edge":
         driver=webdriver.Edge()


