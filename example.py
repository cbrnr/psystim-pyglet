import pyglet
from pyglet.text import Label
from pyglet.window import Window, key

clock = pyglet.clock.get_default()
t0 = clock.time()


def time():
    return clock.time() - t0


with open("log.csv", "w") as f:
    f.write("time,key\n")

window = Window(caption="PsyStim")

label = Label(
    font_size=24,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)


@window.event
def on_key_press(symbol, modifiers):
    if symbol is not None:
        with open("log.csv", "a") as f:
            f.write(f"{time()},{key.symbol_string(symbol)}\n")


@window.event
def on_draw():
    window.clear()
    label.text = f"{time():.3f} s"
    label.draw()


pyglet.app.run()
