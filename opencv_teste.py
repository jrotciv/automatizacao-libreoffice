import cv2
import numpy as np
import pyautogui
import mss
from time import sleep 

def capturar_tela():
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[0])
        screenshot_np = np.array(screenshot)
        gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGRA2GRAY)
    return gray_screenshot

def carregar_template(template_path):
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    largura, altura = template.shape[::-1]
    return template, largura, altura

def encontrar_template(gray_screenshot, template):
    res = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(res)
    return max_loc

def clicar(top_left, largura, altura):
    center_x = top_left[0] + largura // 2
    center_y = top_left[1] + altura // 2
    pyautogui.click(center_x, center_y)

#Abri o navegador
template, largura, altura = carregar_template('templates/chrome.png')
gray_screenshot = capturar_tela()
top_left = encontrar_template(gray_screenshot, template)
clicar(top_left, largura, altura)

# Abrir nova aba
sleep(1)
pyautogui.hotkey('ctrl', 't')
# Ir para aba do youtube music
pyautogui.write('https://music.youtube.com/')
pyautogui.press('enter')


sleep(5)
# Pesquisar música
template, largura, altura = carregar_template('templates/pesquisa.png')
gray_screenshot = capturar_tela()
top_left = encontrar_template(gray_screenshot, template)
clicar(top_left, largura, altura)
pyautogui.write('Shape of You')
pyautogui.press('enter')

# Clicar na música
sleep(5)
template, largura, altura = carregar_template('templates/musica.png')
gray_screenshot = capturar_tela()
top_left = encontrar_template(gray_screenshot, template)
clicar(top_left, largura, altura)