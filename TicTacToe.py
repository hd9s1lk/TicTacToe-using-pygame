import pygame 
from pygame.locals import * 
from consts import *

pygame.init()

#Janela de jogo
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TicTacToe by Henrique!")


def draw_grid():
    bg = (255,255,200)
    grid = (50,50,50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x* 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x*100,0),(x*100, screen_width), line_width)

markers = []
clicked = False
pos = []
player = 1
font = pygame.font.SysFont(None,40)
again_rect = Rect(50,180,200,50)

#lista das casas
for x in range(3):
    row = [0] * 3
    markers.append(row)


#logica do jogo
def draw_markers():
    x_pos = 0
    for marker in markers:
        y_pos = 0
        for y in marker:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 +15, y_pos * 100 +15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos * 100 +15, y_pos * 100 +85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50 ,y_pos *100 + 50), 38, line_width)
            y_pos +=1
        x_pos +=1


def check_winner():
    global winner
    global game_over
    y_pos = 0
    for marker in markers:
        #colunas
        if sum(marker) == 3:
            winner = 1
            game_over = True
        if sum(marker) == -3:
            winner = 2
            game_over = True
        #linhas
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
           winner = 1
           game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
           winner = 2
           game_over = True
        y_pos +=1


    #cruzado
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True

def show_winner(winner):
    win_text = "Player " + str(winner) + "wins!"
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen, green, (50,100, 200, 50))
    screen.blit(win_img, (50,110))


    again_text = "Play again?"
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen,green, again_rect)
    screen.blit(again_img, (50, 190))
    



#evento de jogo
while running:

    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()
    if game_over == True:
        show_winner(winner)

        #ver se clicou
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    #reset ao jogo
                    markers = []
                    pos = []
                    player = 1
                    winner = 0
                    game_over = False
                    for x in range(3):
                        row = [0] * 3
                        markers.append(row)




    pygame.display.update()
        
pygame.quit()