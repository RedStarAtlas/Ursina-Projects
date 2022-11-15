# Created by RedStarAtlas
# A popcorn machine simulator

from ursina import *
import random

app = Ursina()

popcorn_multiple = []

for _ in range(40):
    popcorn = Entity(model = 'sphere', texture = "images/popcorn.jpeg", scale = .3)

    popcorn.x = random.randint(-3, 3)
    popcorn.y = random.randint(-2, 2)
    popcorn.z = random.randint(-4, 4)
    popcorn.dx = random.randint(1, 10) / 100
    popcorn.dy = random.randint(1, 10) / 100
    popcorn.dz = random.randint(1, 10) / 100

    popcorn_multiple.append(popcorn)

def update():
    for popcorn in popcorn_multiple:
        popcorn.x += popcorn.dx
        popcorn.y += popcorn.dy
        popcorn.z += popcorn.dz

        if popcorn.x > 3:
            popcorn.x = 3
            popcorn.dx *= -1
        if popcorn.x < -3:
            popcorn.x = -3
            popcorn.dx *= -1

        if popcorn.y > 2:
            popcorn.y = 2
            popcorn.dy *= -1
        if popcorn.y < -2:
            popcorn.y = -2
            popcorn.dy *= -1

        if popcorn.z > 4:
            popcorn.z = 4
            popcorn.dz *= -1
        if popcorn.z < -4:
            popcorn.z = -4
            popcorn.dz *= -1

        popcorn.rotation_z += 2

app.run()