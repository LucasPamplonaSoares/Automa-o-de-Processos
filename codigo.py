# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui 
import time

# clicar -> pyautogui.click
# escrever -> Pyautogui.wirte
# apertar uma tecla -> pyautogui.press
# atalho -> pyautogui.hotkey
# scroll -> pyautogui.scroll

# Uma pausa de 1 segundo para todas as atividades
pyautogui.PAUSE = 1

# Apertar a tecla WINDOWS
pyautogui.press("win")

# Escrever o navegador
pyautogui.write("edge")

# Apertar ENTER
pyautogui.press("enter")

# Digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# Apertar ENTER
pyautogui.press("enter")

# Esperar 3 segundos
time.sleep(3)

# Passo 02 - Faze Login
pyautogui.click(x=915, y=380)

# Digitar o Email
pyautogui.write("test@gmail.com")

# Passar para o campo de senha
pyautogui.press("tab")

# Digitar a senha
pyautogui.write("1234")

# Clicar no botão Logar
pyautogui.click(x=998, y=536)
time.sleep(3)

# Passo 03 - Importar Base de Dados
import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # Passo 04 - Cadastrar um produtor
    pyautogui.click(x=783, y=276)
    # Código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # Preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # Preco Unitario
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    # Enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# Passo 05 - Repetir isso até acabar a base de dados
