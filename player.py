'''
@author: Ilya Mozerov
'''
from pygame import *
from platformer.unit import *

WIDTH = 22
HEIGHT = 20
COLOR =  "#000000"

class Player(Unit):
    def __init__(self, x, y, gravity = GRAVITY, width = WIDTH, height = HEIGHT, color = COLOR):
        super(Player, self).__init__(x, y, gravity, width, height, color)