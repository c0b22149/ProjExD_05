import pygame
import sys

img_bg = pygame.image.load("ex05/images/bg.jpg")

bg_y = 0
game_started = False  # フラグ
game_over = False
bg_color = (200, 200, 200)
text_color = (0, 0, 0)
button_color = (111, 131, 255)
button_hover_color = (25, 93, 174)

HEIGHT = 600
WIDTH = 800

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
    global bg_y
    global game_started
    global game_over

    pygame.init()
    pygame.display.set_caption("シューティングゲームの背景")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 125, 200, 100)
    start_button_hover = False
    game_over_button_rect= pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 25, 200, 100)
    game_over_button_hover = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
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
                if start_button_hover and not game_started and not game_over:
                    game_started = True
                elif game_over_button_hover:  # ゲーム終了ボタンが押されたらウィンドウを閉じる
                    pygame.quit()
                    sys.exit()

                    
        if game_started:
            bg_y = (bg_y + 1) % 600
            screen.fill(bg_color)
            screen.blit(img_bg, [0, bg_y - 600])
            screen.blit(img_bg, [0, bg_y])
        
        if not game_started and not game_over:
            screen.fill(bg_color)
            draw_button(screen, start_button_rect, "Let's Fight!!", button_color if start_button_hover else button_hover_color)
            draw_button(screen, game_over_button_rect, "Game End...", button_color if game_over_button_hover else button_hover_color)

        pygame.display.update()
        clock.tick(120)
        
if __name__ == "__main__":
    main()