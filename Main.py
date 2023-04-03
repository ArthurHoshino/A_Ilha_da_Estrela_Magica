import pygame
import perguntas, Botao, Inimigo

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# <==== GLOBAL VARIABLES ====>
menu_state = 'mainMenu'
perguntas = perguntas.perguntas
battleActive = False
levelList, enemyList = [False, False], [False, False]
font = pygame.font.SysFont('comicsansms', 40)
TEXT_COL = (255, 255, 255)

# <==== IMPORT SPRITES ====>
button_unp_play = pygame.image.load('sprite/play_button_unp.png').convert_alpha()
button_pressed_play = pygame.image.load('sprite/play_btn.png').convert_alpha()
button_unp_quit = pygame.image.load('sprite/quit_button_unp.png').convert_alpha()
button_pressed_quit = pygame.image.load('sprite/quit_button.png').convert_alpha()

button_unp_left = pygame.image.load('sprite/left_btn_unp.png').convert_alpha()
button_pressed_left = pygame.image.load('sprite/left_btn.png').convert_alpha()

button_unp_level_1 = pygame.image.load('sprite/level_1_unp.png').convert_alpha()
button_pressed_level_1 = pygame.image.load('sprite/level_1_btn.png').convert_alpha()
button_unp_level_2 = pygame.image.load('sprite/level_2_unp.png').convert_alpha()
button_pressed_level_2 = pygame.image.load('sprite/level_2_btn.png').convert_alpha()

button_unp_a = pygame.image.load('sprite/a_btn_unp.png').convert_alpha()
button_pressed_a = pygame.image.load('sprite/a_btn.png').convert_alpha()
button_unp_b = pygame.image.load('sprite/b_btn_unp.png').convert_alpha()
button_pressed_b = pygame.image.load('sprite/b_btn.png').convert_alpha()
button_unp_c = pygame.image.load('sprite/c_btn_unp.png').convert_alpha()
button_pressed_c = pygame.image.load('sprite/c_btn.png').convert_alpha()
button_unp_d = pygame.image.load('sprite/d_btn_unp.png').convert_alpha()
button_pressed_d = pygame.image.load('sprite/d_btn.png').convert_alpha()

capanga_1 = pygame.image.load('sprite/capanga_1.png').convert_alpha()


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

# <==== BUTTONS ====>
# Select buttons
button_group_play = pygame.sprite.GroupSingle()
button_play = Botao.Button(button_unp_play, button_pressed_play, 400, 150, 5)
button_group_play.add(button_play)

button_group_quit = pygame.sprite.GroupSingle()
button_quit = Botao.Button(button_unp_quit, button_pressed_quit, 400, 350, 5)
button_group_quit.add(button_quit)

button_group_left = pygame.sprite.GroupSingle()
button_left = Botao.Button(button_unp_left, button_pressed_left, 35, 10, 3)
button_group_left.add(button_left)

# Level buttons
button_group_level_1 = pygame.sprite.GroupSingle()
button_level_1 = Botao.Button(button_unp_level_1, button_pressed_level_1, 400, 450, 3)
button_group_level_1.add(button_level_1)

button_group_level_2 = pygame.sprite.GroupSingle()
button_level_2 = Botao.Button(button_unp_level_2, button_pressed_level_2, 400, 375, 3)
button_group_level_2.add(button_level_2)

# Enemies buttons
button_group_inimigo_1 = pygame.sprite.GroupSingle()
button_inimigo_1 = Botao.Button(button_unp_level_1, button_pressed_level_1, 80, 100, 3)
button_group_inimigo_1.add(button_inimigo_1)

# Battle buttons
button_group_option_a = pygame.sprite.GroupSingle()
button_option_a = Botao.Button_Enemy(button_unp_a, button_pressed_a, 80, 350, 3, "a")
button_group_option_a.add(button_option_a)
button_group_option_b = pygame.sprite.GroupSingle()
button_option_b = Botao.Button_Enemy(button_unp_b, button_pressed_b, 430, 350, 3, 'b')
button_group_option_b.add(button_option_b)
button_group_option_c = pygame.sprite.GroupSingle()
button_option_c = Botao.Button_Enemy(button_unp_c, button_pressed_c, 80, 500, 3, 'c')
button_group_option_c.add(button_option_c)
button_group_option_d = pygame.sprite.GroupSingle()
button_option_d = Botao.Button_Enemy(button_unp_d, button_pressed_d, 430, 500, 3, 'd')
button_group_option_d.add(button_option_d)

