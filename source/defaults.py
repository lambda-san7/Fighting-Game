##########################
# IMPORTS
##########################

import pygame

##########################
# INIT
##########################

pygame.init()

##########################
# WINDOW
##########################

class new_window:
    def __init__(self,w,h,title):
        self.title = title
        self.pygame = pygame.display.set_mode((w,h),pygame.RESIZABLE)
        pygame.display.set_mode(title)

    def w(self):
        return pygame.display.Info().current_w
    
    def h(self):
        return pygame.display.Info().current_h
    
    def draw(self,image,x,y):
        self.pygame.blit(image,(x,y))

    def update(self):
        pygame.display.update()
        self.pygame.fill((0,0,0))

window = new_window(900,600,"Fighting Game")

##########################
# SPRITE
##########################

class sprite:
    def __init__(self,file_name):
        self.texture = pygame.image.load(file_name)
    def render(self,x,y,w,h):
        window.draw(pygame.transform.scale(self.texture,(w,h)),x,y)