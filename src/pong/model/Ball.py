
from pong.model.Config import GAME_WIDTH, GAME_HEIGHT
from pong.model.AbstractGameItem import AbstractGameItem
import random

"""
 * A Ball for the Pong game
 * A model class
"""


class Ball(AbstractGameItem):
    WIDTH = 30
    HEIGHT = 30

    BALL_VELOCITY_X = random.choice([-1, 1]) * 4
    BALL_VELOCITY_Y = random.choice([-1, 1]) * random.randint(1, 3)

    def __init__(self, x, y, color):
        super().__init__(x, y, width=Ball.WIDTH, height=Ball.HEIGHT, color=color)
        self.x = x  # 0, 0 is upper left corner
        self.y = y
        self.dy = Ball.BALL_VELOCITY_Y
        self.dx = Ball.BALL_VELOCITY_X
        self.color = color

    def move_ball(self):
        self.set_y(self.get_y() + self.dy)
        self.set_x(self.get_x() + self.dx)

    def set_dx(self, dx):
        self.dx *= dx

    def set_dy(self, dy):
        self.dy *= dy

    def center_ball(self):
        self.x = GAME_WIDTH / 2
        self.y = GAME_HEIGHT / 2
        self.dx = (random.choice([-1, 1])) * 4
        self.dy = (random.choice([-1, 1])) * (random.randint(1, 3))
