import pygame
import sys
from enemy import Enemy
from enemy_beam import Enemy_Beam
from main_character import *
from beam import Beam

"""
imageフォルダーからの読み込み
"""
img_bg = pygame.image.load("ex05/images/bg.jpg")
img_main = pygame.image.load("ex05/images/main.gif")


"""
読み込んだイメージに対する操作
"""
img_main = pygame.transform.scale(img_main, (img_main.get_width()*2, img_main.get_height()*2))
main_rect = img_main.get_rect()
main_rect.center = (370, 550)


"""
初期座標
"""
bg_y = 0
score = 0
mainch_y = 0

HEIGHT = 600
WIDTH = 800


def main():
    global bg_y,score

    pygame.init()
    pygame.display.set_caption("Fighter Jet!")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    emys = pygame.sprite.Group()
    emy_beams = pygame.sprite.Group()

    # 敵機生成
    emys.add(Enemy("white") for _ in range(10))

    tmr = 0
    beams : list[Beam] = list()
    main_ch = main_character((370, 550))
    screen.blit(img_main, main_rect) # メインキャラの初期位置


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
            # 敵機のビームの発射
            for emy in emys:
                if emy.state == "stop" and emy.is_beam == False:
                    emy_beams.add(Enemy_Beam(emy))
                    emy.is_beam = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        # キーが押されたら，かつキーの種類がスペースキーだったら
                        beams.append(Beam(main_ch))

        # 敵が停止している and 180フレームに1回ビームを発射
        for emy in emys:
            if emy.state == "stop" and tmr % 180 == 0:
                emy_beams.add(Enemy_Beam(emy))


        screen.blit(img_main, (360, 520))
        key_lst = pygame.key.get_pressed()


        bg_y = (bg_y + 1) % 600
        screen.blit(img_bg,[0,bg_y - 600])
        screen.blit(img_bg,[0,bg_y])
        
        #scoreの表示
        font_score = pygame.font.Font(None,36)
        text_score = font_score.render(f"Score:{score}",True,(255,255,255))
        screen.blit(text_score,(10,10))

        emys.update()
        emys.draw(screen)
        emy_beams.update()
        emy_beams.draw(screen)
        tmr += 1

        # screen.blit(img_main, main_rect)
        main_ch.update(key_lst, screen)
        for i,j in  enumerate(beams):
            if check_screen(j.rct) != (True, True):
                del beams[i]
            else:
                j.update(screen)
        pygame.display.update()
        tmr += 1
        clock.tick(120)

if __name__ == "__main__":
    main()
