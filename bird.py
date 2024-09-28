import pygame as pg


class Bird:
    def __init__(self):
        self.__y = 100
        self.__moment = 0
        self.__g_force = 2
        self.__flap = -20
        self.__x = 50
        self.__bird = pg.image.load('bird.png')  # size 50x36
        self.__step = 0

    def __gravity(self):
        self.__moment += self.__g_force if self.__moment < 10 * self.__g_force else 0

    def jump(self):
        self.__moment = self.__flap

    def get_y(self):
        return self.__y

    def draw_bird(self, scr: pg.display.set_mode):
        scr.blit(self.__bird, (self.__x, self.__y))

    def step(self, scr):
        if pg.key.get_pressed()[pg.K_SPACE]:
            self.jump()
        else:
            self.__gravity()
        self.__y = min(645, max(0, self.__y + self.__moment))
        self.draw_bird(scr)
        self.__step += 1

    def get_step(self):
        return self.__step

    def hit_detection(self, p, p_gap):
        b = pg.Rect(self.__x, self.__y, 50, 36)
        p_b = pg.Rect(p[0], p[1], 110, 650)
        p_t = pg.Rect(p[0], p[1] - p_gap, 110, -650)
        return b.colliderect(p_t) or b.colliderect(p_b)

    def get_x(self):
        return self.__x

    def get_moment(self):
        return self.__moment
