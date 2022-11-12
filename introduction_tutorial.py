# imports all necessary things we need from the engine
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# creates a window
app = Ursina()

# most things in ursina are Entities. An Entity is a thing you place in the world.
# you can think of them as GameObjects in Unity or Actors in Unreal.
# the first paramenter tells us the Entity's model will be a 3d-model called 'cube'.
# the next parameter tells us the model's color should be orange.

player = Entity(model='cube', color=color.azure, scale_y=2)

# can move the camera around with the mouser
EditorCamera()

# create a function called 'update'.
# this will automatically get called by the engine every frame.

def update():
# this part will make the player move left or right based on our input.
# to check which keys are held down, we can check the held_keys dictionary.
# 0 means not pressed and 1 means pressed.
# time.dt is simply the time since the last frame. by multiplying with this, the
# player will move at the same speed regardless of how fast the game runs.

    player.x += held_keys['d'] * time.dt * 4
    player.x -= held_keys['a'] * time.dt *4 
        
def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)

# starts running the game
app.run()