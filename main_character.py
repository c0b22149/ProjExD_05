import pygame

img_main = pygame.image.load("ex05/images/main.gif")
img_main = pygame.transform.scale(img_main, (img_main.get_width()*2, img_main.get_height()*2))
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
        メインキャラクターの画像Surfaceを生成する
        引数1 xy: メインキャラクタ画像の位置座標タプル
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