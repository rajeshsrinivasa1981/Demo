from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from POM.Pages.homepage import Homepage
from POM.Pages.loginpage import LoginPage

class TestLogin():

    @pytest.fixture(scope="session")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        Login = LoginPage(driver)
        Login.enter_username("Admin")
        Login.enter_password("admin123")
        Login.click_login()

    def test_home(self,test_setup):
        homepage = Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()


