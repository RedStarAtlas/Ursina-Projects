# Created by RedStarAtlas

from ursina import *

class Main(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui)

    # Creates the paddles
    left_paddle = Entity(scale = (.1, 2), x = -.75, model = 'quad', origin_x = .5, collider = 'box')
    right_paddle = Entity(scale = (.1, 2), x = .75, model = 'quad', origin_x = -.5, collider = 'box')
    
    # Creates the four walls
    floor = Entity(model='quad', y=-.5, origin_y=.5, collider='box', scale=(2,10), visible=False)
    ceiling = Entity(model='quad', y=.5, origin_y=-.5, collider='box', scale=(2,10), visible=False)
    left_wall = Entity(model='quad', x=-.5, origin_y=.5, collider='box', scale=(2,10), visible=False)
    right_wall = Entity(model='quad', x=.5, origin_y=-.5, collider='box', scale=(2,10), visible=False)
    
    collision_cooldown = .15
    ball = Entity(model='circle', scale=.2, collider='box', speed=0, collision_cooldown=collision_cooldown)
    
    def update():
        pass
    
    
    def input():
        pass
    
    app = Ursina(title='Pong Game!')

    app.run()