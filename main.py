from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/login")

input("Enter to close")
driver.quit()