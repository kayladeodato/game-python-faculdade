#C
import pygame

COLOR_PURPLE = (178, 102, 255)
COLOR_YELLOW_LIGHT = (255, 255, 204)
COLOR_ORANGE = (255, 178, 102)
COLOR_WHITE = (255, 255, 255)

#E
EVENT_ENEMY = pygame.USEREVENT
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 3, # cada vez que rodar o while vai mover 3 pixels
                'Player2': 3,
                'Enemy1': 4,
                'Enemy2': 5
                }

#I
IMAGE_LENGTH = {7}

#M
MENU_OPTIONS = ('NEW GAME 1P',
                'NEW GAME 2P - COOPERATIVE',
                'NEW GAME 2P - COMPETITIVE',
                'EXIT')


#W
WIN_WIDTH = 576
WIN_HEIGHT = 324

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
