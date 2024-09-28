import pygame as pg
from main_screen import Window
import time
import neat

def game():
    t_s = time.time()
    pg.init()
    play = Window()
    play.run()
    pg.quit()
    return time.time() - t_s


def main():
    return game()


if __name__ == '__main__':
    main()
