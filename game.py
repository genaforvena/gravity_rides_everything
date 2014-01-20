'''
@author: Ilya Mozerov
'''
import pygame
from pygame import *
from platformer.player import *
from platformer.platform import *
from platformer.camera import *
from platformer.enemy import *
from platformer.exit import *

WIN_WIDTH = 800 
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#cdc9c9"

def start_game():
    pygame.init() 
    screen = pygame.display.set_mode(DISPLAY) 
    pygame.display.set_caption("Gravity rides everything")
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) 
    bg.fill(Color(BACKGROUND_COLOR))
    total_level_width = len(level[0])*PLATFORM_WIDTH
    total_level_height = len(level)*PLATFORM_HEIGHT
   
    timer = pygame.time.Clock()
    camera = Camera(configure_camera, total_level_width, total_level_height) 
    
    while True: 
        timer.tick(60)
        screen.blit(bg, (0,0))
        _process_key_press()
        
        for enemy in enemies:
            enemy.update(platforms)
         
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        player[0].update(platforms)
        camera.update(player[0])
        pygame.display.update() 
        
        if player[0].is_touching_enemy(enemies):
            raise SystemExit, "HERO WAS EATEN!"
        
        if player[0].is_touching_exit(exits):
            raise SystemExit, "YOU WIN!"

def _process_key_press():
    for e in pygame.event.get(): 
            if e.type == QUIT:
                raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_LEFT:
                change_gravity_destination("left")
            if e.type == KEYDOWN and e.key == K_RIGHT:
                change_gravity_destination("right")
            if e.type == KEYDOWN and e.key == K_DOWN:
                change_gravity_destination("down")
            if e.type == KEYDOWN and e.key == K_UP:
                change_gravity_destination("up")

def build_level_setup_functions(elementSign, elementConstructor, elementList):
    def setup_function():
        x=y=0
        for row in level: 
            for col in row:
                if col == elementSign:
                    element = elementConstructor(x, y)
                    elementList.append(element)                            
                    entities.add(element)
                    
                x += PLATFORM_WIDTH 
            y += PLATFORM_HEIGHT
            x = 0
    return setup_function
 
def configure_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width-WIN_WIDTH), l)  
    t = max(-(camera.height-WIN_HEIGHT), t) 
    t = min(0, t)                           

    return Rect(l, t, w, h)        

if __name__ == "__main__":
    player = []
    enemies = []
    platforms = []
    exits = []
    entities = pygame.sprite.Group()
    level = [
       "----------------------------------",
       "-                                -",
       "-                       --       -",
       "-                                -",
       "-            --                  -",
       "-    p                           -",
       "--                               -",
       "-                                -",
       "-                   ----     --- -",
       "-                                -",
       "--              e                -",
       "-                                -",
       "-                e               ----",
       "x                                   -",
       "-                                ----",
       "-      ---                       -",
       "-                                -",
       "-   -------         ----         -",
       "-                                -",
       "-                         -      -",
       "-                            --  -",
       "-                                -",
       "-                                -",
       "----------------------------------"] 
    
    setup_platforms = build_level_setup_functions("-", Platform, platforms)
    setup_exits = build_level_setup_functions("x", Exit, exits)
    setup_enemies = build_level_setup_functions("e", Enemy, enemies)
    setup_player = build_level_setup_functions("p", Player, player)
    
    setup_platforms()
    setup_exits()
    setup_enemies()
    setup_player()     
       
    start_game()
    