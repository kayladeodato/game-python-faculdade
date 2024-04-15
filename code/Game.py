import sys

import pygame as pygame

from code.Const import WIN_HEIGHT, MENU_OPTIONS, WIN_WIDTH
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        # Boa prática, dar um pygame.init()
        pygame.init()

        # Tudo que vou desenhar, criação da tela.
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            # Cria o menu
            menu = Menu(self.window)

            # Coloca pra executar
            menu_return = menu.run()

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                sys.exit()
