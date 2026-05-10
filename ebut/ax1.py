from selenium import webdriver
import time

navegador= webdriver.Chrome()

navegador.get("https://the-internet.herokuapp.com/add_remove_elements/?utm_source=chatgpt.com")

navegador.maximize_window()

add = navegador.find_element("xpath", "//div[contains(., 'Add Element')]//button")


add.click()
add.click()
add.click()

time.sleep(10)