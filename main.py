import pygame
import sys
from main_character import *
from beam import Beam

"""
imageフォルダーからの読み込み
"""
img_bg = pygame.image.load("ex05/ProjExD_05/images/bg.jpg")
img_main = pygame.image.load("ex05/ProjExD_05/images/main.gif")


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
mainch_y = 0

HEIGHT = 600
WIDTH = 800


def main():
    global bg_y

    pygame.init()
    pygame.display.set_caption("シューティングゲームの背景")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()

    beams : list[Beam] = list()
    main_ch = main_character((370, 550))
    screen.blit(img_main, main_rect) # メインキャラの初期位置


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # キーが押されたら，かつキーの種類がスペースキーだったら
                    beams.append(Beam(main_ch))


        screen.blit(img_main, (360, 520))
        key_lst = pygame.key.get_pressed()


        bg_y = (bg_y + 1) % 600
        screen.blit(img_bg,[0,bg_y - 600])
        screen.blit(img_bg,[0,bg_y])
        # screen.blit(img_main, main_rect)
        main_ch.update(key_lst, screen)
        for i,j in  enumerate(beams):
            if check_screen(j.rct) != (True, True):
                del beams[i]
            else:
                j.update(screen)
        pygame.display.update()
        clock.tick(120)

if __name__ == "__main__":
    main()
