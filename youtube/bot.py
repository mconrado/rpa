from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
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

    def busca(self, busca):
        url = "https://www.youtube.com/results?search_query=%s" % busca
        self.webdriver.get(url)

if __name__ == "__main__":
    bot = RoboYoutube()
    bot.busca("teste")
    time.sleep(3)

