# imports all necessary things we need from the engine
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# creates a window
app = Ursina()

player = Entity(model='cube', color=color.azure, scale_y=2)

# can move the camera around with the mouser
EditorCamera()

def update():
    player.x += held_keys['d'] * time.dt * 4
    player.x -= held_keys['a'] * time.dt *4 
        
def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)

# starts running the game
app.run()