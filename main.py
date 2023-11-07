import pygame
import sys
from enemy import Enemy
from enemy_beam import Enemy_Beam
from endgame import Game_over
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

"""
タイトルボタン
"""
game_started = False  # フラグ
game_ov = False
bg_color = (200, 200, 200)
text_color = (0, 0, 0)
button_color = (111, 131, 255)
button_hover_color = (25, 93, 174)

HEIGHT = 600
WIDTH = 800
RIGHT = 3

def draw_button(screen, button_rect, button_text, button_color):
    """
    タイトル画面のボタンの描画
    引数：ボタンの座標、テキスト、色
    """
    pygame.draw.rect(screen, button_color, button_rect)
    font = pygame.font.SysFont(None, 40)
    text = font.render(button_text, True, text_color)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

def main():
    global bg_y,score
    global game_started
    global game_ov

    pygame.init()
    pygame.display.set_caption("Fighter Jet!")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    emys = pygame.sprite.Group()
    emy_beams = pygame.sprite.Group()
    game_over=Game_over()
    start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 125, 200, 100)
    start_button_hover = False
    game_over_button_rect= pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 25, 200, 100)
    game_over_button_hover = False



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
            if event.type == pygame.MOUSEMOTION:  # メニュー選択
                if start_button_rect.collidepoint(event.pos):
                    start_button_hover = True
                else:
                    start_button_hover = False

                if game_over_button_rect.collidepoint(event.pos):
                    game_over_button_hover = True
                else:
                    game_over_button_hover = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_hover and not game_started and not game_ov:
                    game_started = True
                elif game_over_button_hover:  # ゲーム終了ボタンが押されたらウィンドウを閉じる
                    pygame.quit()
                    sys.exit()
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
        if game_started:
    # 敵機生成
            emys.add(Enemy("white") for _ in range(10))
            game_started=False
            game_ov=True
        if not game_started and not game_ov:
            screen.fill(bg_color)
            draw_button(screen, start_button_rect, "Let's Fight!!", button_color if start_button_hover else button_hover_color)
            draw_button(screen, game_over_button_rect, "Game End...", button_color if game_over_button_hover else button_hover_color)

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
        game_over.update(screen)
        tmr += 1
        clock.tick(120)
        
if __name__ == "__main__":
    main()
