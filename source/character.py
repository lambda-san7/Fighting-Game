##########################
# IMPORTS
##########################

import pygame
from defaults import window, events

##########################
# HITBOX
##########################

class hitbox:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

##########################
# CHARACTER
##########################

class character:
    def __init__(self,controls=["w","a","s","d","RSHIFT","LSHIFT","RETURN"]):
        self.hitbox = hitbox(0,0,50,50)
        self.controls = controls

    def handle(self):
        self.controller()

    def controller(self):
        if events.key_down == self.controls[0]:
            print("jumped")
        if events.key_press[eval(f"pygame.K_{self.controls[1]}")]:
            print("moving left")
        if events.key_press[eval(f"pygame.K_{self.controls[3]}")]:
            print("moving right")
        if events.key_press[eval(f"pygame.K_{self.controls[2]}")]:
            print("crouching")
        if events.key_down == self.controls[4]:
            print("light attack")
        if events.key_down == self.controls[5]:
            print("dodge")
        if events.key_down == self.controls[6]:
            print("heavy attack")

michael = character()