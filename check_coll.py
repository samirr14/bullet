"""
Checks collissions betweetn players and bullets, power ups and bombs,
and bullets with power ups and other bullets
"""

import arcade
"""Checks collision between bullets"""
def check_bullets(game, bullet_1, bullet_2):
    for bullet in bullet_1:
        for bullet2 in bullet_2:

            if bullet.alive and bullet2.alive: 

                if (abs(bullet.center.x - bullet2.center.x) < bullet.radius+bullet2.radius and abs(bullet.center.y - bullet2.center.y) < bullet.radius+ bullet2.radius):

                    bullet.alive = False
                    bullet2.alive = False
                    print("Bullets collide")
    
    for bullet2 in bullet_2:
        for bullet in bullet_1:

            if bullet.alive and bullet2.alive: 

                if (abs(bullet.center.x - bullet2.center.x) < bullet.radius+bullet2.radius and abs(bullet.center.y - bullet2.center.y) < bullet.radius+ bullet2.radius):

                    bullet.alive = False
                    bullet2.alive = False
                    print("Bullets collide")
    
    game.remove_dead()



def check_power_bullet(self):
    """Checks collissions between bullets and power ups"""
    for power in self.power_ups:
        for bullet in self.p1_bullet:
            too_close = bullet.radius + power.size /2
            if (abs(power.center.x - bullet.center.x) < too_close and abs(power.center.y -bullet.center.y) < too_close):
                power.alive = False
                bullet.alive = False
                self.p1.score += 10


    for power in self.power_ups:
        for bullet in self.p2_bullet:
            too_close = bullet.radius + power.size /2
            if (abs(power.center.x - bullet.center.x) < too_close and abs(power.center.y -bullet.center.y) < too_close):
                power.alive = False
                bullet.alive = False
                self.p2.score += 10

    self.remove_dead()

def check_power(self):
    """checks collissions between players and power ups"""
    for player in self.players:
        for power in self.power_ups:
            
            if power.alive:
                too_close = player.radius + power.size /2
                if abs(player.center.x - power.center.x) < too_close and abs(player.center.y - power.center.y) < too_close:
                    power.update(player)
                    power.alive = False
                    

    self.remove_dead()


def check_shot(self, p1_name, p2_name):
    """Checks coll between players and bullets"""

    #Bullet from player 1 hit player 2
    for bullet in self.p1_bullet:
        
        if bullet.alive:
            too_close = self.p2.radius + bullet.radius
            if abs(self.p2.center.x - bullet.center.x) < too_close and abs(self.p2.center.y - bullet.center.y) < too_close:
                bullet.alive = False
                if self.p2.lives > 1:
                    self.p2.got_shot()
                    self.p1.score += 5
                else:
                    self.p2.got_shot()
                    self.p1.score += 5
                    self.winner = p1_name
                    self.loser = p2_name
                    self.game_on = False
                    self.game_over.active = True
                    

    #Checks bullet form player 2 hits player1
    for bullet in self.p2_bullet:
        
        if bullet.alive:
            too_close = self.p1.radius + bullet.radius
            if abs(self.p1.center.x - bullet.center.x) < too_close and abs(self.p1.center.y - bullet.center.y) < too_close:
                bullet.alive = False
                if self.p1.lives > 1:
                    self.p1.got_shot()
                    self.p2.score += 5
                else:
                    self.p1.got_shot()
                    self.p2.score += 5
                    self.winner = p2_name
                    self.loser = p1_name
                    self.game_over.active = True
                    self.game_on = False

    self.remove_dead()


def check_bomb(self, p1_name, p2_name):
    """Checks coll between players and bombs"""
    for bomb in self.bombs:
        too_close = self.p1.radius +bomb.radius
        if bomb.alive:
            if abs(self.p1.center.x - bomb.center.x) < too_close and abs(self.p1.center.y - bomb.center.y) < too_close:
                bomb.alive = False
                if self.p1.lives > 1:
                    self.p1.got_shot()
                    self.p1.score -= 5
                else:
                    self.p1.got_shot()
                    self.p1.score -= 5
                    self.winner = p2_name
                    self.loser = p1_name
                    self.game_over.active = True
                    self.game_on = False
            elif abs(self.p2.center.x - bomb.center.x) < too_close and abs(self.p2.center.y - bomb.center.y)< too_close:
                bomb.alive = False
                if self.p2.lives > 1:
                    self.p2.got_shot()
                    self.p2.score -= 5
                else:
                    self.p2.got_shot()
                    self.p2.score -= 5
                    self.winner = p1_name
                    self.loser = p2_name
                    self.game_over.active = True
                    self.game_on = False
    self.remove_dead()


def check_bomb_bullets(self):
    for bomb in self.bombs:
        for bullet in self.p1_bullet:
            too_close = bullet.radius + bomb.radius
            if (abs(bomb.center.x - bullet.center.x) < too_close and abs(bomb.center.y -bullet.center.y) < too_close):
                bomb.alive = False
                bullet.alive = False
                self.p1.score += 10


    for bomb in self.bombs:
        for bullet in self.p2_bullet:
            too_close = bullet.radius + bomb.radius
            if (abs(bomb.center.x - bullet.center.x) < too_close and abs(bomb.center.y -bullet.center.y) < too_close):
                bomb.alive = False
                bullet.alive = False
                self.p2.score += 10

    self.remove_dead()


def off_screen(self, width):
    """Checks if bullet is off screnn"""
    for bullet in self.p1_bullet:
        if bullet.is_off_screen(width):
            bullet.alive = False
    for bullet in self.p2_bullet:
        if bullet.is_off_screen(width):
            bullet.alive = False