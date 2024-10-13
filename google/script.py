from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configurar o ChromeDriver
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/chromium-browser'


pesquisa = input("Digite sua pesquisa:")

# Inicia o WebDriver usando o webdriver_manager
service = Service(ChromeDriverManager(driver_version="112.0.5615.49").install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

time.sleep(3)
campo = driver.find_element(By.XPATH, "//textarea[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

time.sleep(3)
button_element = driver.find_element(By.ID, "hdtb-tls")
button_element.click()

resultados = driver.find_element(By.XPATH, "//*[@id='result-stats']")
print(resultados.text)

