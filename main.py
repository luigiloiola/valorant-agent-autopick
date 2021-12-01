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
print(agentes)



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






#
# try:
#     while True:
#         x, y = pyautogui.position()
#         position = f'x:{x}  //  y:{y}'
#         print(position)
#         sleep(5)
# except:
#     pass




#
# def is_loop():
#     pos = imagesearch_loop(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\encontrar partrida.png',1)
#     if pos:
#         pyautogui.click(x=pos[0], y=pos[1])


    # pos = imagesearch_loop(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\role.png', 1)
    # if pos:
    #     print(pos)
    #     pyautogui.click(x=pos[0], y=pos[1])
    #     pyautogui.move(0, -94)
    #     pyautogui.click()
    # pos = imagesearch_loop(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\role.png', 1)
    # if pos:
    #     pyautogui.click(x=pos[0], y=pos[1])
    #     pyautogui.move(-98, 0)
    #     pyautogui.click()
    #

        # pos2 = imagesearch_loop(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\role.png', 1)
# is_loop()


# # x:404  //  y:196


# x:802  //  y:639
# x:802  //  y:545
# x:704  //  y:631