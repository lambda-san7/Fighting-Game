##########################
# IMPORTS
##########################

from defaults import window, tick, sprite, events, center
from character import michael

##########################
# SCENES
##########################

def game():
    michael.handle()

scene = game

##########################
# GAME LOOP
##########################

while 1:
    tick()
    window.clear()
    events.update()
    scene()
    window.update()