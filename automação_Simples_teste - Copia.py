import pyautogui
import pandas as pd
import time
# 1 Abrir o sistema
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
#linha 10 colocar o site
pyautogui.write('')
pyautogui.press('enter')
# 2 Entrar no cadastro
time.sleep (5)
pyautogui.click(x=392, y=410)
pyautogui.write('Teste@gmail.com')
pyautogui.prTeste@gmail.com Senhac55ef
ess('tab')
pyautogui.write('Senhac55ef')
pyautogui.press('tab')
pyautogui.press('enter')
# 3 Base de Dados usando Pandas
tabela = pd.read_csv('produtos.csv')
# 4 atribuições de cada produto/ cadastrar cada produto
for linha in tabela.index:
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.click(x=450, y=295)
    pyautogui.write(codigo)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))  
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('home')
    