##########################
# IMPORTS
##########################

import pygame
from defaults import window, events, sprite, friction, gravity

floor = 400

##########################
# COLLISION
##########################

'''class collision:
    def __init__(self):
        self.idk = "idk"
    
    def grounded(self,y,h):
        if y + h >= 50:
            return True
        return False'''

##########################
# ENTITY
##########################

class entity:
    def __init__(self,parent,x,y,w,h):
        self.parent = parent
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x_velocity = 0
        self.y_velocity = 0
       # self.collision = collision()

    def physics(self):
        self.physics_x()
        self.physics_y()

    def physics_x(self):
        self.x += self.x_velocity

        if self.x_velocity < 0:
            self.x_velocity += friction

        if self.x_velocity > 0:
            self.x_velocity -= friction

    def physics_y(self):
        self.y_velocity += gravity
        
        if self.y + self.h <= floor:
            self.y += self.y_velocity

        if self.y + self.h >= floor:
            self.y_velocity = 0
            self.y = floor - self.h

        if self.y + self.h == floor:
            self.y_velocity = 0
            self.parent.curr_jumps = self.parent.jumps

##########################
# CHARACTER
##########################

class character:
    def __init__(self,controls=["w","a","s","d","RSHIFT","LSHIFT","RETURN"]):
        self.entity = entity(self,0,0,50,50)
        self.controls = controls
        self.speed = 20
        self.jump = 50
        self.jumps = 2
        self.curr_jumps = 0

    def handle(self):
        self.controller()
        self.entity.physics()
        self.render()

    def render(self):
        sprite("line_of_duty.png").render(self.entity.x,self.entity.y,self.entity.w,self.entity.h)

    def controller(self):
        if events.key_down == self.controls[0]:
            if self.curr_jumps != 0:
                self.curr_jumps -= 1
                self.entity.y_velocity = -self.jump
        if events.key_press[eval(f"pygame.K_{self.controls[1]}")]:
            self.entity.x_velocity = -self.speed
        if events.key_press[eval(f"pygame.K_{self.controls[3]}")]:
            self.entity.x_velocity = self.speed
        if events.key_press[eval(f"pygame.K_{self.controls[2]}")]:
            print("crouching")
        if events.key_down == self.controls[4]:
            print("light attack")
        if events.key_down == self.controls[5]:
            print("dodge")
        if events.key_down == self.controls[6]:
            print("heavy attack")

michael = character()