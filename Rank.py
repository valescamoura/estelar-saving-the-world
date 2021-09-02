from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from functools import cmp_to_key

def cmp_score(score1, score2):
    if int(score1[1]) >= int(score2[1]):
        return -1
    else:
        return 1

def Formatar(lista):
    maior = 0
    for j in range(5):
        if len(lista[j][0]) > maior:
            maior = len(lista[j][0])
    for z in range(5):
        if len(lista[z][0]) != maior:
            lista[z][0] = lista[z][0] + ' '*(maior-len(lista[z][0]))
    maior = 0
    for j in range(5):
        if len(lista[j][1]) > maior:
            maior = len(lista[j][1])
    for z in range(5):
        if len(lista[z][1]) != maior:
            lista[z][1] = '0' * (maior - len(lista[z][1])) + lista[z][1]
    return lista

def Rank():
    janela = Window(800, 600)
    janela.set_title("Estelar: Saving the World")
    fundo = GameImage("rankingtela.png")

    keyboard = Window.get_keyboard()

    arquivo = open("ranking.txt", "r")
    rank = []
    for linha in arquivo:
       linha = linha.rstrip('\n')
       rank.append(linha.split())
    arquivo.close()

    rank.sort(key=cmp_to_key(cmp_score))
    rank = Formatar(rank)

    while True:
        fundo.draw()
        janela.draw_text('Player:', 220, 200, size=46, color=(255, 255, 0))
        janela.draw_text(str(rank[0][0]), 220, 250, size=46, color=(255, 255, 255))
        janela.draw_text(str(rank[1][0]), 220, 300, size=46, color=(255, 255, 255))
        janela.draw_text(str(rank[2][0]), 220, 350, size=46, color=(255, 255, 255))
        janela.draw_text(str(rank[3][0]), 220, 400, size=46, color=(255, 255, 255))
        janela.draw_text(str(rank[4][0]), 220, 450, size=46, color=(255, 255, 255))
        janela.draw_text('Score:', 470, 200, size=46, color=(255, 255, 0))
        janela.draw_text(str(rank[0][1]), 490, 250, size=46, color=(255, 255, 255))
        janela.draw_text(str(rank[1][1]), 490, 300, size=46, color=(255, 255, 255))
        janela.draw_text(str(rank[2][1]), 490, 350, size=46, color=(255, 255, 255))
        janela.draw_text(str(rank[3][1]), 490, 400, size=46, color=(255, 255, 255))
        janela.draw_text(str(rank[4][1]), 490, 450, size=46, color=(255, 255, 255))

        janela.update()

        if keyboard.key_pressed("esc"):
            return 0
