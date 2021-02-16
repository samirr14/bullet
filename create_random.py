"""
Creates the random objects that will appear on the screen
Bombs, Power ups, Etc
"""
import random
from flying import Bullet1, Bomb
from power import SpeedBullet, SpeedPlayer, AddLive, AddBullet, BonusScore

def create_power(self, width, height):
    powers = []
    speed_bullet = SpeedBullet(width, height)
    speed_player = SpeedPlayer(width, height)
    add_live = AddLive(width, height)
    add_bullet = AddBullet(width, height)
    bonus_score = BonusScore(width, height)

    powers.append(speed_player)
    powers.append(speed_bullet)
    powers.append(add_live)
    powers.append(add_bullet)
    powers.append(bonus_score)

    self.power_ups.append(random.choice(powers))

def create_bomb(self, width, height):
    bomb = Bomb(width, height)
    self.bombs.append(bomb)