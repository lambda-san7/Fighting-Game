##########################
# IMPORTS
##########################

from defaults import window, tick, sprite, events, center

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
    sprite("line_of_duty.png").render(
        center.x(window.w(),100),
        center.y(window.h(),100),
        100,
        100
    )
    window.update()