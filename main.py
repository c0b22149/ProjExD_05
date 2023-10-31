import pygame
import sys

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

def check_screen(obj_rct: pygame.Rect):
    """
    引数: 敵キャラRect敵Rect
    戻り値；タプル（横方方向判定結果, 縦方向判定結果)
    画面内ならTrue, 画面外ならFalse
    """
    width, height = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        width = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        height = False

    return width, height

class main_character:
    """
    ゲームキャラクターに関するクラス
    """
    delta = {  # 押下キーと移動量の辞書
        pygame.K_LEFT: (-5, 0),
        pygame.K_RIGHT: (+5, 0),
    }

    def __init__(self, xy: tuple[int, int]):
        """
        こうかとん画像Surfaceを生成する
        引数1 num：こうかとん画像ファイル名の番号
        引数2 xy：こうかとん画像の位置座標タプル
        """
        self.img = img_main
        self.rct = self.img.get_rect()
        self.rct.center = xy

    def update(self, key_lst: list[bool], screen: pygame.Surface):
        """
        押下キーに応じてメインキャラを移動させる
        引数1 key_lst：押下キーの真理値リスト
        引数2 screen：画面Surface
        """
        sum_mv = [0, 0]
        for k, mv in __class__.delta.items():
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        self.rct.move_ip(sum_mv)
        if check_screen(self.rct) != (True, True):
            self.rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(self.img, self.rct)

class Beam:
    def __init__(self, ch: main_character):
        """
        ビーム画像Surfaceを生成
        引数 bird: メインキャラのインスタンス
        """
        img = pygame.image.load("ex05/ProjExD_05/images/main_beam.png")
        self.img = pygame.transform.rotate(img, 90)
        self.rct = ch.rct
        self.rct.centery = ch.rct.centery
        self.vx, self.vy = +5, -10

    def update(self, screen: pygame.Surface):
        """
        ビームを速度vxに従って移動させる
        引数 screen:画面Surface
        """
        self.rct.move_ip(self.vx, self.vy)
        screen.blit(self.img, self.rct)

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    # キーが押されたら，かつキーの種類がスペースキーだったら
                    beams.append(Beam(main_ch))


        screen.blit(img_main, (360, 520))
        key_lst = pygame.key.get_pressed()

        # """矢印キー判定(移動量)"""
        # delta = {   # 矢印キーと移動量の辞書
        # pygame.K_LEFT:  (-5, 0),
        # pygame.K_RIGHT: (+5, 0),
        # }
        # key_lst = pygame.key.get_pressed()
        # sum_mv = [0, 0]
        # for key, mv in delta.items():
        #     if key_lst[key]:
        #         sum_mv[0] += mv[0]
        #         sum_mv[1] += mv[1]
        # """mainキャラ"""
        # main_rect.move_ip(sum_mv[0], sum_mv[1]) # メインキャラの移動
        # if check_screen(main_rect) != (True, True): # スクリーン判定
        #     main_rect.move_ip(-sum_mv[0], -sum_mv[1])

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
