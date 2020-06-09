from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.zhihu.com/")
name = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
name.sendKeys("17722699710")
password.sendKeys("sfls2012101")

time.sleep(5)
driver.quit()



