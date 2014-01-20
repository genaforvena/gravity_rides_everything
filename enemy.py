'''
@author: Ilya Mozerov
'''
from pygame import *
from platformer.player import Unit
from platformer import unit

WIDTH = 40
HEIGHT = 32
COLOR =  "#900000"
GRAVITY = unit.GRAVITY * ((WIDTH * HEIGHT) / (unit.WIDTH * unit.HEIGHT))

class Enemy(Unit):
    def __init__(self, x, y, gravity = GRAVITY, width = WIDTH, height = HEIGHT, color = COLOR):
        super(Enemy, self).__init__(x, y, gravity, width, height, color)
    
    
