from selenium import webdriver 
import time
#abrindo navegador
nav = webdriver.Chrome()

#navegacao
nav.get("https://iesgo.flie.com.br/Login.asp")

#tela cheia
nav.maximize_window()

#selecionar elementos
login = nav.find_element("id", "js-login-btn")



#selecionanado abas
""" aba = nav.window_handles
aba[0]
aba[1]
#mudando de aba
nav.switch_to.window(aba[1]) """

#escrevendo
nome= nav.find_element('id', 'username')
nome.send_keys("04135905188")

senha= nav.find_element('id', 'password')
senha.send_keys('12345678')
#clicar
login.click()

matricula=nav.find_element("xpath", "//div[contains(., 'RA: 48873')]//button")

matricula.click()
time.sleep(60)



#scrol