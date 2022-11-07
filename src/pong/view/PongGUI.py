# package pong.view
import pygame

from pong.model.Ball import Ball
from pong.model.Pong import Pong
from pong.model.Paddle import Paddle
from pong.model.Config import *

# Initializing pygame
pygame.init()
pygame.display.set_caption("Pong")


class PongGUI:

    def __init__(self):

        # Color Settings
        self.ball_color = color_AZURE
        self.left_color = color_PASTEL_PINK
        self.right_color = color_PASTEL_PINK
        self.screen_color = color_BLACK
        self.points_color = color_AQUA

        # Creating screen
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

        # Ball / Paddles / Color Settings
        self.ball = Ball(GAME_WIDTH / 2, GAME_HEIGHT / 2, self.ball_color)
        self.paddle_left = Paddle(50, GAME_HEIGHT / 2, self.left_color)
        self.paddle_right = Paddle(GAME_WIDTH - 50, GAME_HEIGHT / 2, self.right_color)

        # Model
        self.pong_model = Pong(self.ball, self.paddle_left, self.paddle_right)

        # Clock
        self.clock = pygame.time.Clock()

        # Font
        self.points_font = pygame.font.SysFont(None, 36, True)

    """
    
    The GUI for the Pong game.
    No application logic here just GUI and event handling.

    """

    # ------- Keyboard handling ----------------------------------
    def key_pressed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.update_paddle_left_speed(-1)
            elif event.key == pygame.K_DOWN:
                self.update_paddle_left_speed(1)
            elif event.key == pygame.K_q:
                self.update_paddle_right_speed(-1)
            elif event.key == pygame.K_a:
                self.update_paddle_right_speed(1)

    def key_released(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.update_paddle_left_speed(0)
            elif event.key == pygame.K_DOWN:
                self.update_paddle_left_speed(0)
            elif event.key == pygame.K_q:
                self.update_paddle_right_speed(0)
            elif event.key == pygame.K_a:
                self.update_paddle_right_speed(0)

    def update_paddle_left_speed(self, factor):
        self.pong_model.set_speed_right_paddle(Paddle.PADDLE_SPEED * factor)

    def update_paddle_right_speed(self, factor):
        self.pong_model.set_speed_left_paddle(Paddle.PADDLE_SPEED * factor)

    # ---------- Rendering -----------------

    def __update_screen(self):
        pygame.display.flip()

    def __draw_background(self):
        self.screen.fill(self.screen_color)

    def __draw_ball(self):
        ball = self.pong_model.get_ball()
        center = (ball.get_x() + ball.get_width() / 2, ball.get_y() + ball.get_height() / 2)
        pygame.draw.circle(self.screen, ball.get_color(), center, ball.get_width() / 3)

    def __draw_paddle_left(self):
        paddle_left = self.pong_model.get_paddle_left()
        pygame.draw.rect(self.screen, paddle_left.get_color(),
                         (paddle_left.get_x(), paddle_left.get_y(), paddle_left.get_width(), paddle_left.get_height()))

    def __draw_paddle_right(self):
        paddle_right = self.pong_model.get_paddle_right()
        pygame.draw.rect(self.screen, paddle_right.get_color(),
                         (paddle_right.get_x(), paddle_right.get_y(), paddle_right.get_width(),
                          paddle_right.get_height()))

    def __show_points(self):
        points_left = self.pong_model.get_points_left()
        points_right = self.pong_model.get_points_right()
        img_left, img_right = self.__create_points_image(points_left, points_right)
        self.__draw_points_image(img_left, img_right)

    def __draw_points_image(self, img_left, img_right):
        rect_left = (150, 20)
        rect_right = (450, 20)
        self.screen.blit(img_left, rect_left)
        self.screen.blit(img_right, rect_right)

    def __create_points_image(self, points_left, points_right):
        points_left_str = f"{points_left}"
        points_right_str = f"{points_right}"
        img_left = self.points_font.render(points_left_str, True, self.points_color)
        img_right = self.points_font.render(points_right_str, True, self.points_color)
        return img_left, img_right

    def render(self):
        self.__draw_background()
        self.__show_points()
        self.__draw_ball()
        self.__draw_paddle_left()
        self.__draw_paddle_right()
        self.__update_screen()

    # ---------- Game loop ----------------

    def run(self):
        keep_going = True
        while keep_going:
            self.clock.tick(50)
            self.update()
            keep_going = self.handle_events()
        pygame.quit()

    def update(self):
        self.pong_model.update()
        self.render()

    def handle_events(self):
        keep_going = True
        events = pygame.event.get()
        for event in events:
            self.key_pressed(event)
            self.key_released(event)
            keep_going &= self.__check_for_quit(event)
        return keep_going

    @staticmethod
    def __check_for_quit(event):
        return event.type != pygame.QUIT
