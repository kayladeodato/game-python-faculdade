import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDGET, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        # Boa prática, dar um pygame.init()
        pygame.init()

        # Tudo que vou desenhar, criação da tela.
        self.window = pygame.display.set_mode(size=(WIN_WIDGET, WIN_HEIGHT))

    def run(self):
        while True:
            # Cria o menu
            menu = Menu(self.window)
            self.menu_text(50, "Ocean", (255, 229, 204), (WIN_WIDGET/2), 70)

            # Coloca pra executar
            menu.run()
            pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # Os textos são considerados superfícies em Py, cria com fundo transparente
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.window.blit(source=text_surf, dest=text_rect)
