#!/usr/bin/python

import pygame
from modules.level import Level
from modules.button import Button
from modules.screen import Screen

pygame.init()


scale = 0.75
board_width, board_height = 20, 20

FPS = 60
mps = 5
clock = pygame.time.Clock()

black = (50, 50, 50)
border_color = (26, 32, 38)
score_board_color = (120, 120, 120)


def update_scale_dependents():
    global tile_size, buff, window_width, window_height, window
    # Window managment variables
    tile_size = int(50 * scale)
    buff = int(15 * scale)
    window_width = (board_width * tile_size) + buff*2
    window_height = (board_height * tile_size) + tile_size*2 + buff*3
    window = pygame.display.set_mode((window_width, window_height))

    global score_board, font
    # Score board
    score_board = pygame.Surface((board_width * tile_size, tile_size * 2))
    font = pygame.font.SysFont("", int(72 * scale))


def snake_game_loop():
    # Snake head
    snake_head = pygame.Surface((tile_size, tile_size))
    snake_head.fill((50, 200, 50))
    # Snake body
    snake_body = pygame.Surface((tile_size, tile_size))
    snake_body.fill((50, 100, 50))
    # Fruit body
    fruit_body = pygame.Surface((tile_size, tile_size))
    fruit_body.fill((200, 65, 65))

    game = Level(board_width, board_height, tile_size, mps, black, snake_head, snake_body, fruit_body)
    game_board = pygame.Surface((board_width * tile_size, board_height * tile_size))
    window.fill(border_color)

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
        score_txt = font.render(f"Score: {game.snake.points}", True, black)

        # Drawing
        game.draw(game_board)
        window.blit(game_board, (buff, buff))
        window.blit(score_board, (buff, board_height * tile_size + (buff * 2)))
        score_board.fill(score_board_color)
        score_board.blit(score_txt, (score_board.get_width()//2 - score_txt.get_width()//2, score_txt.get_height()//2))

        pygame.display.update()

        clock.tick(FPS)

    print(f'Score {game.snake.points}')


def menu():
    menu_screen = Screen()
    menu_screen.add_button(Button(x=window_width // 2, y=window_height, width=300, height=150, scale=scale,
                                  text='Play snake!', font=int(72 * scale), trigger=snake_game_loop, tag='button_play'))
    menu_screen.add_button(Button(x=window_width // 2, y=window_height, width=250, height=100, scale=scale,
                                  text='Change scale', font=int(48 * scale), trigger=update_scale, tag='button_scale'))
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit('-> User quit')

        # Logic
        menu_screen.update(pygame.mouse)

        # Drawing
        window.fill((255, 255, 255))

        menu_screen.draw(window)

        pygame.display.update()
        clock.tick(FPS)


def update_scale():
    global scale
    scale = float(input("New scale:"))
    update_scale_dependents()


if __name__ == "__main__":
    update_scale_dependents()
    menu()

pygame.quit()
