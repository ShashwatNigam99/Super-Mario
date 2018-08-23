""" Contains all game parameters in one place """

from colorama import init, Fore, Style, Back
init(autoreset=True)


class Lives:
    lives = 3


SC_LENGTH = 40
SC_WIDTH = 100
SC_FULLWIDTH = 500

MARIO_LENGTH = 4
MARIO_WIDTH = 3
MARIO_INIT_X = 32
MARIO_INIT_Y = 4

SCENE_MOVE_AFTER = 60

ALLOWED_INPUTS = ['w', 'a', 'd', 'A', 'C', 'D']

SCORE_DIST = 10
SCORE_KILLED = 100

SPEED = {1: 0.25,
         2: 0.2,
         3: 0.15}

colors = {
    'Black': '\x1b[0;30m',
    'Blue': '\x1b[0;34m',
    'Green': '\x1b[0;32m',
    'Cyan': '\x1b[0;36m',
    'Red': '\x1b[0;31m',
    'Purple': '\x1b[0;35m',
    'Brown': '\x1b[0;33m',
    'Gray': '\x1b[0;37m',
    'Dark Gray': '\x1b[1;30m',
    'Light Blue': '\x1b[1;34m',
    'Light Green': '\x1b[1;32m',
    'Light Cyan': '\x1b[1;36m',
    'Light Red': '\x1b[1;31m',
    'Light Purple': '\x1b[1;35m',
    'Yellow': '\x1b[1;33m',
    'White': '\x1b[1;37m'
}
RESET = '\x1b[0m'

groundx = 36
barriers = [colors['Brown']+'#'+RESET, '#', '$']
killers = [colors['Blue']+'~', '~', '{', '}']
beaters = ['^']
