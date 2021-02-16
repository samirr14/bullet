"""
Creates 2 players facing each other
"""
import arcade
from point import Point, Velocity
from flying import Bullet1, Bullet2
PLAYER_SPEED = 10
BULLET_SPEED = 15   
GUN_SIZE = 25

class Player:
    """
    Parents players class
    """
    def __init__(self, screen_width, screen_height):
        self.center = Point()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity = Velocity()
        self.speed = PLAYER_SPEED
        self.radius = 20
        self.color = ""
        self.lives = 5
        self.score = 0

        self.bullets = []
        self.bullet_speed = BULLET_SPEED

    def draw(self):
        #Head
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)

    def update(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

        #Checks for collision with extra border (-10) Check Screen file line 14
        if self.center.y > self.screen_height - self.radius -5:
            self.center.y = self.screen_height - self.radius -5

        if self.center.y < self.radius +5:
            self.center.y = self.radius +5
    

    def fire(self):
        if len(self.bullets) > 0:
            return self.bullets.pop()
    
    def got_shot(self):
        self.lives -=1

class P1(Player):
    """
    Extends player and creates player 1
    gets the screen parameters to define the position of the player
    """
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        #Apears in the center of the left side
        self.center.x = screen_width /4
        self.center.y = screen_height /2
        self.color = arcade.color.DARK_BLUE
        self.bullet_color = arcade.color.DARK_MIDNIGHT_BLUE
        self.bullet_velocity = self.bullet_speed
        self.arm_color = arcade.color.BLACK
        self.reload()


    def draw(self):
        super().draw()
        #arm
        arcade.draw_rectangle_filled(self.center.x +5,self.center.y +15, GUN_SIZE, 10,self.arm_color)

    def update(self):
        super().update()

        #Stops at right side
        #if self.center.x > self.screen_width - self.radius -10:
            #self.center.x = self.screen_width - self.radius -10

        #Stop at half of the screen 
        if self.center.x > self.screen_width/2 - self.radius -5:
            self.center.x = self.screen_width/2 - self.radius -5
        #Stops at left side  
        if self.center.x < self.radius +10:
            self.center.x = self.radius +10
        

        #Keeps bullet in the gun
        for bullet in self.bullets:
            bullet.center.x = self.center.x +5
            bullet.center.y = self.center.y +15
            

    def reload(self):
        #Reloads up to 50 bullets
        for i in range(0,50):
            i = Bullet1(self.center.x, self.center.y +20, self.bullet_color, self.bullet_velocity)
            self.bullets.append(i)

class P2(Player):
    """
    Extends player and creates player 2
    gets the screen parameters to define the position of the player
    """
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.center.x = screen_width - screen_width/4
        self.center.y = screen_height/2
        self.color = arcade.color.DARK_RED
        self.bullet_color = arcade.color.RED_BROWN
        self.bullet_velocity = -self.bullet_speed
        self.arm_color = arcade.color.BLACK
        self.reload()

    def draw(self):
        super().draw()
        #arm
        arcade.draw_rectangle_filled(self.center.x -5,self.center.y +15, GUN_SIZE, 10, arcade.color.BLACK)

    def update(self):
        super().update()
        #Stops at left side of screen
        #if self.center.x < self.radius +10:
            #self.center.x = self.radius +10 
        #Stops at half of the screen
        if self.center.x < self.screen_width/2 + self.radius +5:
            self.center.x = self.screen_width/2 + self.radius +5
        #STops at right side
        if self.center.x > self.screen_width - self.radius -10:
            self.center.x = self.screen_width - self.radius -10

        #Keeps bullet in the gun
        for bullet in self.bullets:
            bullet.center.x = self.center.x -5
            bullet.center.y = self.center.y +15


    def reload(self):
        #Reloads up to 50 bullets
        for i in range(0,50):
            i = Bullet1(self.center.x, self.center.y +20, self.bullet_color, self.bullet_velocity)
            self.bullets.append(i)