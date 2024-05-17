from tkinter import Tk, Button, Entry, Label, ttk, messagebox
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import sys

login = ""
senha = ""
campo_login = None  
campo_senha = None

if hasattr(sys, '_MEIPASS'):
    diretorio_executavel = sys._MEIPASS
else:
    diretorio_executavel = os.path.dirname(os.path.abspath(__file__))
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_imagem = os.path.join(diretorio_executavel, 'voll.png')
imagem_original = Image.open(caminho_imagem)
largura_nova, altura_nova = 200, 150  
imagem_redimensionada = imagem_original.resize((largura_nova, altura_nova))

def executar_automacao():
    
    global campo_login,campo_senha
    login = campo_login.get()
    senha = campo_senha.get()
    diretorio_usuario = os.path.expanduser("~")
    chrome_driver_path = os.path.join(diretorio_usuario, 'Downloads', 'chromedriver_win32')

    driver = webdriver.Chrome()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://maximavoip.voll360.com/")

    campo_login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-1"))
    )
    campo_login.send_keys(login)

    campo_senha = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "input-2"))
    )
    campo_senha.send_keys(senha)

    forcar_conexao = WebDriverWait(driver, 25).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="SwitchCheckSizemd"]'))
    )
    forcar_conexao.click()

    botao = WebDriverWait(driver, 25).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="submit"]'))
    )
    botao.click()

    def loop_tabulacao():
        botao_chat = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[1]/div[4]/div[1]/div/div[1]'))
        )
        botao_chat.click()

        botao_tabulacao = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[3]/button[8]'))
        )
        botao_tabulacao.click()

        digitar_tabulacao = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-cy="tabulation"]'))
        )
        digitar_tabulacao.send_keys('GESTÃO DE CARTEIRA')

        selecionar_tabulacao = WebDriverWait(driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="[GES] Gestão de Carteira"]'))
        )
        selecionar_tabulacao.click()

        botao_ok = WebDriverWait(driver, 25).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-cy="tabular"]'))
        )
        botao_ok.click()

    for _ in range(30):
        loop_tabulacao()
    time.sleep(10)
    driver.quit()

def iniciar_interface():
    global imagem, campo_login, campo_senha,login,senha
    messagebox.showinfo("Aviso", "ATENÇÃO: O SOFTWARE SÓ IRÁ TABULAR CHATS QUE NÃO TIVERAM INTERAÇÃO COMO 'GESTÃO CARTEIRA'. OS CHATS RESTANTES DEVEM SER TABULADOS MANUALMENTE, POR FAVOR, ANTES DE PROSSEGUIR DESLOGUE DO SEU VOLL POIS O SISTEMA LOGARÁ AUTOMATICAMENTE PARA REALIZAR AS TABULAÇÕES")
    imagem_original = Image.open(caminho_imagem)
    largura_nova, altura_nova = 200, 150  
    imagem_redimensionada = imagem_original.resize((largura_nova, altura_nova))
    

    root = Tk()
    root.title("Interface para Automação")
    estilo = ttk.Style()
    estilo.configure("TButton", foreground="white", background="red", font=("Helvetica", 12, "bold"))
    

   
    label_imagem = Label(root)
    label_imagem.grid(row=0, column=0, columnspan=2) 

    
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
    label_imagem.config(image=imagem_tk)  

    
    label_login = Label(root, text="Login do VOLL:", font=("Helvetica", 11, "bold"))
    label_login.grid(row=1, column=0)  
    campo_login = Entry(root)
    campo_login.grid(row=1, column=1)  

   
    label_senha = Label(root, text="Senha do VOLL:", font=("Helvetica", 11, "bold"))
    label_senha.grid(row=2, column=0)  
    campo_senha = Entry(root, show="*")
    campo_senha.grid(row=2, column=1)  

   
    botao_executar = Button(root, text="Clique aqui para tabular os chats", command=executar_automacao, bg="red", fg="white", font=("Helvetica", 14, "bold"))
    botao_executar.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

    root.mainloop()



if __name__ == "__main__":
    iniciar_interface()
    input("Pressione Enter para sair...")
