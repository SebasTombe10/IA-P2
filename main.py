import pygame
import button
import draw_board

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)
font_sub = pygame.font.SysFont("arial", 20)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
titulo_img = pygame.image.load("images/titulo.png").convert_alpha()
principiante_img = pygame.image.load("images/principiante.png").convert_alpha()
amateur_img = pygame.image.load("images/amateur.png").convert_alpha()
experto_img = pygame.image.load('images/experto.png').convert_alpha()
home_img = pygame.image.load("images/home.png").convert_alpha()


#create button instances
titulo_button = button.Button(100, 100, titulo_img, 1)
principiante_button = button.Button(300, 280, principiante_img, 1)
amateur_button = button.Button(300, 360, amateur_img, 1)
experto_button = button.Button(300, 440, experto_img, 1)
home_button = button.Button(750,10,home_img,1)



def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw title
      titulo_button.draw(screen)
      #draw pause screen buttons
      if principiante_button.draw(screen):
        menu_state = "principiante"
      if amateur_button.draw(screen):
        menu_state = "amateur"
      if experto_button.draw(screen):
        menu_state = "experto"

    if menu_state == "principiante":
       draw_text("Principiante", font_sub, TEXT_COL, 660, 10)
       action_board = draw_board.board(screen)
       if home_button.draw(screen):
         menu_state = "main"
         action_board = None

    if menu_state == "amateur":
       draw_text("Amateur", font_sub, TEXT_COL, 660, 10)
       action_board = draw_board.board(screen)
       if home_button.draw(screen):
         menu_state = "main"
         action_board = None

    if menu_state == "experto":
       draw_text("Experto", font_sub, TEXT_COL, 660, 10)
       action_board = draw_board.board(screen)
       if home_button.draw(screen):
         menu_state = "main"
         action_board = None
       

    """#check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
        """
  else:
    draw_text("Bienvenido a", font, TEXT_COL, 250, 50)
    titulo_button.draw(screen)
    draw_text("Presiona ESPACIO para continuar", font_sub, TEXT_COL, 270, 180)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()