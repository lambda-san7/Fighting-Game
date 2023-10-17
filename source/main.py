##########################
# IMPORTS
##########################

from defaults import window, tick, sprite, events

##########################
# SCENES
##########################

##########################
# GAME LOOP
##########################

while 1:
    tick()
    window.clear()
    events()
    sprite("line_of_duty.png").render(0,0,900,600)
    window.update()