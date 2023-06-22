from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Lista de números para enviar mensagens
numeros = ["NUMERO AQUI"] # Insira os números aqui

# Mensagem que deseja enviar
mensagem = "Olá! Esta é uma mensagem automática enviada pelo Selenium."

# Inicializa o driver do Selenium
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado e no PATH

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")
input("Faça o login no WhatsApp Web e pressione Enter para continuar...")

# Loop para enviar mensagens para cada número na lista
for numero in numeros:
    try:
        # Pesquisa pelo número de telefone
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.clear()
        search_box.send_keys(numero)
        sleep(2)
        search_box.send_keys(Keys.ENTER)
        sleep(5)

        # Digita a mensagem e envia
        message_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        message_box.click()
        sleep(2)
        message_box.send_keys(mensagem)
        sleep(2)
        message_box.send_keys(Keys.ENTER)
        sleep(2)

        print(f"Mensagem enviada para {numero}")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {str(e)}")

# Fecha o navegador
driver.quit()





