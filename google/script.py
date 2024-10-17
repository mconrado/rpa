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

button_element = driver.find_element(By.ID, "hdtb-tls")
button_element.click()

resultados = driver.find_element(By.XPATH, "//*[@id='result-stats']").text
print(resultados)
numero_resultados = int(resultados.split("Aproximadamente")[1].split(' resultados')[0].replace('.', ''))
maximo_paginas = numero_resultados/10
pagina_alvo = input("%s páginas encontradas, até qual página quer ir?" % (maximo_paginas))
lista_resultados = []

url_pagina = driver.find_element(By.XPATH, "//a[@aria-label='Page 2']").get_attribute("href")

pagina_atual = 0
start = 10

while pagina_atual <= int(pagina_alvo) -1:
    if pagina_atual > 1:
        url_pagina = url_pagina.replace("start=%s" % start, "start=%s" % (start+10))
        start += 10
        driver.get(url_pagina)
    elif pagina_atual == 1:
        driver.get(url_pagina)
    pagina_atual += 1

    time.sleep(2)

    divs = driver.find_elements(By.XPATH, "//div[@class='yuRUbf']")
    for div in divs:
        nome = div.find_element(By.TAG_NAME, 'span')
        link = div.find_element(By.TAG_NAME, 'a')
        resultado = "%s;%s" % (nome.text, link.get_attribute("href"))
        print(resultado)
        lista_resultados.append(resultado)

with open("resultados.txt", "w") as arquivo:
    for resultado in lista_resultados:
        arquivo.write("%s\n" % resultado)
    arquivo.close()
print("%s resultados encontrados no Google e salvos no arquivo.txt" % len(lista_resultados))
