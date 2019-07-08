from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://www.orangehrm.com/")
driver.find_element_by_id("").send_keys("Admin")




driver.close()
driver.quit()