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
        ball.collision_cooldown -= time.dt
        ball.position += ball.left * time.dt * ball.speed

        left_paddle.y += (held_keys['w'] - held_keys['s']) * time.dt * 1
        right_paddle.y += (held_keys['up arrow'] - held_keys['down arrow']) * time.dt * 1
    
        if ball.collision_cooldown > 0:
            return

        hit_info = ball.intersects()
        if hit_info.hit:
            ball.collision_cooldown = collision_cooldown

    def input(key):
        if key == 'space':
            info_text.enabled = False
            reset()
    
        if key == 't':
            ball.speed += 5
    
    app = Ursina(title='Pong Game!')

    app.run()