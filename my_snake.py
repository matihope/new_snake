#!/usr/bin/python

import pygame
from modules.level import Level
from modules.button import Button

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
    tile_size = int(50 * scale)
    buff = int(15 * scale)
    window_width = (board_width * tile_size) + buff*2
    window_height = (board_height * tile_size) + tile_size*2 + buff*3
    window = pygame.display.set_mode((window_width, window_height))

    global snake_head, snake_body, fruit_body, score_board, font
    # Snake head
    snake_head = pygame.Surface((tile_size, tile_size))
    snake_head.fill((50, 200, 50))
    # Snake body
    snake_body = pygame.Surface((tile_size, tile_size))
    snake_body.fill((50, 100, 50))
    # Fruit body
    fruit_body = pygame.Surface((tile_size, tile_size))
    fruit_body.fill((200, 65, 65))
    # Score board
    score_board = pygame.Surface((board_width * tile_size, tile_size * 2))

    font = pygame.font.SysFont("", int(72 * scale))

    Button(x=window_width // 2 - 150 * scale, y=window_height - 200 * scale, width=300 * scale,
           height=150 * scale, text='Play!', font=int(72 * scale), trigger=game_loop, tag='button_play')
    Button(x=window_width // 2 - 100 * scale, y=window_height - 400 * scale, width=200 * scale,
           height=100 * scale, text='Apply', font=int(48 * scale), trigger=update_scale, tag='button_apply')


def game_loop():
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
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit('-> User quit')

        # Logic
        for _, button in Button:
            button.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], pygame.mouse.get_pressed()[0])

        # Drawing
        window.fill((255, 255, 255))

        for _, button in Button:
            button.draw(window)

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
