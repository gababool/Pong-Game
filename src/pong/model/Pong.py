
from pong.model import Ball, Paddle
from pong.model.Ball import Ball
from pong.model.Config import GAME_HEIGHT, GAME_WIDTH, BALL_SPEED_FACTOR
from pong.model.Paddle import Paddle


class Pong:
    """

     * Logic for the Pong Game

    """

    points_left = 0
    points_right = 0

    def __init__(self, ball, paddle_left, paddle_right):

        self.ball: Ball = ball
        self.paddle_left: Paddle = paddle_left
        self.paddle_right: Paddle = paddle_right

        self.points_left = 0
        self.points_right = 0

    # --------  Game Logic -------------

    timeForLastHit_left = 0
    timeForLastHit_right = 0

    def update(self):
        self.move_paddle_left()
        self.move_paddle_right()
        self.move_ball()
        self.ball_paddle_collision()
        self.ball_border_collision()

    def ball_paddle_collision(self):
        if self.timeForLastHit_left == 0:
            if self.ball.intersects(self.paddle_left):
                self.ball.set_dx(-1 * BALL_SPEED_FACTOR)
                self.ball.set_dy(BALL_SPEED_FACTOR)
                self.timeForLastHit_left = 1
                self.timeForLastHit_right = 0
        if self.timeForLastHit_right == 0:
            if self.ball.intersects(self.paddle_right):
                self.ball.set_dx(-1 * BALL_SPEED_FACTOR)
                self.ball.set_dy(BALL_SPEED_FACTOR)
                self.timeForLastHit_left = 0
                self.timeForLastHit_right = 1

    def ball_border_collision(self):
        if self.ball.get_max_y() >= GAME_HEIGHT or self.ball.get_max_y() <= 30:
            self.ball.set_dy(-1)
        if self.ball.get_x() >= GAME_WIDTH:
            self.ball.center_ball()
            self.points_left += 1
            self.timeForLastHit_left, self.timeForLastHit_right = 0, 0
        if self.ball.get_x() <= 0:
            self.ball.center_ball()
            self.points_right += 1
            self.timeForLastHit_left, self.timeForLastHit_right = 0, 0

    # --- Used by GUI  ------------------------

    def get_ball(self):
        return self.ball

    def get_paddle_left(self):
        return self.paddle_left

    def get_paddle_right(self):
        return self.paddle_right

    def get_points_left(self):
        return self.points_left

    def get_points_right(self):
        return self.points_right

    def set_speed_right_paddle(self, speed):
        self.paddle_right.set_dy(speed)

    def set_speed_left_paddle(self, speed):
        self.paddle_left.set_dy(speed)

    def move_paddle_left(self):
        self.paddle_left.move_paddle()

    def move_paddle_right(self):
        self.paddle_right.move_paddle()

    def move_ball(self):
        self.ball.move_ball()