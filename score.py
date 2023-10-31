import pygame
import sys

def initialize_game():
    # Pygameの初期化
    pygame.init()

    # ウィンドウのサイズ
    WIDTH, HEIGHT = 800, 600

    # ウィンドウを作成
    return pygame.display.set_mode((WIDTH, HEIGHT))

def increase_score(score, time_passed, score_increment_interval):
    # 時間経過を追跡
    time_passed += clock.get_time()

    # 一定の時間経過ごとにスコアを増加
    if time_passed >= score_increment_interval:
        score += 1
        time_passed -= score_increment_interval

    return score, time_passed

# ゲームのクロックを設定
clock = pygame.time.Clock()
# スコアを初期化
score = 0
# 時間経過用の変数
time_passed = 0
score_increment_interval = 1000  # ミリ秒単位で1秒ごとにスコアを増加
# ウィンドウを作成
screen = initialize_game()
# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # スコアを増加
    score, time_passed = increase_score(score, time_passed, score_increment_interval)

    # 画面をクリア
    screen.fill((0, 0, 0))

    # スコアを表示
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
    
# Pygameの終了
pygame.quit()
sys.exit()
