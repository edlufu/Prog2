"""  VA

Student: Edvin Lundberg
Mail: edvin.lundberg@gmail.com
Reviewed by: Sven-Erik Ekström
Date reviewed: 16/05
"""

import tkinter as tk
from ball import Ball
from random import choice


class Box:
    def __init__(self, window: tk.Tk):
        self.W = 1000
        self.H = 700

        self.root = window
        self.canvas = tk.Canvas(
            master=self.root, width=self.W, height=self.H, bg="white"
        )
        self.canvas.pack(side=tk.RIGHT)

        self.balls = []

    def set_box(self, n, v):
        """Prepares box for animation start,
        creates balls, etc."""
        self.announcement = self.canvas.create_text(
            self.W / 2,
            self.H / 2,
            anchor=tk.CENTER,
            text="WINNER",
            font=("Arial", 220, "bold"),
            state=tk.HIDDEN,
        )

        self.n = n
        self.ball_v = v

        self.balls = [Ball(self, self.ball_v) for _ in range(self.n)]

    def clear_box(self):
        """Deletes all widgets on canvas"""
        self.canvas.delete("all")

    def move_all(self):
        """Moves all balls one step,
        handles wall and ball to ball collition"""
        for ball_i in self.balls:
            i = self.balls.index(ball_i)
            ball_i.move()
            for ball_j in self.balls[i + 1 :]:
                if ball_i.collition(ball_j):
                    ball_i.collide(ball_j)

                    self.canvas.delete(ball_j.id)
                    self.balls.remove(ball_j)

    def last_ball(self):
        """Chechs if only one ball is left"""
        return len(self.balls) == 1

    def victory_lap(self):
        """Alternative movement cycle for last ball"""
        winner = self.balls[0]
        bounce = winner.move()

        colors = ["#F41311", "#552F4D", "#168BA0", "#4BB566", "#FEF716"]
        if bounce:
            colors.remove(winner.color)
            randcolor = choice(colors)
            winner.color = randcolor
            self.canvas.itemconfig(winner.id, fill=randcolor)


if __name__ == "__main__":
    window = tk.Tk()

    window.mainloop()
