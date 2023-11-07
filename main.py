import pygame
import sys
from enemy import Enemy
from enemy_beam import Enemy_Beam
from endgame import Game_over
from main_character import *
from beam import Beam
import random

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
#
last_score_update_time = 0
RIGHT = 3


def main():
    global bg_y,score,last_score_update_time

    pygame.init()
    pygame.display.set_caption("Fighter Jet!")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    emys = pygame.sprite.Group()
    emy_beams = pygame.sprite.Group()
    game_over=Game_over()

    # 敵機生成
    emys.add(Enemy("white") for _ in range(10))

    tmr = 0
    beams : list[Beam] = list()
    main_ch = main_character((370, 550))
    screen.blit(img_main, main_rect) # メインキャラの初期位置


    while True:
        #
        current_time = pygame.time.get_ticks()
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT: #プログラム終了
                return

        # 敵が停止している and 180フレームに1回ビームを発射
        for emy in emys:
            if emy.state == "stop" and tmr % 300 == 0: 
                 emy_beams.add(Enemy_Beam(emy))

        if emys.sprites() == []:
            cho = random.choice(["white", "green", "red"])
            emys.add(Enemy(cho) for _ in range(10))

        # メインキャラと敵ビームの衝突判定  
        if pygame.sprite.spritecollide(main_ch, emy_beams, False):
            # ゲームオーバー処理
            pygame.quit()
            sys.exit()
    
        # メインキャラと敵の衝突判定 
        for bem in beams:
            hit_to_emy = pygame.sprite.spritecollide(bem, emys, False)
            if hit_to_emy:
                level = hit_to_emy[0].get_level()
                if level == "white":
                    score += 1
                elif level == "green":
                    score += 10
                elif level == "red":
                    score += 20
                hit_to_emy[0].kill()

        screen.blit(img_main, (360, 520))
        key_lst = pygame.key.get_pressed()


        bg_y = (bg_y + 1) % 600
        screen.blit(img_bg,[0,bg_y - 600])
        screen.blit(img_bg,[0,bg_y])

        #
        if current_time - last_score_update_time >=1000:
            score += 1
            last_score_update_time = current_time

        
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
        for i,j in enumerate(beams):
            if check_screen(j.rect) != (True, True):
                del beams[i]
            else:
                j.update(screen)
        pygame.display.update()
        clock.tick(100)

if __name__ == "__main__":
    main()
  