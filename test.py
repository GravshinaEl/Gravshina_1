from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Тест_1. Открытие браузера, поиск по элементу, навигация, закрытие браузера
browser = webdriver.Firefox() # Открытие браузера
URL = 'http://uitestingplayground.com/'
browser.get(URL) # Открытие сайта

wait = WebDriverWait(browser, 5) #явное ожидание до 5 секунд, как увидит условие
link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Dynamic ID'))) #ожидание и поиск по ссылке
link.click()

"""sleep(2)
link = browser.find_element(By.LINK_TEXT) #поиск по тексту ссылки на UI
link = browser.find_element(By.XPATH, '//a[@href="/dynamicid"]') #поиск по XPATH
link.click()"""

button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
button.click()
print('Успешно')

browser.back()
browser.quit()
print('Тест завершен')
