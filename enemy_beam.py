import pygame as pg
from enemy import Enemy

class Enemy_Beam(pg.sprite.Sprite):
    """
    敵機のビームに関するクラス
    """
    def __init__(self, enemy: Enemy):
        super().__init__()
        self.image = pg.image.load("ex05/images/enemy_beam.png")
        self.rect = self.image.get_rect()
        self.rect.center = enemy.rect.center
        self.vy = +4

    def update(self):
        """
        敵機を速度ベクトルself.vyに基づき移動（降下）させる
        ランダムに決めた停止位置_boundまで降下したら，_stateを停止状態に変更する
        引数 screen：画面Surface
        """
        self.rect.centery += self.vy
        if self.rect.centery > 650:
            self.kill()
