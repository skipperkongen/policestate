import pyglet
from pyglet import shapes
import numpy as np

CELLS = 64
SCALE = 1
DIM = CELLS*SCALE

window = pyglet.window.Window(width=DIM, height=DIM)
batch = pyglet.graphics.Batch()


# https://pyglet.readthedocs.io/en/latest/programming_guide/shapes.html
dots = [
    pyglet.shapes.Rectangle(
        x=32,
        y=32,
        width=SCALE,
        height=SCALE,
        color=(225, 50, 30) if i == 0 else (50, 225, 30),
        batch=batch
    )
    for i in range(9)
]

def update(dt):
    for dot in dots:
        delta_x = np.random.randint(-1,2)
        delta_y = np.random.randint(-1,2)
        dot.x += delta_x
        dot.y += delta_y

pyglet.clock.schedule_interval(update, 0.1)

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()
print('foo')