# Enemy
capanga_group_1 = Inimigo.Enemy()

run = True
while run:
    screen.fill('White')

    # <==== MAIN MENU ====>
    if menu_state == 'mainMenu':
        draw_text('A Ilha da Estrela Mágica', font, 'Black', 245, 50)

        button_group_play.update()
        button_group_play.draw(screen)

        button_group_quit.update()
        button_group_quit.draw(screen)

        if button_play.mouse_click() == True:
            menu_state = 'map'
            button_play.reset_state()

        if button_quit.mouse_click() == True:
            run = False
    
    # <==== MAP ====>
    if menu_state == 'map':
        screen.fill((52, 78, 91))
        draw_text('MAPA', font, TEXT_COL, 350, 10)

        button_group_left.update()
        button_group_left.draw(screen)

        button_group_level_1.update()
        button_group_level_1.draw(screen)

        if button_level_1.mouse_click() == True:
            menu_state = 'levelMenu'
            button_level_1.reset_state()

        if button_left.mouse_click() == True:
            menu_state = 'mainMenu'
            button_left.reset_state()
        
        if levelList[0] == True:
            button_group_level_2.update()
            button_group_level_2.draw(screen)
        
    # <==== LEVEL MENU ====>
    if menu_state == 'levelMenu':
        screen.fill((52, 78, 91))
        draw_text('SELEÇÃO DE INIMIGO', font, TEXT_COL, 250, 10)

        button_group_left.update()
        button_group_left.draw(screen)

        button_group_inimigo_1.update()
        button_group_inimigo_1.draw(screen)

        if button_inimigo_1.mouse_click() == True:
            menu_state = 'battle'
            button_inimigo_1.reset_state()

        if button_left.mouse_click() == True:
            menu_state = 'map'
            button_left.reset_state()
    
    # <==== BATTLE ====>
    if menu_state == 'battle':
        draw_text('BATALHA ÉPICA', font, 'Black', 275, 10)

        button_group_left.update()
        button_group_left.draw(screen)

        if battleActive == False:
            capanga_group_1.battle()
            battleActive = True

        draw_text(capanga_group_1.perguntaList[-1], font, 'Black', 270, 90)

        button_group_option_a.update()
        button_group_option_a.draw(screen)
        draw_text(capanga_group_1.perguntaList[0], font, 'Black', 120, 365)

        button_group_option_b.update()
        button_group_option_b.draw(screen)
        draw_text(capanga_group_1.perguntaList[1], font, 'Black', 470, 365)

        button_group_option_c.update()
        button_group_option_c.draw(screen)
        draw_text(capanga_group_1.perguntaList[2], font, 'Black', 120, 515)

        button_group_option_d.update()
        button_group_option_d.draw(screen)
        draw_text(capanga_group_1.perguntaList[3], font, 'Black', 470, 515)
        
        # <==== ANSWER VERIFICATION ====>
        if button_option_a.mouse_click() == True:
            capanga_group_1.verifyAnswer(capanga_group_1.perguntaList[0], capanga_group_1.perguntaJaFeita[-1])
            battleActive = False
            capanga_group_1.perguntaList = []
            button_option_a.reset_state()

        if button_option_b.mouse_click() == True:
            capanga_group_1.verifyAnswer(capanga_group_1.perguntaList[1], capanga_group_1.perguntaJaFeita[-1])
            battleActive = False
            capanga_group_1.perguntaList = []
            button_option_b.reset_state()
        
        if button_option_c.mouse_click() == True:
            capanga_group_1.verifyAnswer(capanga_group_1.perguntaList[2], capanga_group_1.perguntaJaFeita[-1])
            battleActive = False
            capanga_group_1.perguntaList = []
            button_option_c.reset_state()
        
        if button_option_d.mouse_click() == True:
            capanga_group_1.verifyAnswer(capanga_group_1.perguntaList[3], capanga_group_1.perguntaJaFeita[-1])
            battleActive = False
            capanga_group_1.perguntaList = []
            button_option_d.reset_state()
        
        # <==== LEVEL COMPLETION VERIFICATION ====>
        if capanga_group_1.correct == 5:
            print('Inimigo derrotado')
            menu_state = 'map'
            enemyList[0] = True
            levelList[0] = True
        
        if capanga_group_1.wrong == 3:
            print('Foi de arrasta pra cima')
            battleActive = False
            perguntaList = []
            menu_state = 'mainMenu'
        
        if button_left.mouse_click() == True:
            menu_state = 'levelMenu'
            button_left.reset_state()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
