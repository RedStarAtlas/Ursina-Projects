# Created by RedStarAtlas

from ursina import *
from time import sleep

app = Ursina(title='Pong Game!')

# Ping Pong Table
table = Entity(model="cube", color=color.light_gray, scale=(10, .5, 14), position=(0, 0, 0), texture='white_cube')

# The line/net of the table
line = Entity(parent=table, color=color.white, model="quad", scale=(.88, .2, .1), position=(0, 3.5, -.2))

#Player 1 paddle
Player_1_paddle = Entity(parent=table, color=color.blue, model="cube", scale=(.2, .03, .05), position=(0, 3.7, .22), collider="box")

#Player 2 paddle
Player_2_paddle = Entity(parent=table, color=color.blue, model="cube", scale=(.2, .03, .05), position=(0, 3.7, -.62), collider="box")

# Ping pong ball
ball = Entity(parent=table, model="sphere", color=color.magenta, scale=.05, position=(0, 3.71, -.2), collider="box", speed=0)

# The camera angle the user sees the game as
camera.position = (0, 15, -26)
camera.rotation_x = 30

# Resets the ball position
def reset_ball():
    ball.x = 0
    ball.z = -.2

def update():
    global dx, dz
    global score_A, score_B
    
    # Player 1 controls
    Player_1_paddle.x = Player_1_paddle.x + held_keys['right arrow'] * time.dt
    Player_1_paddle.x = Player_1_paddle.x - held_keys['left arrow'] * time.dt

    # Player 2 controls
    Player_2_paddle.x = Player_2_paddle.x + held_keys['d'] * time.dt
    Player_2_paddle.x = Player_2_paddle.x - held_keys['a'] * time.dt

    # Ball control
    ball.x = ball.x + time.dt*2 * dx
    ball.z = ball.z + time.dt*2 * dz

    # Ball Collision
    hit_info = ball.intersects()

    if hit_info.hit:
        if hit_info.entity == Player_1_paddle or hit_info.entity == Player_2_paddle:
            dz = -dz

    # Table left and right border check
    if abs(ball.x) > .4:
        dx = -dx
    
    # Table floor and ceiling border check
    if ball.z > .25:
        score_B += 1
        print_on_screen(f"Player 1: {score_A}, Player 2: {score_B}", position=(-.85, .45), scale=2, duration=1)

        if score_B >= 10:
            sleep(2)
            exit()

        reset_ball()

    if ball.z < -.65:
        score_A += 1
        print_on_screen(f"Player 1: {score_A}, Player 2: {score_B}", position=(-.85, .45), scale=2, duration=1)

        if score_A >= 10:
            sleep(2)
            exit()

        reset_ball()

    if held_keys['space']:
        info_press.visible = False
        dx = .1
        dz = .2
        reset_ball()

# UI
Text(text="Player 1", scale=2, position=(-.09, .40))
Text(text="Player 2", scale=2, position=(-.09, -.43))
Text(text="Hold [Space Bar] to reset the hockey puck ", scale=1, position=(.45, .3))
info_press = Text(text="Press [Space Bar] to start", scale=2, position=(.2, .4))

score_A = 0
score_B = 0
dx = 0
dz = 0

app.run()