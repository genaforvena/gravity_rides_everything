'''
@author: Ilya Mozerov
'''
from pygame import *

#default values
WIDTH = 22
HEIGHT = 20
COLOR =  "#888888"
GRAVITY = 0.35
GRAVITY_DESTINATION = "down"

def change_gravity_destination(gravity_destination):
    if not (gravity_destination == "up" or gravity_destination == "down" or gravity_destination == "left" or gravity_destination == "right"):
        raise TypeError("gravity_destination must be up, down, left or right")
    global GRAVITY_DESTINATION
    GRAVITY_DESTINATION = gravity_destination

class Unit(sprite.Sprite):
    def __init__(self, x, y, gravity = GRAVITY, width = WIDTH, height = HEIGHT, color = COLOR):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x 
        self.startY = y
        self.image = Surface((width, height))
        self.image.fill(Color(color))
        self.rect = Rect(x, y, width, height)
        self.yvel = 0 
        self.gravity = gravity
        
    def update(self, platforms):
        if GRAVITY_DESTINATION == "down":
            self.yvel += self.gravity
        if GRAVITY_DESTINATION == "up":
            self.yvel -= self.gravity 
        if GRAVITY_DESTINATION == "right":
            self.xvel += self.gravity
        if GRAVITY_DESTINATION == "left":
            self.xvel -= self.gravity
 
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms) 
        
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:     
                    self.rect.left = p.rect.right 

                if yvel > 0:                 
                    self.rect.bottom = p.rect.top 
                    self.yvel = 0

                if yvel < 0:   
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
    
    def is_touching_enemy(self, enemies):
        for enemy in enemies:
            if sprite.collide_rect(self, enemy):
                return True
            
    def is_touching_exit(self, exits):
        for exit in exits:
            if sprite.collide_rect(self, exit):
                return True