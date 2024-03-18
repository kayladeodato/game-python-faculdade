import pygame
from pygame import Surface


class Menu:
    def __int__(self, window):
        # self é o atributo (self.window), se não tiver o self é uma variável (window)
        self.window: Surface = window

        # Cria uma superfície carregando uma imagem de fundo. O convert alpha é para otimizar a renderização da imagem.
        self.surf = pygame.image.load('./asset/mountain-bg.png').convert_alpha()

        # Onde quero que a imagem seja posicionada. Obtém o retângulo a partir da superfície
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # Coloca a música e deixa ela tocando
        pygame.mixer_music.load('./asset/menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            # Desenha na tela
            self.window.blit(source=self.surf, dest=self.rect)

            # Escrever na tela/Atualiza a tela
            pygame.display.flip()
        pass
