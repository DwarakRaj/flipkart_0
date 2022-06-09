from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

print("OMM NAMAH SHIVAY")

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 20)
driver.get('https://flipkart.com')
sleep(3)
driver.maximize_window()

print(" site title : " + driver.title)
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="_2KpZ6l _2doB4z"]'))).click()

search_bar = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
search_bar.clear()
search_bar.send_keys("iphone")
search_bar.send_keys(Keys.RETURN)
print(" listing page ::")
a_link = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='_4rR01T'])[1]")))
print(a_link.text)
print(" link printed ----------- ")
a_link.click()
print(" main page : ")
sleep(0.4)

driver.switch_to.window(driver.window_handles[-1])
sleep(1)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button._3v1-ww"))).click()
sleep(5)
print('clicked add to cart')

# target = driver.find_element_by_xpath("(//div[@class = '_2WkVRV'])[39]")
# loc = target.location_once_scrolled_into_view
# print('-------------- action performed----------')

target = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input._253qQJ")))
print(target.get_attribute('value'))
print('printed--------')






# driver.switch_to.window(driver.window_handles[0])
# box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
# box.send_keys(Keys.CONTROL ,'a')
# box.send_keys(Keys.DELETE)
# sleep(5)
# box.send_keys


# print(driver.title)
# print(driver.current_url)
# dr = driver.current_window_handle
# print(dr)
# close_btn = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']")
# close_btn.click()
# print('-------------- clicked ----------')
# driver.find_element_by_xpath("//input[@type='text']").send_keys("iPhone")
# print('-------------- iphone ENtered ----------')
# print(driver.title)
# print(driver.current_url)
# print('pribted-------------------------************************')
# driver.find_element_by_xpath("//button[@type='submit']").click()
# sleep(3)
# driver.find_element_by_xpath("//div[.='APPLE iPhone 12 (Black, 64 GB)']").click()
# sleep(8)
# print('waiting period over')
# print(driver.title)
# print(driver.title)
# print(driver.current_url)
# print('printed ------------driver title----------------------')
# # text = driver.find_element_by_xpath("//div[@class='aMaAEs']/div/h1/span[@class='B_NuCI']").text
# text = driver.find_element_by_xpath("//div[.='APPLE iPhone 12 (Black, 64 GB)']").text
# print(text)
# sleep(2)
# els = driver.find_elements_by_xpath("//button")
# print(len(els))
# var = els[0].text
# print(var)
# # driver.find_element_by_xpath("(//button)[2]").click()
# sleep(5)
# print('name printed----------------')


# driver.find_element_by_xpath("(//span[@class='_2I9KP_'])[4]").click()
# sleep(3)
# driver.find_element_by_link_text('Sarees').click()
# sleep(5)
# target = driver.find_element_by_xpath("(//div[@class = '_2WkVRV'])[39]")
#
# loc = target.location_once_scrolled_into_view
# print('-------------- action performed----------')
# sleep(2)
#
# driver.get('https://gmail.com')
# sleep(2)
# driver.find_element_by_xpath("//input[@type='email']").send_keys("usawhjr@gmail.com")
# sleep(2)
# driver.find_element_by_xpath("//button[.='Next']").click()
# sleep(2)
# print('before password')
# # driver.find_element_by_xpath("//input[@type='password']").send_keys("Mumbai@12345")
# # sleep(5)
# # driver.find_element_by_xpath("//span[.='Next']").click()
#
# driver.execute_script("window.open('about:blank','secondtab');")
# driver.switch_to.window("secondtab")
# driver.get('https://gmail.com')
#
# driver.execute_script("window.open('about:blank','thirdtab');")
# driver.switch_to.window("thirdtab")
# driver.get('https://bluestone.com')
#
# driver.execute_script("window.open('about:blank','fourthtab');")
# driver.switch_to.window("fourthtab")
# driver.get('https://amazon.com')
