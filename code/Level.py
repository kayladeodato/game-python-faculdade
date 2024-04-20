import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityMediator import EntityMediator
from code.Const import COLOR_WHITE, MENU_OPTIONS, EVENT_ENEMY, WIN_HEIGHT, COLOR_GREEN, COLOR_CYAN
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # Opção do menu
        self.entity_list: list[Entity] = []

        # Extenda essa lista com base nesses elementos. Retorna uma lista
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        # Sete um cronometro toda vez que acontecer algo
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        # Desenhar o objeto
        while True:

            # Velocidade dos background que estão passando na tela.
            # Em 1 segundo estou rodanço o laço while 90 vezes
            clock.tick(60)

            # Cria o level e coloca pra rodar. Tem a ver com entidades
            for ent in self.entity_list:

                # São desenhadas as entidades
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health:.0f} | Score: {ent.score}', COLOR_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health:.0f} | Score: {ent.score}', COLOR_CYAN, (10, 45))

            # Texto a ser printado na tela
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list):.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            # Atualizar a tela
            pygame.display.flip()

            # Verificar relacionamentos de entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # Quero pegar os eventos que acontecem no pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    # Encerra o jogo
                    pygame.quit()

                    # Encerra o console
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    # Alternando os inimigos
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # Os textos são considerados superfícies em Py, cria com fundo transparente e são renderizados
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_position[0], top=text_position[1])
        self.window.blit(source=text_surf, dest=text_rect)
