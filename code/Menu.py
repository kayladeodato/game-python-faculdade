import sys
from tkinter.font import Font

import pygame
from pygame import Surface, Rect

from code.Const import COLOR_PURPLE, MENU_OPTIONS, COLOR_YELLOW_LIGHT, COLOR_ORANGE, WIN_WIDTH


class Menu:
    def __init__(self, window):
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
        menu_option = 0

        while True:
            # Desenha na tela
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(45, "Paradise", COLOR_PURPLE, ((WIN_WIDTH / 2), 70))
            self.menu_text(45, "Monster", COLOR_PURPLE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTIONS[i], COLOR_ORANGE, (WIN_WIDTH / 2, 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTIONS[i], COLOR_YELLOW_LIGHT, (WIN_WIDTH / 2, 200 + 30 * i))

            pygame.display.flip()

            # Verificar eventos
            for event in pygame.event.get():
                # Fechar a aplicação no campo fechar da tela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Se a tecla de setas for pressionada:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # Pra cima
                        if menu_option < len(MENU_OPTIONS) -1 :
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP: # Pra baixo
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) -1

                # Retornar a opção menu_option
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # Os textos são considerados superfícies em Py, cria com fundo transparente
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
