import pygame

HEIGHT = 600
WIDTH = 800

class Game_over():

    def __init__(self):
        self.font = pygame.font.Font(None, 100)
        self.color = (255, 0, 0)
        self.score = 0
        self.image = self.font.render(f"GAME OVER ", 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = 400, HEIGHT-300

    def update(self, screen: pygame.Surface):
        self.image = self.font.render(f"GAME OVER ", 0, self.color)
        screen.blit(self.image, self.rect)