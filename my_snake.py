#!/usr/bin/python

import pygame
from modules.level import Level
from modules.button import Button
from modules.screen import Screen


scale = 0.75
board_width, board_height = 20, 20

smooth = False
FPS = 60
mps = 5
clock = pygame.time.Clock()

black = (50, 50, 50)
border_color = (26, 32, 38)
score_board_color = (120, 120, 120)

# Unscaled window
TILE_SIZE = 50
BUFF = 15
WINDOW_WIDTH = (board_width * TILE_SIZE) + BUFF * 2
WINDOW_HEIGHT = (board_height * TILE_SIZE) + TILE_SIZE * 2 + BUFF * 3
WINDOW = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

# Score board
score_board = pygame.Surface((board_width * TILE_SIZE, TILE_SIZE * 2))
FONT = pygame.font.SysFont("", 72)


def update_scale_dependents():
    global window_width_real, window_height_real, window_real

    # window_real variables
    t_s = TILE_SIZE * scale
    b_s = BUFF * scale
    window_width_real = int((board_width * t_s) + b_s*2)
    window_height_real = int((board_height * t_s) + t_s*2 + b_s*3)
    window_real = pygame.display.set_mode((window_width_real, window_height_real))


def snake_game_loop():
    # Snake head
    snake_head = pygame.Surface((TILE_SIZE, TILE_SIZE))
    snake_head.fill((50, 200, 50))
    # Snake body
    snake_body = pygame.Surface((TILE_SIZE, TILE_SIZE))
    snake_body.fill((50, 100, 50))
    # Fruit body
    fruit_body = pygame.Surface((TILE_SIZE, TILE_SIZE))
    fruit_body.fill((200, 65, 65))

    game = Level(board_width, board_height, TILE_SIZE, mps, black, snake_head, snake_body, fruit_body)
    game_board = pygame.Surface((board_width * TILE_SIZE, board_height * TILE_SIZE))
    WINDOW.fill(border_color)

    run_game = True
    while run_game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game.snake.dead = True
                run_game = False
                pygame.quit()
                exit('-> User quit')
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    run_game = False

        # Logic
        game.handle_logic(pygame.key.get_pressed())
        if game.snake.dead:
            break
        score_txt = FONT.render(f"Score: {game.snake.points}", True, black)

        # Drawing
        game.draw(game_board)
        WINDOW.blit(game_board, (BUFF, BUFF))

        score_board.fill(score_board_color)
        score_board.blit(score_txt, (score_board.get_width()//2 - score_txt.get_width()//2, score_txt.get_height()//2))
        WINDOW.blit(score_board, (BUFF, board_height * TILE_SIZE + (BUFF * 2)))

        real_draw(WINDOW, draw_smooth=smooth)
        pygame.display.update()
        clock.tick(FPS)

    print(f'Score {game.snake.points}')


def menu():
    menu_screen = Screen()
    menu_screen.add_button(Button(x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT-75, width=300, height=150,
                                  text='Play snake!', font_size=72, trigger=snake_game_loop, tag='button_play'))
    menu_screen.add_button(Button(x=WINDOW_WIDTH//2, y=WINDOW_HEIGHT-300, width=250, height=100,
                                  text='Change scale', font_size=48, trigger=update_scale, tag='button_scale'))
    menu_screen.add_button(Button(x=WINDOW_WIDTH // 2, y=WINDOW_HEIGHT - 500, width=250, height=100,
                                  text='Toggle smooth', font_size=48, trigger=toggle_smooth,
                                  long_click=False, tag='button_smooth'))

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit('-> User quit')

        # Logic
        m = pygame.mouse
        menu_screen.update(m.get_pos()[0]/scale, m.get_pos()[1]/scale, m.get_pressed()[0])

        # Drawing
        WINDOW.fill((255, 255, 255))

        menu_screen.draw(WINDOW)

        real_draw(WINDOW, draw_smooth=smooth)
        pygame.display.update()
        clock.tick(FPS)


def update_scale():
    global scale
    scale = float(input("New scale:"))
    update_scale_dependents()


def real_draw(surface, draw_smooth=False):
    """Function that is responsible for drawing to real window"""
    if draw_smooth:
        pygame.transform.smoothscale(surface, (window_width_real, window_height_real), window_real)
    else:
        pygame.transform.scale(surface, (window_width_real, window_height_real), window_real)


def toggle_smooth():
    global smooth
    smooth = not smooth


if __name__ == "__main__":
    pygame.init()

    update_scale_dependents()
    menu()

pygame.quit()
