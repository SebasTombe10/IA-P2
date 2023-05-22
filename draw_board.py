import pygame 
import button

# Cargar las imágenes
casilla_blanca_img = pygame.image.load('images/casilla_blanca.png')
casilla_negra_img = pygame.image.load('images/casilla_negra.png')

GRID_SIZE=8
CELL_SIZE=75

buttons = []

def board(surface):
    # Crear matriz de botones
 
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            # Alternar entre las imágenes
            if (row + col) % 2 == 0:
                buttonx = button.Button(x, y, casilla_blanca_img,1)
            else:
                buttonx = button.Button(x, y, casilla_negra_img,1)
            
            buttons.append(buttonx)
    #Fila 1 
    if buttons[0].draw(surface):
           return print("F1la 1 - posicion 0")
    if buttons[1].draw(surface):
           return print("F1la 1 - posicion 1")
    if buttons[2].draw(surface):
           return print("F1la 1 - posicion 2")
    if buttons[3].draw(surface):
           return print("F1la 1 - posicion 3")
    if buttons[4].draw(surface):
           return print("F1la 1 - posicion 4")
    if buttons[5].draw(surface):
           return print("F1la 1 - posicion 5")
    if buttons[6].draw(surface):
           return print("F1la 1 - posicion 6")
    if buttons[7].draw(surface):
           return print("F1la 1 - posicion 7")
    
    #Fila 2 
    if buttons[8].draw(surface):
           return print("F1la 2 - posicion 0")
    if buttons[9].draw(surface):
           return print("F1la 2 - posicion 1")
    if buttons[10].draw(surface):
           return print("F1la 2 - posicion 2")
    if buttons[11].draw(surface):
           return print("F1la 2 - posicion 3")
    if buttons[12].draw(surface):
           return print("F1la 2 - posicion 4")
    if buttons[13].draw(surface):
           return print("F1la 2 - posicion 5")
    if buttons[14].draw(surface):
           return print("F1la 2 - posicion 6")
    if buttons[15].draw(surface):
           return print("F1la 2 - posicion 7")
    
    #Fila 3 
    if buttons[16].draw(surface):
           return print("F1la 3 - posicion 0")
    if buttons[17].draw(surface):
           return print("F1la 3 - posicion 1")
    if buttons[18].draw(surface):
           return print("F1la 3 - posicion 2")
    if buttons[19].draw(surface):
           return print("F1la 3 - posicion 3")
    if buttons[20].draw(surface):
           return print("F1la 3 - posicion 4")
    if buttons[21].draw(surface):
           return print("F1la 3 - posicion 5")
    if buttons[22].draw(surface):
           return print("F1la 3 - posicion 6")
    if buttons[23].draw(surface):
           return print("F1la 3 - posicion 7")
    
    #Fila 4 
    if buttons[24].draw(surface):
           return print("F1la 4 - posicion 0")
    if buttons[25].draw(surface):
           return print("F1la 4 - posicion 1")
    if buttons[26].draw(surface):
           return print("F1la 4 - posicion 2")
    if buttons[27].draw(surface):
           return print("F1la 4 - posicion 3")
    if buttons[28].draw(surface):
           return print("F1la 4 - posicion 4")
    if buttons[29].draw(surface):
           return print("F1la 4 - posicion 5")
    if buttons[30].draw(surface):
           return print("F1la 4 - posicion 6")
    if buttons[31].draw(surface):
           return print("F1la 4 - posicion 7")
    
    #Fila 5 
    if buttons[32].draw(surface):
           return print("F1la 5 - posicion 0")
    if buttons[33].draw(surface):
           return print("F1la 5 - posicion 1")
    if buttons[34].draw(surface):
           return print("F1la 5 - posicion 2")
    if buttons[35].draw(surface):
           return print("F1la 5 - posicion 3")
    if buttons[36].draw(surface):
           return print("F1la 5 - posicion 4")
    if buttons[37].draw(surface):
           return print("F1la 5 - posicion 5")
    if buttons[38].draw(surface):
           return print("F1la 5 - posicion 6")
    if buttons[39].draw(surface):
           return print("F1la 5 - posicion 7")
    
    #Fila 6 
    if buttons[40].draw(surface):
           return print("F1la 6 - posicion 0")
    if buttons[41].draw(surface):
           return print("F1la 6 - posicion 1")
    if buttons[42].draw(surface):
           return print("F1la 6 - posicion 2")
    if buttons[43].draw(surface):
           return print("F1la 6 - posicion 3")
    if buttons[44].draw(surface):
           return print("F1la 6 - posicion 4")
    if buttons[45].draw(surface):
           return print("F1la 6 - posicion 5")
    if buttons[46].draw(surface):
           return print("F1la 6 - posicion 6")
    if buttons[47].draw(surface):
           return print("F1la 6 - posicion 7")
    
    #Fila 7 
    if buttons[48].draw(surface):
           return print("F1la 7 - posicion 0")
    if buttons[49].draw(surface):
           return print("F1la 7 - posicion 1")
    if buttons[50].draw(surface):
           return print("F1la 7 - posicion 2")
    if buttons[51].draw(surface):
           return print("F1la 7 - posicion 3")
    if buttons[52].draw(surface):
           return print("F1la 7 - posicion 4")
    if buttons[53].draw(surface):
           return print("F1la 7 - posicion 5")
    if buttons[54].draw(surface):
           return print("F1la 7 - posicion 6")
    if buttons[55].draw(surface):
           return print("F1la 7 - posicion 7")
    
    #Fila 7 
    if buttons[56].draw(surface):
           return print("F1la 8 - posicion 0")
    if buttons[57].draw(surface):
           return print("F1la 8 - posicion 1")
    if buttons[58].draw(surface):
           return print("F1la 8 - posicion 2")
    if buttons[59].draw(surface):
           return print("F1la 8 - posicion 3")
    if buttons[60].draw(surface):
           return print("F1la 8 - posicion 4")
    if buttons[61].draw(surface):
           return print("F1la 8 - posicion 5")
    if buttons[62].draw(surface):
           return print("F1la 8 - posicion 6")
    if buttons[63].draw(surface):
           return print("F1la 8 - posicion 7")
    
