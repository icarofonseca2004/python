from selenium import webdriver
import time

navegador= webdriver.Chrome()

navegador.get("https://the-internet.herokuapp.com/add_remove_elements/?utm_source=chatgpt.com")

navegador.maximize_window()

add = navegador.find_element("xpath", "//button[text()= 'Add Element']")



for i in range(3):
    add.click()

botoes = navegador.find_elements('class name', 'added-manually')

botoes[1].click()



print(f'Sobrou {len(navegador.find_elements('class name', 'added-manually'))} botoes')

time.sleep(10)