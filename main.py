import pygame
import sys
from score import increase_score
img_bg = pygame.image.load("ex05/images/bg.jpg")

bg_y = 0
score = 0

HEIGHT = 600
WIDTH = 800

def main():
    global bg_y,score

    pygame.init()
    pygame.display.set_caption("シューティングゲームの背景")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #スコアを増加
        score, _ = increase_score(score,0,1000)

        bg_y = (bg_y + 1) % 600
        screen.blit(img_bg,[0,bg_y - 600])
        screen.blit(img_bg,[0,bg_y])
        
        #scoreの表示
        font_score = pygame.font.Font(None,36)
        text_score = font_score.render(f"Score:{score}",True,(255,255,255))
        screen.blit(text_score,(10,10))

        pygame.display.update()
        clock.tick(120)
        
if __name__ == "__main__":
    main()
