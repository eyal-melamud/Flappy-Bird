import pygame as pg
import random


class Pipe:
    def __init__(self):
        self.__p_t = pg.image.load('pipe_t.png')
        self.__p_b = pg.image.load('pipe_b.png')
        self.__gap = 225
        self.__y = random.randint(self.__gap + 100, 796 - self.__gap)
        self.__pace = 5
        self.__x = 450 + self.__pace

    def draw(self, scr: pg.display.set_mode):
        self.__x -= self.__pace
        scr.blit(self.__p_b, (self.__x, self.__y))
        scr.blit(self.__p_t, (self.__x, self.__y - self.__gap - 650))

    def get_gap(self):
        return self.__gap

    def get_pos(self):
        return self.__x, self.__y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_pace(self):
        return self.__pace
