from colorama import init, Fore, Back, Style
from msvcrt import getch, kbhit
from time import sleep
import sys
import level

init()

escapeStart = "\x1B["
CLEAR_SCREEN = escapeStart + "2J"

specialKeyInputEscape = ["\x00", "\xE0"]

class Key:
    ARROW_LEFT = 0
    ARROW_RIGHT = 1
    ARROW_UP = 2
    ARROW_DOWN = 3
    ESCAPE = 4

class GameMode:
    SINGLE_PLAYER = 0
    MULTI_PLAYER = 1
    HELP = 2

def clear_screen():
    print(CLEAR_SCREEN)


def input_ready():
    return kbhit()

def get_input():
    #getch returns a bytes object, so we get the first byte for the actual value
    input = getch()[0]

    if input == 0x0 or input == 0xE0:
        #special key, so we have to call getch multiple times to figure out what it was
        input = getch()[0]

        if input == 0x48:
            return Key.ARROW_UP
        elif input == 0x50:
            return Key.ARROW_DOWN
        elif input == 0x4D:
            return Key.ARROW_RIGHT
        elif input == 0x4B:
            return Key.ARROW_LEFT
    else:
        #standard key press
        if input == 27:
            return Key.ESCAPE


def print_instructions():
    print("-----Rodent's Revenge-----")
    print("")
    print("Controls: arrow keys or a, w, s, d. Press Control+C at any time to quit")
    print("" * 2)

def get_desired_game_mode():
    while True:
        print("What would you like?")
        print("(S)ingleplayer, (M)ultiplayer, (H)elp")

        line = sys.stdin.readline().replace("\n", "")
        upper_line = line.upper()

        if upper_line == "S":
            return GameMode.SINGLE_PLAYER
        elif upper_line == "M":
            return GameMode.MULTI_PLAYER
        elif upper_line == "H":
            return GameMode.HELP

        print("Unknown option \"{0}\". Options: S, M, H\n\n".format(line))

def single_player_game():
    pass


clear_screen()

level.gen_level()

print_instructions()

game_mode = get_desired_game_mode()

if game_mode == GameMode.SINGLE_PLAYER:
    single_player_game()
elif game_mode == GameMode.MUTIPLAYER:
    multi_player_game()
elif game_mode == GameMode.HELP:
    pass

while True:
    if input_ready():
        key = get_input()

        if key == Key.ESCAPE:
            sys.exit(0)

        print(key)

    sleep(0.1)
