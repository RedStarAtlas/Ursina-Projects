# Created by RedStarAtlas
# A popcorn machine simulator

from ursina import *
import random

app = Ursina()

title = Text(text = "Working Popcorn Machine!", scale = 2, position = (-.8, .40), color=color.yellow)
title_2 = Text(text = "Is there a purpose for this?", scale = 1, position = (-.8, .25))
title_3 = Text(text = "Probably not.", scale = 1, position = (-.8, .20), color=color.yellow)
title_4 = Text(text = "But now you've seen it!", scale = 1, position = (-.8, .15))
title_5 = Text(text = "*This showcases the use of collision and gravity*", scale = 1, position = (-.8, -.20), color=color.yellow)
title_6 = Text(text = "*Totally did not come up with this at midnight last night*", scale = .7, position = (-.8, -.30))
# creates the multiple popcorn instead of a singular one
popcorn_multiple = []

# Adds gravity to the popcorn so that it falls instead of floats
Gravity = -0.01

machine_back = Entity(model="cube",  scale=(6.6, 8), position=(0, 0, 0), texture = "images/pop.jpg")

# The camera angle the user sees the popcorn machine
camera.position = (-4, 0, -26)

# The random allows the popcorn to move at random speeds instead of all the same speed
for _ in range(150):
    popcorn = Entity(model = 'sphere', texture = "images/popcorn.jpeg", scale = .1)

    popcorn.x = random.randint(-2, 1)
    popcorn.y = random.randint(-3, 2)
    popcorn.z = random.randint(-4, 4)
    popcorn.dx = random.randint(1, 10) / 150
    popcorn.dy = random.randint(1, 10) / 150
    popcorn.dz = random.randint(1, 10) / 150

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
        if popcorn.y < -3:
            popcorn.y = -3
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

# Allows the popcorn to collide into eachother 
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