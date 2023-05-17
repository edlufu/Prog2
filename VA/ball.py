"""  VA

Student: Edvin Lundberg
Mail: edvin.lundberg@gmail.com
Reviewed by: Sven-Erik Ekström
Date reviewed: 16/05
"""

from random import uniform, randint, choice
from vector import Vector
import tkinter as tk
from math import sqrt


class Ball:
    def __init__(self, box, v: float):
        self.box = box
        self.r = 15
        self.color = choice(("#F41311", "#552F4D", "#168BA0", "#4BB566", "#FEF716"))

        # creates ball in random location
        start_x = randint(self.r, self.box.W - self.r)
        start_y = randint(self.r, self.box.H - self.r)
        self.id = self.box.canvas.create_oval(
            start_x,
            start_y,
            (start_x + 2 * self.r),
            (start_y + 2 * self.r),
            fill=self.color,
        )
        # set poisition vector to center of ball
        self.pos = Vector(start_x + self.r, start_y + self.r)

        # set velocity vector with ball assinged speed in random direction
        mV_start = v
        xV_start = round(mV_start - uniform(0, 2 * mV_start), 3)
        yV_start = round((mV_start**2 - xV_start**2) ** 0.5, 3)
        self.v = Vector(xV_start, yV_start)

    def update_pos(self):
        """updates position vector after move()"""
        self.pos.x += self.v.x
        self.pos.y += self.v.y

    def man_update_pos(self, x, y):
        """manually update position to x, y coordinates"""
        self.pos.x = x
        self.pos.y = y

    def move(self):
        """moves ball on step,
        returns True if bounced"""

        # check if contact with wall
        bounce = self.bounce()

        # moves ball and updates pos and canvas
        self.box.canvas.move(self.id, self.v.x, self.v.y)
        self.update_pos()

        return bounce

    def bounce(self):
        """checks and handles collition with wall,
        return True if bounced"""
        bounce = False

        if self.pos.x + self.r >= self.box.W:
            self.box.canvas.moveto(
                self.id, self.box.W - (2 * self.r + 0.0001), self.pos.y - self.r
            )
            self.man_update_pos(self.box.W - (self.r + 0.0001), self.pos.y)
            self.v.x = -self.v.x
            bounce = True

        elif self.pos.x - self.r <= 0:
            self.box.canvas.moveto(self.id, 0.0001, self.pos.y - self.r)
            self.man_update_pos((self.r + 0.0001), self.pos.y)
            self.v.x = -self.v.x
            bounce = True

        if self.pos.y + self.r >= self.box.H:
            self.box.canvas.moveto(
                self.id, self.pos.x - self.r, self.box.H - (2 * self.r + 0.0001)
            )
            self.man_update_pos(self.pos.x, self.box.H - (self.r + 0.0001))
            self.v.y = -self.v.y
            bounce = True

        elif self.pos.y - self.r <= 0:
            self.box.canvas.moveto(self.id, self.pos.x - self.r, 0.0001)
            self.man_update_pos(self.pos.x, self.r + 0.0001)
            self.v.y = -self.v.y
            bounce = True

        return bounce

    def distance(self, other):
        """Calculates distance to other ball,
        from center to center"""
        dx = self.pos.x - other.pos.x
        dy = self.pos.y - other.pos.y
        return (dx**2 + dy**2) ** 0.5

    def collition(self, other):
        """Returns true if balls overlapp"""
        return self.distance(other) < self.r + other.r

    def collide(self, other):
        """Ball who hits other absorbs other,
        new area bceomes sum of area, winning ball retains its color"""
        self.r = sqrt(self.r**2 + other.r**2)

        # redraws winning ball with new are in same position
        self.box.canvas.coords(
            self.id,
            self.pos.x - self.r,
            self.pos.y - self.r,
            self.pos.x + self.r,
            self.pos.y + self.r,
        )


if __name__ == "__main__":
    window = tk.Tk()
    canvas = tk.Canvas(window, height=500, width=500)

    window.mainloop()
