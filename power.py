"""
Created power ups that can increase the player's speed, the bullets speed of give a shied, 
for a few seconds
"""
import arcade
import random
from point import Point
SIZE = 40

class Power:
    def __init__(self, width, height):
        self.center = Point()
        self.center.x = random.uniform(width/4, width - width/4)
        self.center.y = random.uniform(0, height)
        self.size = SIZE
        self.color = None
        self.text = ""
        self.alive = True

    def draw(self):
        arcade.draw_rectangle_outline(self.center.x, self.center.y, self.size, self.size,self.color,5)
        #text_x = self.center.x -(SIZE/2) 
        #text_y =self.center.y - (SIZE/2)
        arcade.draw_text(self.text,self.center.x, self.center.y,self.color,12,0, align="center", anchor_x="center", anchor_y="center")

        

class SpeedBullet(Power):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.color = arcade.color.GREEN
        self.text = ">>\nBull"

    def update(self, player):
        #Takes the bullet list form the main file
        player.bullet_speed = 22


class SpeedPlayer(Power):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.color = arcade.color.DARK_BROWN
        self.text = ">>\nPlayer"

    def update(self, player):
        player.speed = 15

class AddLive(Power):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.color = arcade.color.LIGHT_BLUE
        self.text = "+1\nLive"
    
    def update(self, player):
        player.lives  += 1

class AddBullet(Power):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.color = arcade.color.DARK_GRAY
        self.text = "+50\nBull"
    
    def update(self, player):
        player.reload()


class BonusScore(Power):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.color = arcade.color.PURPLE
        self.text = "+50\npoints"

    def update(self, player):
        player.score += 50