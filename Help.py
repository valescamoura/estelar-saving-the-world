from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *

def Ajuda():
    janela = Window(800, 600)
    janela.set_title("Estelar: Saving the World")
    fundo = GameImage("telahelp.png")

    keyboard = Window.get_keyboard()

    while True:

        if keyboard.key_pressed("esc"):
            break

        fundo.draw()
        janela.update()
