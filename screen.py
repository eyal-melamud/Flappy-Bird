import pygame as pg
from pipe import Pipe
from button import Button

pg.init()


def print_txt(scr, txt, x, y, size):
    white = (255, 255, 255)
    pg.display.set_caption('Show Text')
    font = pg.font.Font('freesansbold.ttf', size)
    text = font.render(str(txt), True, white)
    scr.blit(text, (x, y))


class Window:
    def __init__(self, fps):
        self.scr = pg.display.set_mode((450, 800))
        self.__bg = pg.image.load('bg.jpg')
        self.__ground = pg.image.load('bg_b.jpg')
        self.__place = 0  # the position of the moving ground
        self.scr.fill((0, 0, 0))
        self.__point = 0
        self.__base = 0
        self.cool_down = 10
        self.__step = 0  # counts how many steps have been played
        self.b_sp1 = Button(400, 600, 32, 'x1', 40, fps == 40)
        self.b_sp2 = Button(400, 650, 32, 'x3', 120, fps == 120)
        self.b_sp3 = Button(400, 700, 32, 'x?', 1000, fps == 1000)
        self.b_sp4 = Button(400, 750, 32, '->', 0, False)
        self.buttons = [self.b_sp1, self.b_sp2, self.b_sp3, self.b_sp4]

    def print_screen(self, pipes, birds, gen=0):

        self.scr.fill((0, 0, 0))
        self.scr.blit(self.__bg, (0, 0))

        if self.got_a_point(pipes, birds):
            self.__point += 1

        # prints

        # draws the pipes
        for pi in pipes:
            pi.draw(self.scr)
        # prints the ground and takes care of her movement
        self.scr.blit(self.__ground, (self.__place, 645))
        # draw the birds
        if self.__place <= - 450:
            self.__place = 0
        else:
            self.__place -= Pipe().get_pace()

        print_txt(self.scr, self.__point, 200, 50, 50)  # prints the score
        print_txt(self.scr, 'gen - {}'.format(gen), 20, 700, 22)
        print_txt(self.scr, 'birds still alive - {}'.format(len(birds)), 20, 725, 22)
        self.b_sp1.print_button(self.scr)
        self.b_sp2.print_button(self.scr)
        self.b_sp3.print_button(self.scr)
        self.b_sp4.print_button(self.scr)
        for br in birds:
            br.step(self.scr)
        pg.display.flip()

    def got_a_point(self, pipes, birds):
        if self.cool_down > 0:
            self.cool_down -= 1
            return False
        for pi in pipes:
            for bird in birds:
                if pi.get_x() - pi.get_pace() <= bird.get_x() <= pi.get_x() + pi.get_pace():
                    self.cool_down = 10
                    return True
        return False

    def get_point(self):
        return self.__point

    def hendel_buttons(self, x, y, fps):
        for b in self.buttons:
            if b.sp_1.collidepoint(x, y):
                for c in self.buttons: c.con = False
                b.con = True
                return b.value
        return fps
