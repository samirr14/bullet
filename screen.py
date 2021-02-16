"""
Handles all elements that will show information on the screen
"""
import arcade
from point import Point
class Screen:
    def __init__(self, width, height):
        self.center = Point()
        self.active = True
        self.center.x = width
        self.center.y = height

    def draw(self):
        #last parameter is width of the outline
        arcade.draw_rectangle_outline(self.center.x/2, self.center.y/2, self.center.x -10, self.center.y -10 , arcade.color.BLACK, 10)
        

class PlayerInfo(Screen):
    def __init__(self, width, height, x, name, lives, color, bullet, score):
        super().__init__(width, height)
        self.x = x
        self.name = name
        self.lives = lives
        self.color = color
        self.bullet = bullet
        self.score = score
        

    def draw(self):
        super().draw()
        self.info = "{} - Lives: {} - Bullets: {} - Points: {}".format(self.name, self.lives, self.bullet, self.score)
        arcade.draw_text(self.info,self.x, self.center.y -30, self.color, 20,0,align="center",anchor_x="center",anchor_y="center")

    def update(self, lives, bullet, score):
        self.lives = lives
        self.bullet = bullet
        self.score = score



class Start(Screen):
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def draw(self):
        super().draw()
        self.title = "Bullet Vs Bullet\n See who's better"
        self.instructions1 = "Player 1: \n\n W (up), A (left), \nS (downn), D(right) \n\n G (shoot) Space (Pause) \n"
        self.instructions2 = "Player 2: \n\n up_arr(up), left_arr(left), down_arr(down), right_ arr(right) \n\n 1 (shoot) Enter (Pause) \n"
        self.instructions3 = "End with your opponent's life or reach 500 points to win the game!\n\nHit power up = +10 points / Hit Player = + 5 points / Bonus = + 25 points"
        self.begin = "Click any where to start!"
        

        arcade.draw_text(self.title, self.center.x /2, self.center.y -70, arcade.color.BLACK, 50,0,align="center",anchor_x="center",anchor_y="center")
        arcade.draw_text(self.instructions1, self.center.x /4, self.center.y - 250, arcade.color.DARK_BLUE, 25,0,align="center",anchor_x="center",anchor_y="center")
        arcade.draw_text(self.instructions2, self.center.x - self.center.x /4, self.center.y -250, arcade.color.DARK_RED, 25,0,align="center",anchor_x="center",anchor_y="center")
        arcade.draw_text(self.instructions3, self.center.x /2, self.center.y /3, arcade.color.BLACK, 30,0,align="center",anchor_x="center",anchor_y="center") 
        arcade.draw_text(self.begin, self.center.x /2, self.center.y /6, arcade.color.BLACK, 50,0,align="center",anchor_x="center",anchor_y="center")        

class Pause(Screen):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.active = False

    def draw(self):
        super().draw()

class GameOver(Screen):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.active = False

    def draw(self, p1, p2, winner, loser):
        super().draw()
        self.p1 = p1
        self.p2 = p2
        self.winner = winner
        self.loser = loser
        self.title = "Game Over"
        
        self.line1 = "The Winner is: {}".format(self.winner)
        self.line2 = "Sorry {}, you can try next time!".format(self.loser)
        if self.winner == self.p2:
            temp = self.line1
            self.line1 = self.line2
            self.line2 = temp

        arcade.draw_text(self.title, self.center.x /2, self.center.y -70, arcade.color.BLACK, 50,0,align="center",anchor_x="center",anchor_y="center")
        arcade.draw_text(self.line1, self.center.x /4, self.center.y - 250, arcade.color.DARK_BLUE, 25,0,align="center",anchor_x="center",anchor_y="center")
        arcade.draw_text(self.line2, self.center.x - self.center.x /4, self.center.y -250, arcade.color.DARK_RED, 25,0,align="center",anchor_x="center",anchor_y="center")

        


