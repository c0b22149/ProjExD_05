import pygame
import sys
from enemy import Enemy
from enemy_beam import Enemy_Beam

img_bg = pygame.image.load("ex05/images/bg.jpg")

bg_y = 0

HEIGHT = 600
WIDTH = 800

def main():
    global bg_y

    pygame.init()
    pygame.display.set_caption("Fighter Jet!")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    emys = pygame.sprite.Group()
    emy_beams = pygame.sprite.Group()

    # 敵機生成
    emys.add(Enemy("white") for _ in range(10))

    tmr = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.key.key_code("e"):
                for emy in emys:
                    emy_beams.add(Enemy_Beam(emy))
            if event.type == pygame.KEYDOWN and event.key == pygame.key.key_code("g"):
                emys.add(Enemy("green") for _ in range(10))
            if event.type == pygame.KEYDOWN and event.key == pygame.key.key_code("r"):
                emys.add(Enemy("red") for _ in range(10))

        # 敵が停止している and 180フレームに1回ビームを発射
        for emy in emys:
            if emy.state == "stop" and tmr % 180 == 0:
                emy_beams.add(Enemy_Beam(emy))

        # 敵機のビームの発射
        for emy in emys:
            if emy.state == "stop" and emy.is_beam == False:
                emy_beams.add(Enemy_Beam(emy))
                emy.is_beam = True

        bg_y = (bg_y + 1) % 600
        screen.blit(img_bg,[0,bg_y - 600])
        screen.blit(img_bg,[0,bg_y])
        print(tmr)

        emys.update()
        emys.draw(screen)
        emy_beams.update()
        emy_beams.draw(screen)
        pygame.display.update()
        tmr += 1
        clock.tick(600)
        
if __name__ == "__main__":
    main()
