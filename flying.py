"""
Handles all elements that will move around the screen
"""
import arcade
import random
from point import Point, Velocity


BOMB_SPEED = 8
class Flying:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True

    def update(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def is_off_screen(self, width):
        if self.center.x > width or self.center.x < 0:
            return True
    

class Bullet1(Flying):
    def __init__(self, playerx, playery, color, velocity):
        super().__init__()
        self.center.x = playerx
        self.center.y = playery
        self.velocity.dx =  velocity
        self.color = color
        self.radius = 5
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)



class Bullet2(Flying):
    def __init__(self, playerx, playery):
        super().__init__()
        self.center.x = playerx
        self.center.y = playery
        self.velocity.dx = -10

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, 10, arcade.color.DARK_BROWN)


class Bomb(Flying):
    def __init__(self, width, height):
        super().__init__()
        self.center.x = random.uniform(width /2, width -width /4 )
        self.center.y = random.uniform(height /2, height - height /4)
        self.color = arcade.color.BLACK
        self.velocity.dx = random.uniform(-BOMB_SPEED, BOMB_SPEED)
        self.velocity.dy = random.uniform(-BOMB_SPEED, BOMB_SPEED)
        self.radius = 20
        self.width = width
        self.height = height

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y,self.radius, self.color)

    def update(self):
        super().update()
        if self.center.x > self.width - self.radius:
            self.velocity.dx *= -1

        if self.center.x < self.radius:
            self.velocity.dx *= -1

        if self.center.y > self.height - self.radius:
            self.velocity.dy *= -1

        if self.center.y < self.radius:
            self.velocity.dy *= -1