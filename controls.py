"""
Handlesthe players controls with the keyboard

"""
import arcade

"""PLAYER 1"""

def p1_control(key, player, bullet_list):
        #Move P1
        if key == arcade.key.D:
            player.velocity.dx = player.speed
        if key == arcade.key.A:
            player.velocity.dx = -player.speed
        if key == arcade.key.W:
            player.velocity.dy = player.speed
        if key == arcade.key.S:
            player.velocity.dy = -player.speed
        
        #Reload / Fire P1
        """
        if key == arcade.key.R:
            reload()
        """
        
        if key == arcade.key.G:
            #Creates and add a bullet to the list
            #bullet = self.bullet = Bullet1(self.p1.center.x, self.p1.center.y +20, self.p1.bullet_color, self.p1.bullet_speed)

            #self.p1_bullet.append(bullet)
            
            if len(player.bullets) > 0:
                #Gets a bullet from the bullet list in the player 1 class and adds it to the bullet list in Main
                bullet = player.bullets.pop()
                bullet_list.append(bullet)
                


def p1_stop(key, player):
    if key == arcade.key.D or key == arcade.key.A:
        player.velocity.dx = 0

    if key == arcade.key.W or key == arcade.key.S:
        player.velocity.dy = 0



"""PLAYER 2"""

def p2_control(key, player, bullet_list):
        if key == arcade.key.LEFT:
            player.velocity.dx = -player.speed
        if key == arcade.key.RIGHT:
            player.velocity.dx = player.speed
        if key == arcade.key.UP:
            player.velocity.dy = player.speed
        if key == arcade.key.DOWN:
            player.velocity.dy = -player.speed

        #Reload/Fire P2
        """
        if key == arcade.key.NUM_2:
            player.reload()
        """
        
        if key == arcade.key.NUM_1:
            #bullet = self.bullet = Bullet1(player.center.x, player.center.y +20, player.bullet_color,-player.bullet_speed)
            #player_bullet.append(bullet)
            
            if len(player.bullets) > 0:
                bullet_list.append(player.fire())
                

def p2_stop(key, player):
    if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        player.velocity.dx = 0

    if key == arcade.key.UP or key == arcade.key.DOWN:
        player.velocity.dy = 0