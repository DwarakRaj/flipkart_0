from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep

print (" We are entering Chegg.com website as a part of Python automation trial" )

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 20)
driver.get('https://www.chegg.com/')
sleep(3)
driver.maximize_window()
sleep(4)

print(" site title : " + driver.title)
wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='sohp-t1-hw']"))).click()






