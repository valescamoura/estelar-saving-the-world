from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.animation import *
from PPlay.sound import *
from random import randint

def Play():

    janela = Window(800, 600)
    janela.set_title("Estelar: Saving the World")

    keyboard = Window.get_keyboard()

    contador_vidas = GameImage("cont_vidas.png")
    contador_cristais = GameImage("cont_cristal.png")
    contador_cristais.x = contador_vidas.width + 2

    #CRIAR CENARIO
    x_da_tela = 0
    cenario = []
    for i in range(10):
        fundo = [Sprite("background1.png"), Sprite("background2.png"), Sprite("background3.png")]
        for j in range(3):
            fundo[j].x = x_da_tela
        x_da_tela += janela.width
        fundo[2].y = fundo[1].height - fundo[2].height
        cenario.append(fundo)

    #CRIAR PLATAFORMAS FIXAS
    x_da_plat = janela.width/2 - 46
    plataformas = []
    for i in range(3):
        for j in range(8):
            plat = Sprite("plataforma.png")
            plat.x = x_da_plat
            plat.y = 300
            x_da_plat += plat.width + 40
            plataformas.append(plat)
        x_da_plat = (janela.width/2 - 46) + 3*(i+1)*janela.width
    plataformas[0].y = 440
    plataformas[1].y = 370
    plataformas[6].x = plataformas[0].x + 2*janela.width
    plataformas[6].y = 440
    plataformas[7].x = plataformas[1].x + 2*janela.width
    plataformas[7].y = 370
    plataformas[8].y = 440
    plataformas[9].y = 370
    plataformas[14].x = plataformas[8].x + 2*janela.width
    plataformas[14].y = 440
    plataformas[15].x = plataformas[9].x + 2 * janela.width
    plataformas[15].y = 370
    plataformas[16].y = 440
    plataformas[17].y = 370
    plataformas[22].x = plataformas[16].x + 2 * janela.width
    plataformas[22].y = 440
    plataformas[23].x = plataformas[17].x + 2 * janela.width
    plataformas[23].y = 370

    #CRAIR PLATAFORMAS MOVEIS E CRISTAIS
    x_da_plat = plataformas[5].x + plataformas[5].width + 50
    cristais = []
    for i in range(3):
        plat = Sprite("plataforma.png")
        plat.x = x_da_plat
        plat.y = 300
        plataformas.append(plat)
        crist = Sprite("cristal.png")
        crist.x = x_da_plat + plat.width/2 - crist.width/2 + 50
        crist.y = plat.y - crist.height - 200
        cristais.append(crist)
        x_da_plat = x_da_plat + 3 * janela.width
    cont_plat = 150
    vel_plat = 1

    #CRIAR CORACOES
    coracao = []
    for i in range(3):
        corac = Sprite("coração.png")
        corac.y = 170 - corac.height
        coracao.append(corac)
    coracao[0].x = plataformas[7].x + plataformas[7].width/2 - corac.width/2
    coracao[1].x = plataformas[15].x + plataformas[15].width / 2 - corac.width / 2
    coracao[2].x = plataformas[23].x + plataformas[23].width / 2 - corac.width / 2

    #CRIAR ESTELAR
    estelar = Sprite("rparada.png", 12)
    x_estelar = 0
    y_estelar = janela.height - estelar.height
    estelar.y = y_estelar
    magia_estelar = []
    vel_magia = 3

    #CRIAR VILOES
    viloes = []
    x_vilao = 800
    vel_vilao = -80
    for i in range(25):
        vilao = Sprite("left.png", 4)
        vilao.x = x_vilao
        vilao.y = janela.height - vilao.height
        x_vilao += 290
        vilao.set_total_duration(1000)
        viloes.append(vilao)

    # NAVE DO VILAO
    navev = Sprite('navevilão2.png')
    navev.x = janela.width
    navev.y = 40
    vel_navev = -280
    cont = 20

    # VILAO ALEATORIO
    nave_aleat = Sprite("navevilão2.png")
    nave_aleat.x = janela.width
    nave_aleat.y = 20
    aleat = randint(600, 1200)
    time_nave_aleat = 2
    lista_de_tiros = []

    #VARIAVEIS DE CONTROLE
    cont_vidas = 5
    cont_cristais = 0
    delta_time = 1
    delta_time2 = 1   #pular
    delta_time3 = 1   #atirar
    delta_time4 = 1.5   #colisao
    move = "r"
    pula = False
    plat_up = False
    plat_up_aux = False
    plat_atual = 0
    plat_movel = False
    score = 0

    #VARIAVEIS DE FIM DE JOGO
    winner = Sprite("winner.png")
    winner.x = janela.width/2 - winner.width/2
    winner.y = janela.height/2 - winner.height/2
    gameover = Sprite("gameover.png")
    gameover.x = janela.width/2 - gameover.width/2
    gameover.y = janela.height/2 - gameover.height/2
    final = Sprite("navevilão.png")
    final.set_position(cenario[9][0].x + janela.width - final.width, janela.height - final.height)

    # VILÃ PRINCIPAL
    vila = Sprite("vila_parada.png", 16)
    vila.set_position(final.x - 1 - vila.width, janela.height - vila.height)
    time_vila = 1.5
    time_vvila = 1
    magia_vila = []
    vidas_vila = 3
    morreu = 0

    #FPS
    fps = 0
    contador = 0
    tempo_transcorrido = 0

    #SONS:
    som_pulo = Sound('pulo.ogg')
    som_navev = Sound('somnavev.ogg')
    som_efeito = Sound('efeito.ogg')
    som_colisao_est_v = Sound("estelar_vilao.ogg")
    som_winner = Sound("tema.ogg")
    som_gameover = Sound("gameoversom.ogg")
    som_tiro_nave_aleat = Sound("tironave.ogg")
    som_magia = Sound("som_magia.ogg")
    som_colisao = Sound("somcolisao.ogg")

    ######## LOOP ########
    while True:
        delta_time += janela.delta_time()
        delta_time2 += janela.delta_time()
        delta_time3 += janela.delta_time()
        delta_time4 += janela.delta_time()
        time_nave_aleat += janela.delta_time()
        time_vila += janela.delta_time()
        aleat -= 1
        andando = False

        # NAVE ALEATORIA
        if aleat <= 0:
            if nave_aleat.x + nave_aleat.width >= 0:
                nave_aleat.x -= 3
                if time_nave_aleat >= 1:
                    som_tiro_nave_aleat.set_volume(50)
                    som_tiro_nave_aleat.play()
                    tiro = Sprite("tiro_nave.png")
                    tiro.set_position(nave_aleat.x+nave_aleat.width-tiro.width/2, nave_aleat.y+nave_aleat.height)
                    lista_de_tiros.append(tiro)
                    time_nave_aleat = 0
            else:
                nave_aleat.x = janela.width
                aleat = randint(600, 1200)

        #COLISAO DO TIRO DA NAVE ALEATORIA COM A ESTELAR/MOVER/VERIFICAR COORDENADAS DO TIRO
        for z in range(len(lista_de_tiros)):
            lista_de_tiros[z].y += 3
            if lista_de_tiros[z].collided(estelar):
                cont_vidas -= 1
                lista_de_tiros.pop(z)
                som_colisao_est_v.set_volume(100)
                som_colisao_est_v.play()
                x_estelar = estelar.x
                if move == "r":
                    estelar = Sprite("rhurt.png", 6)
                else:
                    estelar = Sprite("lhurt.png", 6)
                estelar.x = x_estelar
                estelar.y = y_estelar
                estelar.set_loop(False)
                break
        if lista_de_tiros != [] and lista_de_tiros[0].y >= janela.height:
            lista_de_tiros.pop(0)

        # TEMPO TRANSCORRIDO
        tempo_transcorrido += janela.delta_time()
        contador += 1
        if tempo_transcorrido >= 1:
            fps = contador
            contador = 0
            tempo_transcorrido = 0
            print("FPS: "+str(fps))

        # SPRITE ESTELAR E MOVIMENTACAO DO CENARIO
        if keyboard.key_pressed("space") and delta_time3 > 1 and pula == False:
            delta_time3 = 0
            som_magia.set_volume(100)
            som_magia.play()
            x_estelar = estelar.x
            if move == "r":
                estelar = Sprite("rmagia.png", 7)
                magia = Sprite("power.png", 11)
                magia.x = x_estelar
                vel_magia = 3
            else:
                estelar = Sprite("lmagia.png", 7)
                magia = Sprite("power.png", 11)
                magia.x = x_estelar - magia.width
                vel_magia = -3
            estelar.set_loop(False)
            estelar.x = x_estelar
            estelar.y = y_estelar
            magia.set_total_duration(4000)
            magia.set_loop(False)
            magia.y = estelar.y - 12
            magia_estelar.append([magia, vel_magia])
        elif keyboard.key_pressed("up") and delta_time2 > 1:
            delta_time2 = 0
            pula = True
            x_estelar = estelar.x
            if move == "r":
                estelar = Sprite("rpulando.png", 9)
            else:
                estelar = Sprite("lpulando.png", 9)
            estelar.set_loop(False)
            estelar.x = x_estelar
            estelar.y = y_estelar
            som_pulo.set_volume(50)
            som_pulo.play()
        elif keyboard.key_pressed("right") and delta_time4 >= 1 and delta_time3 > 1:
            move = "r"
            if pula == False and delta_time >= 1:
                andando = True
                delta_time = 0
                x_estelar = estelar.x
                estelar = Sprite("randando.png", 12)
                estelar.set_loop(False)
                estelar.x = x_estelar
                estelar.y = y_estelar
            if estelar.x >= janela.width/2 - estelar.width/2 and cenario[9][0].x > 0:
                vel_roll = -100
                for i in range(10):
                    for j in range(3):
                        cenario[i][j].move_x(vel_roll * janela.delta_time())
                for i in range(27):
                    plataformas[i].move_x(vel_roll*janela.delta_time())
                for i in range(len(coracao)):
                    coracao[i].move_x(vel_roll*janela.delta_time())
                for i in range(len(cristais)):
                    cristais[i].move_x(vel_roll*janela.delta_time())
                for i in range(len(viloes)):
                    viloes[i].move_x(vel_roll*janela.delta_time())
                final.move_x(vel_roll*janela.delta_time())
                vila.move_x(vel_roll*janela.delta_time())
                if aleat <= 0 and nave_aleat.x >= 0:
                    nave_aleat.move_x(vel_roll*janela.delta_time())
                for i in range(len(lista_de_tiros)):
                    lista_de_tiros[i].move_x(vel_roll*janela.delta_time())
            else:
                if estelar.x <= janela.width - estelar.width:
                    estelar.move_x(100 * janela.delta_time())
                    x_estelar = estelar.x
        elif keyboard.key_pressed("left") and delta_time4 >= 1:
            move = "l"
            if pula == False and delta_time >= 1:
                andando = True
                delta_time = 0
                x_estelar = estelar.x
                estelar = Sprite("landando.png", 12)
                estelar.set_loop(False)
                estelar.x = x_estelar
                estelar.y = y_estelar
            if estelar.x >= janela.width/2 - estelar.width/2 and cenario[0][0].x < 0:
                vel_roll = 100
                for i in range(10):
                    for j in range(3):
                        cenario[i][j].move_x(vel_roll * janela.delta_time())
                for i in range(27):
                    plataformas[i].move_x(vel_roll*janela.delta_time())
                for i in range(len(coracao)):
                    coracao[i].move_x(vel_roll*janela.delta_time())
                for i in range(len(cristais)):
                    cristais[i].move_x(vel_roll*janela.delta_time())
                for i in range(len(viloes)):
                    viloes[i].move_x((vel_roll*janela.delta_time()))
                final.move_x(vel_roll * janela.delta_time())
                vila.move_x(vel_roll*janela.delta_time())
                if aleat <= 0 and nave_aleat.x >= 0:
                    nave_aleat.move_x(vel_roll*janela.delta_time())
                for i in range(len(lista_de_tiros)):
                    lista_de_tiros[i].move_x(vel_roll*janela.delta_time())
            else:
                if estelar.x > 0:
                    estelar.move_x(-100 * janela.delta_time())
                    x_estelar = estelar.x
        elif not estelar.is_playing() and andando == False:
            if move == "r":
                estelar = Sprite("rparada.png", 12)
                estelar.x = x_estelar
                estelar.y = y_estelar
            else:
                estelar = Sprite("lparada.png", 12)
                estelar.x = x_estelar
                estelar.y = y_estelar

        # MOVIMENTAR STELAR NO EIXO Y (PULAR/VERIFICAR SE ESTA EM CIMA DA PLATAFORMA)
        if delta_time2 < 0.5 and pula == True:
            estelar.move_y(-500*janela.delta_time())
        elif 0.5 <= delta_time2 < 1 and pula == True:
            for i in range(27):
                if plataformas[i].x <= estelar.x + estelar.width/2 <= plataformas[i].x + plataformas[i].width and plataformas[i].y - 20 <= estelar.y + estelar.height <= plataformas[i].y:
                    pula = False
                    plat_up = True
                    plat_atual = i
                    estelar.stop()
                    y_estelar = plataformas[i].y - 90
                    if i > 23:
                        plat_movel = True
            estelar.move_y(500*janela.delta_time())
        elif delta_time2 >= 1 and pula is True:
            pula = False

        #VERIFICAR SE ESTA EM CIMA DA PLATAFORMA E DESCER
        if plat_up is True:
            if not (plataformas[plat_atual].x <= estelar.x + estelar.width/2 <= plataformas[plat_atual].x + plataformas[plat_atual].width) and pula is False:
                plat_up = False
                if move == "r":
                    estelar = Sprite("rpulando.png", 9)
                else:
                    estelar = Sprite("lpulando.png", 9)
                estelar.y = y_estelar
                estelar.x = x_estelar
                estelar.set_sequence(4, 8, loop=False)
                plat_up_aux = True
                if plat_atual > 23:
                    plat_movel = False
        if plat_up is False and plat_up_aux is True:
            estelar.y += 4
            y_estelar = estelar.y
            if estelar.y >= janela.height - estelar.height:
                plat_up_aux = False

        # MOVIMENTAR PLATAFORMA/CORACAO/CRISTAL
        for i in range(24, 27):
            plataformas[i].x += vel_plat
        for i in range(len(cristais)):
            cristais[i].y += vel_plat
        for i in range(len(coracao)):
            coracao[i].y += vel_plat
        if plat_movel is True:
            estelar.x += vel_plat
        if cont_plat < 0:
            vel_plat *= -1
            cont_plat = 150
        cont_plat -= 1

        #COLISAO DO CRISTAL E DO CORACAO COM ESTELAR
        for i in range(len(coracao)):
            if estelar.collided(coracao[i]):
                som_efeito.set_volume(100)
                som_efeito.play()
                coracao.pop(i)
                cont_vidas += 1
                break
        for i in range(len(cristais)):
            if estelar.collided(cristais[i]):
                som_efeito.set_volume(100)
                som_efeito.play()
                cristais.pop(i)
                cont_cristais += 1
                break

        #VERIFICAR COORDENADAS DA MAGIA
        if magia_estelar != [] and (magia_estelar[0][0].x >= janela.width or magia_estelar[0][0].x + magia_estelar[0][0].width <= 0):
            magia_estelar.pop(0)

        #COLISAO DA MAGIA COM O VILAO
        for i in range(len(viloes)):
            if magia_estelar != [] and viloes[i].collided(magia_estelar[0][0]):
                magia_estelar.pop(0)
                som_magia.stop()
                som_colisao.set_volume(100)
                som_colisao.play()
                score += 100
                viloes.pop(i)

        #COLISAO DA ESTELAR COM O VILAO
        if delta_time4 >= 2:
            for i in range(len(viloes)):
                if viloes[i].collided(estelar):
                    som_colisao_est_v.set_volume(100)
                    som_colisao_est_v.play()
                    delta_time4 = 0
                    cont_vidas -= 1
                    x_estelar = estelar.x
                    if move == "r":
                        estelar = Sprite("rhurt.png", 6)
                    else:
                        estelar = Sprite("lhurt.png", 6)
                    estelar.x = x_estelar
                    estelar.y = y_estelar
                    estelar.set_loop(False)

        #CONTROLAR VILÃ
        if vila.x + vila.width + 10 < janela.width:
            if time_vila >= 2.5 and morreu == 0:
                time_vila = 0
                som_magia.set_volume(100)
                som_magia.play()
                vila = Sprite("vila_magia.png", 10)
                vila.set_loop(False)
                vila.set_position(final.x - 1 - vila.width, janela.height - vila.height)
                magia = Sprite("vila_power.png", 11)
                magia.set_total_duration(2000)
                magia.set_loop(False)
                magia.x = vila.x - magia.width
                magia.y = vila.y - 12
                magia_vila.append(magia)
            elif vidas_vila <= 0 and morreu == 0:
                if time_vvila >= 1:
                    vila = Sprite("vila_gameover.png", 6)
                    vila.set_loop(False)
                    vila.set_position(final.x - 1 - vila.width, janela.height - vila.height)
                elif time_vvila <= 0:
                    morreu = 1
                time_vvila -= janela.delta_time()
            elif not vila.is_playing() and morreu == 0:
                vila = Sprite("vila_parada.png", 16)
                vila.set_loop(False)
                vila.set_position(final.x - 1 - vila.width, janela.height - vila.height)
            elif morreu == 1:
                vila.x = janela.width + 1000

        #COLISAO DA MAGIA ESTELAR COM MAGIA DA VILA/VILA
        for i in range(len(magia_estelar)):
            if magia_vila != [] and magia_estelar[i][0].collided(magia_vila[0]):
                magia_vila.pop(i)
                magia_estelar.pop(i)
                break
            if magia_estelar[i][0].collided(vila):
                vidas_vila -= 1
                som_magia.stop()
                som_colisao.set_volume(100)
                som_colisao.play()
                vila = Sprite("vila_hurt.png", 6)
                vila.set_loop(False)
                vila.set_position(final.x - 1 - vila.width, janela.height - vila.height)
                magia_estelar.pop(i)
                score += 200
                break

        #COLISAO MAGIA DA VILA E ESTELAR E VERIFICAR COORDENADAS DO TIRO DA VILA
        for i in range(len(magia_vila)):
            if magia_vila[i].collided(estelar):
                cont_vidas -= 1
                magia_vila.pop(i)
                som_colisao_est_v.set_volume(100)
                som_colisao_est_v.play()
                x_estelar = estelar.x
                if move == "r":
                    estelar = Sprite("rhurt.png", 6)
                else:
                    estelar = Sprite("lhurt.png", 6)
                estelar.x = x_estelar
                estelar.y = y_estelar
                estelar.set_loop(False)
                break
        if magia_vila != [] and magia_vila[0].y <= 0:
            magia_vila.pop(0)

        ### UPDATE
        for i in range(10):
            for j in range(3):
                cenario[i][j].draw()
        for i in range(27):
            plataformas[i].draw()
        for i in range(len(coracao)):
            coracao[i].draw()
        for i in range(len(cristais)):
            cristais[i].draw()
        final.draw()
        contador_vidas.draw()
        janela.draw_text(str(cont_vidas), contador_vidas.width / 2 + 4, 10, size=30)
        contador_cristais.draw()
        janela.draw_text(str(cont_cristais), contador_cristais.x + contador_cristais.width / 2 + 4, 8, size=30)
        janela.draw_text("Score:"+str(score), janela.width - 200, 8, size=30, color=[255, 255, 0])
        estelar.set_total_duration(1000)
        estelar.draw()
        estelar.update()
        #MAGIA DA VILÃ
        for i in range(len(magia_vila)):
            magia_vila[i].draw()
            magia_vila[i].x -= 3
            magia_vila[i].update()
        # NAVE VILÃO PASSANDO ANTES DO VILÃO APARECER
        if navev.x + navev.width >= 0:
            cont -= 1
            if cont == 0:
                som_navev.set_volume(40)
                som_navev.play()
            elif cont < 0:
                navev.draw()
                navev.move_x(vel_navev * janela.delta_time())
                if navev.x + navev.width < 0:
                    som_navev.pause()
        #DESENHAR E MOVIMENTAR VILOES
        for i in range(len(viloes)):
            viloes[i].draw()
            viloes[i].update()
            if 0 - viloes[i].width <= viloes[i].x <= janela.width:
                viloes[i].move_x(vel_vilao*janela.delta_time())
        nave_aleat.draw()
        for i in range(len(lista_de_tiros)):
            lista_de_tiros[i].draw()
        vila.set_total_duration(1000)
        vila.draw()
        vila.update()
        # MAGIA DA ESTELAR (DESENHAR/MOVER)
        for i in range(len(magia_estelar)):
            magia_estelar[i][0].draw()
            magia_estelar[i][0].x += magia_estelar[i][1]
            magia_estelar[i][0].update()
        janela.update()

        #VOLTAR AO MENU
        if keyboard.key_pressed("esc"):
            return 0

        #GANHOU
        if cont_cristais == 3 and estelar.collided(final):
            winner.draw()
            janela.draw_text("Digite seu nome para ser registrado no Rank:", 200, 470, size=20, color=(255, 255, 0))
            janela.update()
            som_winner.set_volume(70)
            som_winner.play()
            print("Digite seu nome (max=10 caract.) para ser registrado no Rank:")
            arquivo = open("ranking.txt", "a")
            nome = input()
            arquivo.write(nome + '\t' + str(score) + '\n')
            arquivo.close()
            som_winner.stop()
            return 0

        #PERDEU
        if cont_vidas <= 0:
            gameover.draw()
            janela.draw_text("Digite seu nome para ser registrado no Rank:", 200, 470, size=20, color=(255, 255, 0))
            janela.update()
            som_gameover.set_volume(70)
            som_gameover.play()
            print("Digite seu nome (max=10 caract.) para ser registrado no Rank:")
            arquivo = open("ranking.txt", "a")
            nome = input()
            arquivo.write(nome + '\t' + str(score) + '\n')
            arquivo.close()
            som_gameover.stop()
            return 0
