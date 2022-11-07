
from pong.model.AbstractGameItem import AbstractGameItem


class Paddle(AbstractGameItem):

    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 60
    PADDLE_SPEED = 5

    def __init__(self, x, y, color):
        super().__init__(x, y, width=Paddle.PADDLE_WIDTH, height=Paddle.PADDLE_HEIGHT, color=color)
        self.dy = 0
        self.x = x  # 0, 0 is upper left corner
        self.y = y
        self.color = color
    
    def set_dy(self, dy):
        self.dy = dy

    def move_paddle(self):
        self.set_y(self.get_y() + self.dy)




