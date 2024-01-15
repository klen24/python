from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome()

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://login.vk.com/?role=fast&_origin=https%3A%2F%2Fvk.com&ip_h=20c328bd190f9739cf&to=YWxfZmVlZC5waHA-&validate_result=-2&lrt=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU"
driver.get(url)
time.sleep(1)

#driver.find_element(self, by, value)
#tag_name = driver.find_element(By.LINK_TEXT, "I Accept")

#driver.find_elements_by_tag_name("I Accept")
#find_element_ "I Accept")
#email_input = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').text


email_input = driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').text
print(email_input)


driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()
time.sleep(2)


driver.find_element(By.ID, "Sign in").click()
print(email_input)


#email_input = driver.find_element(By.TITLE, 'Sign in').click()
time.sleep(3)

driver.quit()