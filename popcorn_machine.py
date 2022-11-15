# Created by RedStarAtlas
# A popcorn machine simulator

from ursina import *
import random

app = Ursina()

popcorn_multiple = []

Gravity = -0.01

machine_back = Entity(model="cube",  scale=(5, 6.5), position=(0, 0, 0), color=color.red)
machine_front = Entity(model="cube",  scale=(4, 5), position=(0, 0, 0), color=color.white)
label_box = Entity(model="cube",  scale=(3.8, .5), position=(0, 2.9, 0), color=color.yellow)

# The camera angle the user sees the game as
camera.position = (-4, 0, -26)

for _ in range(80):
    popcorn = Entity(model = 'sphere', texture = "images/popcorn.jpeg", scale = .1)

    popcorn.x = random.randint(-2, 1)
    popcorn.y = random.randint(-2, 2)
    popcorn.z = random.randint(-4, 4)
    popcorn.dx = random.randint(1, 8) / 200
    popcorn.dy = random.randint(1, 8) / 200
    popcorn.dz = random.randint(1, 8) / 200

    popcorn_multiple.append(popcorn)

def update():
    for popcorn in popcorn_multiple:
        popcorn.dy += Gravity
        popcorn.x += popcorn.dx
        popcorn.y += popcorn.dy
        popcorn.z += popcorn.dz

        if popcorn.x > 1:
            popcorn.x = 1
            popcorn.dx *= -1
        if popcorn.x < -2:
            popcorn.x = -2
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

        popcorn.rotation_x += 2
        popcorn.rotation_y += 2
        popcorn.rotation_z += 2

    # Collision Checking
    for i in range(len(popcorn_multiple)):
        for j in range(i+1, len(popcorn_multiple)):
            popcorn1 = popcorn_multiple[i]
            popcorn2 = popcorn_multiple[j]
            x = popcorn1.x - popcorn2.x
            y = popcorn1.y - popcorn2.y
            z = popcorn1.z - popcorn2.z
            d = ((x**2) + (y**2) + (z**2)) ** 0.5
            if d < 1:
                popcorn1.dx, popcorn2.dx = popcorn2.dx, popcorn1.dx
                popcorn1.dy, popcorn2.dy = popcorn2.dy, popcorn1.dy
                popcorn1.dz, popcorn2.dz = popcorn2.dz, popcorn1.dz

app.run()