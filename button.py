import pygame as pg


class Button:
    def __init__(self, x, y, size, text, value, con=False):
        self.x, self.y, self.size, self.text = x, y, size, text
        self.sp_1 = pg.Rect(self.x, self.y - 5, self.size + 10, self.size + 10)
        self.font = pg.font.Font(None, 32)
        self.color_inactive = (170, 170, 170)
        self.color_active = (170, 170, 255)
        self.color_w = (230, 230, 230)
        self.con = con
        self.value = value

    def print_button(self, scr):
        pg.init()
        txt_surface = self.font.render(self.text, True, self.color_w)

        color = self.color_active if self.con else self.color_inactive
        pg.draw.line(scr, color, (self.x, self.y + 0.5 * self.size),
                     (self.x + self.size + 10, self.y + 0.5 * self.size),
                     self.size + 10)
        # Blit the text.
        scr.blit(txt_surface, (self.sp_1.x + 5, self.sp_1.y + 5))
        # Blit the input_box rect.
        pg.draw.rect(scr, self.color_w, self.sp_1, 2)
