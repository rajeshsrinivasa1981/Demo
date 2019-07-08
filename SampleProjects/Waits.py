from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
WebDriverWait(driver,20).until(EC._find_element(driver.find_element_by_name("btnk")))
driver.find_element_by_name("btnK").click()
