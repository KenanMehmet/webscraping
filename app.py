from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
path=r"C:\Users\Kenan\programming\Selenium\geckodriver.exe"
driver=webdriver.Firefox()
driver.get("https://www.universal-credit.service.gov.uk/sign-in")
sleep(3)
username = driver.find_element(By.XPATH, r'//*[@id="id-userName"]')
username.send_keys("KenanMehmet")
password = driver.find_element(By.XPATH, r'//*[@id="id-password"]')
password.send_keys("9HBzMiazfijuXr5")
submit = driver.find_element(By.XPATH, r'//*[@id="id-submit-button"]')
submit.click()
sleep(5)
driver.quit()