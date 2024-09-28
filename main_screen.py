import pygame as pg
from bird import Bird
from pipe import Pipe


def print_txt(scr, txt, x, y, size):
    white = (255, 255, 255)
    pg.display.set_caption('Show Text')
    font = pg.font.Font('freesansbold.ttf', size)
    text = font.render(str(txt), True, white)
    scr.blit(text, (x, y))


class Window:
    def __init__(self):
        self.game = True
        self.br = Bird()
        self.scr = pg.display.set_mode((450, 800))
        self.__bg = pg.image.load('bg.jpg')
        self.__ground = pg.image.load('bg_b.jpg')
        self.__place = 0  # the position of the moving ground
        self.scr.fill((0, 0, 0))
        self.font = pg.font.Font(None, 32)
        self.clock = pg.time.Clock()
        self.__pipes = []
        self.__diff = 75  # controls the intensity of the pipes
        self.__count = self.__diff
        self.__fps = 30  # sets the speed of the game
        self.cool_down = 10
        self.__point = 0

    def __reset(self):
        self.br = Bird()
        self.__pipes = []
        self.__count = self.__diff
        self.cool_down = 10
        self.__point = 0

    def run(self, con=True):
        while self.game:
            self.scr.fill((0, 0, 0))
            self.scr.blit(self.__bg, (0, 0))
            if self.__count <= 0:
                self.__pipes.append(Pipe())
                self.__count = self.__diff
            else:
                self.__count -= 1
            for pi in self.__pipes:
                pi.draw(self.scr)
                self.hit_detection(self.br.get_y(), pi.get_pos(), pi.get_gap())
            events = pg.event.get()
            events = [event.type for event in events]
            if pg.QUIT in events:
                self.game = False
                continue

            if True in [self.hit_detection(self.br.get_y(), pi.get_pos(), pi.get_gap()) for pi in self.__pipes] or \
                    self.br.get_y() in [645, 0]:
                self.game = con
                self.__reset()
                continue

            if self.got_a_point():
                self.__point += 1
                print(self.br.get_step())

            # prints
            self.scr.blit(self.__ground, (self.__place, 645))
            if self.__place <= - 450:
                self.__place = 0
            else:
                self.__place -= Pipe().get_pace()
            print_txt(self.scr, self.__point, 200, 50, 50)
            self.br.step(self.scr)
            pg.display.flip()
            self.clock.tick(self.__fps)

    def hit_detection(self, b_y, p, p_gap):
        b = pg.Rect(self.br.get_x(), b_y, 50, 36)
        p_b = pg.Rect(p[0], p[1], 110, 650)
        p_t = pg.Rect(p[0], p[1] - p_gap, 110, -650)
        return b.colliderect(p_t) or b.colliderect(p_b)

    def got_a_point(self):
        if self.cool_down > 0:
            self.cool_down -= 1
            return False
        for pi in self.__pipes:
            if pi.get_pos()[0] - pi.get_pace() <= self.br.get_x() <= pi.get_pos()[0] + pi.get_pace():
                self.cool_down = 10
                return True
        return False
