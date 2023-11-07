import pygame
import sys
from endgame import Game_over

img_bg = pygame.image.load("ex05/images/bg.jpg")

bg_y = 0

HEIGHT = 600
WIDTH = 800
RIGHT = 3

def main():
    global bg_y

    pygame.init()
    pygame.display.set_caption("シューティングゲームの背景")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    game_over=Game_over()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg_y = (bg_y + 1) % 600
        screen.blit(img_bg,[0,bg_y - 600])
        screen.blit(img_bg,[0,bg_y])

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT: #プログラム終了
            return

        pygame.display.update()
        game_over.update(screen)
        clock.tick(120)



      
if __name__ == "__main__":
    
    main()
