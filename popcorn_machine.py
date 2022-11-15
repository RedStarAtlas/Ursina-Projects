# Created by RedStarAtlas
# A popcorn machine simulator

from ursina import *

app = Ursina()

popcorn = Entity(model = 'sphere', texture = "images/popcorn.jpeg", scale = .5)

popcorn.x = 0
popcorn.y = 0
popcorn.dx = 0.05
popcorn.dy = 0.06

def update():
    popcorn.x += popcorn.dx
    popcorn.y += popcorn.dy
    if popcorn.x > 4:
        popcorn.x = 4
        popcorn.dx *= -1
    if popcorn.x < -4:
        popcorn.x = -4
        popcorn.dx *= -1
    if popcorn.y > 2:
        popcorn.y = 2
        popcorn.dy *= -1
    if popcorn.y < -2:
        popcorn.y = -2
        popcorn.dy *= -1

app.run()