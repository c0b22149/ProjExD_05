import pygame
from main_character import *

class Beam:
    def __init__(self, ch: main_character):
        """
        ビーム画像Surfaceを生成
        引数 bird: メインキャラのインスタンス
        """
        img = pygame.image.load("ex05/images/main_beam.png")
        self.img = pygame.transform.rotate(img, 90)

        # メインキャラの中心座標を取得
        center_x = ch.rect.centerx
        center_y = ch.rect.centery

        # ビームのrectの中心をメインキャラの中心に合わせる
        self.rect = self.img.get_rect(center=(center_x, center_y))

        # 上方向に速度を設定
        self.vx, self.vy = 0, -10

    def update(self, screen: pygame.Surface):
        """
        ビームを速度vxに従って移動させる
        引数 screen:画面Surface
        """
        self.rect.move_ip(self.vx, self.vy)
        screen.blit(self.img, self.rect)
        # hit = pygame.sprite.spritecollide(self, emys, True)
        # if hit:
        #     # 衝突した敵をemysグループから削除
        #     hit[0].kill()
