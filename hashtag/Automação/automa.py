import pyautogui
import time 
import pandas as pd

pyautogui.PAUSE = 0.5

# abri o windos
# abrir o navegador
# pesquisar o link
# logar no site 
# cadastrar um time 
# repetir 
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.press('win')
pyautogui.write('brave')

pyautogui.press('enter')

time.sleep(5)
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)
pyautogui.click(x=652, y=509)
pyautogui.write('elias@gmail.com')
pyautogui.press('tab') # aqui vai para a senha
pyautogui.write('senha') # escreve a senha
pyautogui.press('tab') # vai para o botão
pyautogui.press('enter')

# cadastro
tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:
    pyautogui.click(x=801, y=365)
    # codigo
    codigo = str(tabela.loc[linha, 'codigo'])
    
    pyautogui.write(codigo)
    pyautogui.press('tab')
    
    # marca
    marca = str(tabela.loc[linha, 'marca'])
    
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    # tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    # categoria
    
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
    # preço unitario
    preco = str(tabela.loc[linha, 'preco_unitario'])
    
    pyautogui.write(preco)
    pyautogui.press('tab')
    
    # custo
    custo = str(tabela.loc[linha, 'custo'])
     
    pyautogui.write(custo)
    pyautogui.press('tab')
    
    # obs
   
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    
    # enviar
    pyautogui.press('tab')
    pyautogui.press('enter')
    # pyautogui.click(x=835, y=754)

    pyautogui.scroll(1000)