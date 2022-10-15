from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.wikipedia.com/')
search_field = driver.find_element(By.ID, 'searchInput').send_keys('Selenium')
button_search = driver.find_element(By.CLASS_NAME)