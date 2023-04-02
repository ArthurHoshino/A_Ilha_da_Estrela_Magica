import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# <==== GLOBAL VARIABLES ====>
menu_state = 'mainMenu'
levelList = [True, False]
enemyList = [False, False]
font = pygame.font.SysFont('comicsansms', 40)
TEXT_COL = (255, 255, 255)

# <==== IMPORT SPRITES ====>
button_unhover_play = pygame.image.load('sprite/play_button_unp.png').convert_alpha()
button_pressed_play = pygame.image.load('sprite/play_btn.png').convert_alpha()

button_unhover_quit = pygame.image.load('sprite/quit_button_unp.png').convert_alpha()
button_pressed_quit = pygame.image.load('sprite/quit_button.png').convert_alpha()

button_unhover_left = pygame.image.load('sprite/left_btn_unp.png').convert_alpha()
button_pressed_left = pygame.image.load('sprite/left_btn.png').convert_alpha()

button_unhover_level_1 = pygame.image.load('sprite/level_1_unp.png').convert_alpha()
button_pressed_level_1 = pygame.image.load('sprite/level_1_btn.png').convert_alpha()

button_unhover_level_2 = pygame.image.load('sprite/level_2_unp.png').convert_alpha()
button_pressed_level_2 = pygame.image.load('sprite/level_2_btn.png').convert_alpha()

class Button_1(pygame.sprite.Sprite):
    def __init__(self, image_unp, image_pressed, pos_x, pos_y, scale):
        super().__init__()
        width_unp = image_unp.get_width()
        height_unp = image_unp.get_height()
        width_pressed = image_pressed.get_width()
        height_pressed = image_pressed.get_height()

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.game_state = 0
        self.mouse_is_down = False
        self.image_list = []
        self.image_list.append(pygame.transform.scale(image_unp, (int(width_unp * scale), int(height_unp * scale))))
        self.image_list.append(pygame.transform.scale(image_pressed, (int(width_pressed * scale), int(height_pressed * scale))))
        self.image = self.image_list[0]
        self.rect = self.image.get_rect(midtop = (pos_x, pos_y))

        self.scale = scale
        self.action = False

    def mouse_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.image = self.image_list[1]
                self.rect.y = self.pos_y + (self.scale * 2)
                if self.mouse_is_down == False:
                    self.mouse_is_down = True
            elif pygame.mouse.get_pressed()[0] == False and self.mouse_is_down == True:
                self.mouse_is_down = False
                self.image = self.image_list[0]
                self.rect.y = self.pos_y

                if self.action == False:
                    self.action = True
                else:
                    self.action = False
                
        else:
            self.image = self.image_list[0]
            self.rect.y = self.pos_y
        
        return self.action

    def reset_state(self):
        self.action = False

    def update(self):
        self.mouse_click()

# <==== BUTTONS ====>
# Select buttons
button_group_play = pygame.sprite.GroupSingle()
button_play = Button_1(button_unhover_play, button_pressed_play, 400, 150, 5)
button_group_play.add(button_play)

button_group_quit = pygame.sprite.GroupSingle()
button_quit = Button_1(button_unhover_quit, button_pressed_quit, 400, 350, 5)
button_group_quit.add(button_quit)

button_group_left = pygame.sprite.GroupSingle()
button_left = Button_1(button_unhover_left, button_pressed_left, 35, 10, 3)
button_group_left.add(button_left)

# Level buttons
button_group_level_1 = pygame.sprite.GroupSingle()
button_level_1 = Button_1(button_unhover_level_1, button_pressed_level_1, 400, 450, 3)
button_group_level_1.add(button_level_1)

button_group_level_2 = pygame.sprite.GroupSingle()
button_level_2 = Button_1(button_unhover_level_2, button_pressed_level_2, 400, 375, 3)
button_group_level_2.add(button_level_2)

# Enemy buttons
button_group_inimigo_1 = pygame.sprite.GroupSingle()
button_inimigo_1 = Button_1(button_unhover_level_1, button_pressed_level_1, 80, 100, 3)
button_group_inimigo_1.add(button_inimigo_1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

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

        if button_left.mouse_click() == True:
            menu_state = 'levelMenu'
            button_left.reset_state()
        
        # if batalha_ganha == True:
        #     enemyList[variable] = True
        #     if level_completo == True:
        #         levelList[variable] = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
