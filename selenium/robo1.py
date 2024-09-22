from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import xlrd

# Configurar o ChromeDriver
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/chromium-browser'  # Substitua pelo caminho do seu executável do Chromium, se necessário

print("Iniciando nosso robô...\n")

dominios = []
#lendo excel
workbook = xlrd.open_workbook('dominio.xls')
sheet = workbook.sheet_by_index(0)

for linha in range(0, 10):
    dominios.append(sheet.cell_value(linha, 0))

# Inicia o WebDriver usando o webdriver_manager
service = Service(ChromeDriverManager(driver_version="112.0.5615.49").install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://registro.br/")

for dominio in dominios:
    pesquisa = driver.find_element(By.ID, "is-avail-field")
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)

    resultados = driver.find_elements(By.TAG_NAME, "strong")
    print("Domínio %s %s " % (dominio, resultados[2].text))

driver.close()
