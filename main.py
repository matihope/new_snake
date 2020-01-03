#!/usr/bin/python3
import pygame
from modules.level import Level
from modules.button import Button

pygame.init()

SCALE = 0.5

TILE_SIZE = int(50 * SCALE)
BUFF = int(15 * SCALE)
BOARD_WIDTH, BOARD_HEIGHT = 20, 20
WINDOW_WIDTH = (BOARD_WIDTH * TILE_SIZE) + BUFF*2
WINDOW_HEIGHT = (BOARD_HEIGHT * TILE_SIZE) + TILE_SIZE*2 + BUFF*3
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

black = (50, 50, 50)
border_color = (26, 32, 38)
score_board_color = (120, 120, 120)

font = pygame.font.SysFont("", int(72*SCALE), bold=True)

clock = pygame.time.Clock()

FPS = 60
MPS = 5

# Snake head
snake_head = pygame.Surface((TILE_SIZE, TILE_SIZE))
snake_head.fill((50, 200, 50))
# Snake body
snake_body = pygame.Surface((TILE_SIZE, TILE_SIZE))
snake_body.fill((50, 100, 50))
# Fruit body
fruit_body = pygame.Surface((TILE_SIZE, TILE_SIZE))
fruit_body.fill((200, 65, 65))
# Score board
score_board = pygame.Surface((BOARD_WIDTH * TILE_SIZE, TILE_SIZE*2))


def game_loop():
    game = Level(BOARD_WIDTH, BOARD_HEIGHT, TILE_SIZE, MPS, black, snake_head, snake_body, fruit_body)
    game_board = pygame.Surface((BOARD_WIDTH * TILE_SIZE, BOARD_HEIGHT * TILE_SIZE))
    window.fill(border_color)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game.snake.dead = True
                break

        # Logic
        game.handle_logic(pygame.key.get_pressed())
        if game.snake.dead:
            break
        score_text = font.render(f"Score: {game.snake.points}", True, black)

        # Drawing
        game.draw(game_board)
        window.blit(game_board, (BUFF, BUFF))
        window.blit(score_board, (BUFF, BOARD_HEIGHT*TILE_SIZE+(BUFF*2)))
        score_board.fill(score_board_color)
        score_board.blit(score_text, (score_board.get_width()//2-score_text.get_width()//2, score_text.get_height()//2))

        pygame.display.update()

        clock.tick(FPS)

    print(f'Score {game.snake.points}')


def menu():
    button_play = Button(x=WINDOW_WIDTH//2-150*SCALE, y=WINDOW_HEIGHT-200*SCALE, width=300*SCALE, height=150*SCALE, text='Play!', font=int(72*SCALE), trigger=game_loop)
    button_apply = Button(x=WINDOW_WIDTH//2-100*SCALE, y=WINDOW_HEIGHT-400*SCALE, width=200*SCALE, height=100*SCALE, text='Apply', font=int(48*SCALE))

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                exit('-> User quit')

        # Logic
        for button in Button.button_list:
            button.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], pygame.mouse.get_pressed()[0])

        # Drawing
        window.fill((255, 255, 255))

        for button in Button.button_list:
            button.draw(window)

        pygame.display.update()

        clock.tick(FPS)


if __name__ == "__main__":
    menu()
