"""
Main file
Name Bullet VS

Description: 2 player arcade game
2D interface
Each player on one side of the screen shooting bullets one to another until one dies.
"""
import arcade
import random
#Import Classes
from static import Wall
from players import P1, P2
from flying import Bullet1, Bomb
from power import SpeedBullet, SpeedPlayer, AddLive, AddBullet, BonusScore
from screen import PlayerInfo, Start, GameOver

#Import Functions
import controls
import check_coll
import create_random


#Global Variables
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
P1_NAME = "Player 1"
P2_NAME = "Player 2"

class Game(arcade.Window):
    """
    Handles all the interaction between the players and the scenario
    """
    def __init__(self, width, height):
        super().__init__(width, height)

        self.game_on = False
        self.start = Start(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game_over = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT)


        self.winner = None
        self.loser = None
        #Splits the screen
        self.line = Wall(SCREEN_WIDTH /2, SCREEN_HEIGHT/2, 10, SCREEN_HEIGHT)

        #Powerups
        self.power_ups = []
        
        #Bomb
        self.bombs = []
        

        #player1 info
        self.p1 = P1(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.p1_bullet = []
        #Expects several parameters(x, y, name, lives, color, bullets)
        self.p1_info = PlayerInfo(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_WIDTH /4, P1_NAME, self.p1.lives, self.p1.color, len(self.p1.bullets), self.p1.score)

        #player2 info
        self.p2 = P2(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.p2_bullet = []
        #Expects several parameters(x, y, name, lives, color, bullets)
        self.p2_info = PlayerInfo(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_WIDTH - SCREEN_WIDTH /4, P2_NAME, self.p2.lives, self.p2.color, len(self.p2.bullets), self.p1.score)

        self.players = [self.p1,self.p2]
        #Sets the background
        arcade.set_background_color(arcade.color.WHITE)


    def on_draw(self):
        #Draws in the screen
        arcade.start_render()

        if self.game_on:
            self.line.draw()

            #Player 1 draw
            self.p1.draw()
            self.p1_info.draw()
            for i in self.p1_bullet:
                i.draw()
            
            #Player2 draw
            self.p2.draw()
            self.p2_info.draw()
            for i in self.p2_bullet:
                i.draw()

            #Powers Draw
            for p in self.power_ups:
                p.draw()

            #draw bomb
            for b in self.bombs:
                b.draw()

        elif self.start.active == True:
            self.start.draw()
        elif self.game_over.active == True:
            arcade.start_render()
            self.line.draw()
            self.p1_info.draw()
            self.p2_info.draw()
            self.game_over.draw(P1_NAME, P2_NAME, self.winner, self.loser)

    def update(self, delta_time):
        """
        Updates the game
        """
        if self.game_on:

            check_coll.check_bullets(self, self.p1_bullet, self.p2_bullet)
            check_coll.off_screen(self, SCREEN_WIDTH)
            check_coll.check_shot(self, P1_NAME, P2_NAME)
            check_coll.check_power(self)
            check_coll.check_power_bullet(self)
            check_coll.check_bomb(self, P1_NAME, P2_NAME)
            check_coll.check_bomb_bullets(self)

            #Updates the player's info
            self.p1.update()
            #pass the current lives to update it on the screen
            self.p1_info.update(self.p1.lives, len(self.p1.bullets), self.p1.score)
            for i in self.p1_bullet:
                i.update()

            self.p2.update()
            self.p2_info.update(self.p2.lives, len(self.p2.bullets), self.p2.score)
            for i in self.p2_bullet:
                i.update()

            for b in self.bombs:
                b.update()
            #Creates random powers
            if random.randint(1,200) == 1:
                create_random.create_power(self, SCREEN_WIDTH, SCREEN_HEIGHT)
                create_random.create_bomb(self, SCREEN_WIDTH, SCREEN_HEIGHT)

            #removes random powers and resets player attributes
            if random.randint(1,700) == 1:
                self.reset_powers(self.p1)
                self.reset_powers(self.p2)
                if len(self.power_ups) > 0:
                    self.power_ups.pop()
    
        else:
            self.reset_lists(self.p1)
            self.reset_lists(self.p2)


            self.reset_powers(self.p1)
            self.reset_powers(self.p2)
            
            
    def reset_powers(self,player):
        """Reset Atrributes"""
        player.bullet_speed = 15
        player.speed = 10

    def reset_lists(self,player):
        """resets game"""
        player.bullets = []
        player.reload()
        self.p1.lives = 5
        self.p1_bullet = []
        self.p1.score = 0
        
        self.p2.lives = 5
        self.p2_bullet = []
        self.p2.score = 0
        self.power_ups = []
        self.bombs = []
    

    
    def remove_dead(self):
        """Removes all dead bullets"""
        for bullet in self.p1_bullet:
            if not bullet.alive:
                self.p1_bullet.remove(bullet)

        for bullet in self.p2_bullet:
            if not bullet.alive:
                self.p2_bullet.remove(bullet)
        
        for power in self.power_ups:
            if not power.alive:
                self.power_ups.remove(power)       

        for bomb in self.bombs:
            if not bomb.alive:
                self.bombs.remove(bomb) 



    """
    Handles the user interaction with the game
    Key press to move, shoot, and pause the game, 
    Clicks to start the game
    """
    def on_key_press(self, key, modifiers):
        
        if self.game_on == True:
            #parameters: key, modifiers, velocity_dx, velocity_dy, speed, bullets
            controls.p1_control(key, self.p1, self.p1_bullet)
            #Move P2
            controls.p2_control(key, self.p2, self.p2_bullet)
                

    def on_key_release(self, key, modifiers):
        #Stops p1
        controls.p1_stop(key, self.p1)

        #Stops P2
        controls.p2_stop(key, self.p2)

    
    def on_mouse_press(self,x: float, y: float, button: int, modifiers: int):
        if self.start.active == True:
            self.game_on = True
            self.start.active = False

        elif self.game_over.active == True:
            self.game_on = True
            self.game_over.active = False
        

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()

