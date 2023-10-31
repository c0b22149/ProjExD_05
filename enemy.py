import pygame as pg
import random

HEIGHT = 600
WIDTH = 800

level_lst = ["white", "green", "red"]

class Enemy(pg.sprite.Sprite):
    """
    敵機に関するクラス
    """
    def __init__(self, level: str ="white"):
        super().__init__()
        self.level = level if level in level_lst else "white"
        self.loaded_image = pg.image.load(f"ex05/images/enemy_{self.level}.gif")
        self.image = pg.transform.scale(self.loaded_image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = random.randint(30, WIDTH-30), 0
        self.vy = +3
        self.bound = random.randint(250, HEIGHT-230)  # 停止位置
        self.state = "down"
        self.is_beam = False
        

    def update(self):
        """
        敵機を速度ベクトルself.vyに基づき移動（降下）させる
        ランダムに決めた停止位置_boundまで降下したら，_stateを停止状態に変更する
        引数 screen：画面Surface
        """
        if self.rect.centery > self.bound:
            self.vy = 0
            self.state = "stop"
        self.rect.centery += self.vy
