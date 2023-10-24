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
    sprite("line_of_duty.png").render(0, 400, window.w(), 400)

scene = game

##########################
# GAME LOOP
##########################

while 1:
    events.update()
    scene()
    window.update()
    window.clear()