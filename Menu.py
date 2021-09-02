from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sound import *
from Play import *
from Help import *
from Rank import *

janela = Window(800, 600)
janela.set_title("Estelar: Saving the World")
fundo = GameImage("fundo.png")

keyboard = Window.get_keyboard()
mouse = Window.get_mouse()

musica = Sound("tema.ogg")
musica.set_volume(80)
musica.play()

while True:
    play = Sprite("play.png")
    play.x = janela.width/2 - play.width/2
    play.y = 220

    ajuda = Sprite("help.png")
    ajuda.x = janela.width/2 - ajuda.width/2
    ajuda.y = 220 + play.height + 20

    rank = Sprite("rank.png")
    rank.x = janela.width/2 - rank.width/2
    rank.y = ajuda.y + 20 + ajuda.height

    exit = Sprite("exit.png")
    exit.x = janela.width/2 - exit.width/2
    exit.y = rank.y + 20 + rank.height

    if mouse.is_over_area([play.x, play.y], [play.x+play.width, play.y+play.height]):
        play = Sprite("play2.png")
        play.x = janela.width/2 - play.width/2
        play.y = 220
        if mouse.is_button_pressed(1):
            musica.pause()
            Play()
            musica.unpause()
    elif mouse.is_over_area([ajuda.x, ajuda.y], [ajuda.x + ajuda.width, ajuda.y + ajuda.height]):
        ajuda = Sprite("help2.png")
        ajuda.x = janela.width/2 - play.width/2 - 10
        ajuda.y = 220 + play.height + 20
        if mouse.is_button_pressed(1):
            Ajuda()
    elif mouse.is_over_area([rank.x, rank.y], [rank.x + rank.width, rank.y + rank.height]):
        rank = Sprite("rank2.png")
        rank.x = janela.width/2 - play.width/2 - 8
        rank.y = ajuda.y + 20 + ajuda.height
        if mouse.is_button_pressed(1):
            Rank()
    elif mouse.is_over_area([exit.x, exit.y], [exit.x + exit.width, exit.y + exit.height]):
        exit = Sprite("exit2.png")
        exit.x = janela.width/2 - play.width/2 - 8
        exit.y = rank.y + 20 + rank.height
        if mouse.is_button_pressed(1):
            janela.close()

    fundo.draw()
    play.draw()
    ajuda.draw()
    rank.draw()
    exit.draw()
    janela.update()
