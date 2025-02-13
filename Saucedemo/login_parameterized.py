import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("locked_out_user","secret_sauce"),\
                                              ("problem_user","secret_sauce"),("performance_glitch_user","secret_sauce")])
def test_login(username,password):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/")
    currenturl=driver.current_url
    print(driver.current_url)
    time.sleep(2)
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    if driver.current_url != currenturl:
        print("Successfully login")
    else:
        print("Login Failed")