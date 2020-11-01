import pyglet
import numpy as np

CELLS = 64
SCALE = 5
DIM = CELLS*SCALE

window = pyglet.window.Window(width=DIM, height=DIM)

# https://pyglet.readthedocs.io/en/latest/programming_guide/shapes.html
circles = [
    pyglet.shapes.Rectangle(
        x=np.random.randint(20,DIM-20),
        y=np.random.randint(20,DIM-20),
        width=10,
        height=10,
        color=(225, 50, 30) if i == 0 else (50, 225, 30)
    )
    for i in range(9)
]

@window.event
def on_draw():
    window.clear()
    for circle in circles:
        circle.draw()

pyglet.app.run()
