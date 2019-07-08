from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("file:///C:/Users/RS042424/OneDrive%20-%20Cerner%20Corporation/Desktop/webtable.html")
rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))
print(rows)
print(cols)

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value= driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end="  ")
    print()



