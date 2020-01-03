#!/usr/bin/python3
import pygame
from modules.level import Level

pygame.init()

tile_size = 50
board_width, board_height = 20, 20
window_width = board_width * tile_size + 30
window_height = board_height * tile_size + tile_size*2 + 45
window = pygame.display.set_mode((window_width, window_height))

black = (50, 50, 50)
border_color = (26, 32, 38)
score_board_color = (120, 120, 120)

font = pygame.font.SysFont("comicsansms", 72)

clock = pygame.time.Clock()

FPS = 60
MPS = 5

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
score_board = pygame.Surface((board_width * tile_size, tile_size*2))


def game():
    game = Level(board_width, board_height, tile_size, MPS, black, snake_head, snake_body, fruit_body)
    game_board = pygame.Surface((board_width * tile_size, board_height * tile_size))
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
        window.blit(game_board, (15, 15))
        window.blit(score_board, (15, board_height*tile_size+30))
        score_board.fill(score_board_color)
        score_board.blit(score_text, (score_board.get_width()//2-score_text.get_width()//2, score_text.get_height()//2))

        pygame.display.update()

        clock.tick(FPS)

    print(f'Score {game.snake.points}')


def menu():
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game()
                run = False
                exit('-> User quit')

        # Logic

        # Drawing
        window.fill((255, 255, 255))

        pygame.display.update()

        clock.tick(FPS)


if __name__ == "__main__":
    menu()
