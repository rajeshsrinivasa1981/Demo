from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    x = driver.title
    assert x == "ABC"

def test_teardown():
    driver.close()
    driver.quit()
    print("Test completed")


