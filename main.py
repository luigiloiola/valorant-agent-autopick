import pyautogui
from pyautogui import locateCenterOnScreen
from time import sleep
from python_imagesearch.imagesearch import imagesearch, imagesearch_loop

chamber = ('chamber',720,903)
cypher =('cypher',795,920)
jett=('jett',869,918)
kayo = ('kayo',972,930)
ekko = ('ekko',1039,915)
reyna = ('reyna',1133,912)
sage = ('sage',1222,914)
sova = ('sova',1306,908)
viper=('viper',651,1005)
raze = ('raze',1142,1004)

agentes = [chamber, cypher, jett, kayo, ekko, reyna, sage, sova, viper, raze]

def pick_valorant(agente=jett):
    pos = imagesearch_loop(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\cypher.png',1)
    if pos:
        pyautogui.moveTo(agente[1],agente[2])
        pyautogui.click()
        pyautogui.click()
        pyautogui.moveTo(956, 814)
        pyautogui.click()

boneco = input('digite o agente: ')
for i in agentes:
    if boneco.upper() == i[0].upper():
        boneco = i
        break

pick_valorant(boneco)

