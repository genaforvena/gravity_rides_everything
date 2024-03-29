'''
@author: Ilya Mozerov
'''
from pygame import *

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = "#0000ff"

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)