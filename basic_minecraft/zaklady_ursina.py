from ursina import *


class TestKrychle(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            color=color.white,
            texture="white_cube",
            rotation=Vec3(45, 45, 45)
        )


class TestTlacitko(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="cube",
            texture="brick",
            color=color.blue,
            highlight_color=color.green,
            pressed_color=color.red
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                print("tlacitko zmacknuto")


def update():  # volá se na každým framu
    if held_keys["a"]:
        test_ctverec.x -= 1 * time.dt


okno = Ursina()

test_ctverec = Entity(model="quad", color=color.red, scale=(1, 4), position=(5, 1))  # (0, 0) je ve středu okna

sand_textura = load_texture("assets/Sans.png")
sans = Entity(model="quad", texture=sand_textura)

test_krychle = TestKrychle()

test_tlacitko = TestTlacitko()

okno.run()
