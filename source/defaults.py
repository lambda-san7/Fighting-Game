##########################
# IMPORTS
##########################

import pygame
import os

##########################
# INIT
##########################

pygame.init()

##########################
# FILE
##########################

dir_path = os.path.dirname(os.path.realpath(__file__))

##########################
# WINDOW
##########################

class new_window:
    def __init__(self,w,h,title):
        self.title = title
        self.pygame = pygame.display.set_mode((w,h),pygame.RESIZABLE)
        pygame.display.set_caption(title)

    def w(self):
        return pygame.display.Info().current_w
    
    def h(self):
        return pygame.display.Info().current_h
    
    def draw(self,image,x,y):
        self.pygame.blit(image,(x,y))

    def clear(self):
        self.pygame.fill((0,0,0))

    def update(self):
        pygame.display.update()

window = new_window(900,600,"Fighting Game")

##########################
# TIME
##########################

clock = pygame.time.Clock()

def tick():
    clock.tick(60)

##########################
# SPRITE
##########################

class sprite:
    def __init__(self,file_name):
        self.texture = pygame.image.load(f"{dir_path}/assets/{file_name}").convert_alpha()
    def render(self,x,y,w,h):
        window.draw(pygame.transform.scale(self.texture,(w,h)),x,y)

##########################
# EVENTS
##########################

def events():
    key_down = False
    key_up = False
    key_pressed = pygame.key.get_pressed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

##########################
# UTILITIES
##########################

class center:
    def x(parent_w,child_w):
        return ((parent_w / 2) - (child_w / 2))
    def y(parent_h,child_h):
        return ((parent_h / 2) - (child_h / 2))