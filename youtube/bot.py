from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time



# Configurar o ChromeDriver
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/chromium-browser'

# Inicia o WebDriver usando o webdriver_manager
# Substitua a driver_version pela versão do seu Chrome ou Chromium
#
service = Service(ChromeDriverManager(driver_version="112.0.5615.49").install()) 

class RoboYoutube():
    def __init__(self):
        self.webdriver = webdriver.Chrome(service=service, options=options)

    def busca(self, busca, paginas):
        videos = []
        pagina = 1

        url = "https://www.youtube.com/results?search_query=%s" % busca
        self.webdriver.get(url)

        while pagina <= paginas:
            titulos = self.webdriver.find_elements(By.XPATH, "//a[@id='video-title']")
            for titulo in titulos:
                if titulo.text not in videos:
                    print("Vídeo encontrado: %s" % titulo.text)
                    videos.append(titulo.text)
            self.proxima_pagina(pagina)
            pagina += 1

    def proxima_pagina(self, pagina):
        print("Mudando para a página %s" % (pagina + 1))
        bottom = pagina * 10000
        self.webdriver.execute_script("window.scrollTo(0, %s);" % bottom)
        time.sleep(5)
        pass

if __name__ == "__main__":
    bot = RoboYoutube()
    bot.busca("teste", 2)
    time.sleep(3)

