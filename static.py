"""
Handles the static onjects of the game, such as the floor and the walls
"""
import arcade
from point import Point


class Static:
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0
        self.color = ""

    def draw(self):
        pass

class Wall(Static):
    def __init__(self, screen_width, screen_height, wd, hg):
        super().__init__()
        self.center.x = screen_width
        self.center.y = screen_height 
        self.wd = wd
        self.hg = hg
        self.color = arcade.color.DARK_GREEN
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.wd , self.hg, self.color)

    