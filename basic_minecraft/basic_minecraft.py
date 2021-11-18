from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

sirka = 9
delka = 9

okno = Ursina()

trava_textura = load_texture("assets/grass_block.png")
kamen_textura = load_texture("assets/stone_block.png")
cihly_textura = load_texture("assets/brick_block.png")
hlina_textura = load_texture("assets/dirt_block.png")
obloha_textura = load_texture("assets/skybox.png")
ruka_textura = load_texture("assets/arm_texture.png")
niceni_zvuk = Audio("assets/punch_sound.wav", loop=False, autoplay=False)

blok_vyber = 1

window.fps_counter.enabled = False
window.exit_button.visible = False


def update():
    if held_keys["left mouse"] or held_keys["right mouse"]:
        ruka.aktivita()

    else:
        ruka.nic_nedela()

    global blok_vyber
    if held_keys["1"]:
        blok_vyber = 1

    elif held_keys["2"]:
        blok_vyber = 2

    elif held_keys["3"]:
        blok_vyber = 3

    elif held_keys["4"]:
        blok_vyber = 4


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=trava_textura):
        super().__init__(
            parent=scene,
            position=position,
            model="assets/block",  # ursina nemá zvládnutou funkci pro nasazení externí textury, musí se udělat krychle externě co to umí
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5,
        )

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                niceni_zvuk.play()
                if blok_vyber == 1:
                    Voxel(position=self.position + mouse.normal, texture=trava_textura)
                    # position je pozice voxelu, mouse.normal zjistí na jaký povrh z krychle se dívím

                elif blok_vyber == 2:
                    Voxel(position=self.position + mouse.normal, texture=hlina_textura)

                elif blok_vyber == 3:
                    Voxel(position=self.position + mouse.normal, texture=kamen_textura)

                elif blok_vyber == 4:
                    Voxel(position=self.position + mouse.normal, texture=cihly_textura)

            if key == "left mouse down":
                niceni_zvuk.play()
                destroy(self)


class Obloha(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture=obloha_textura,
            scale=150,
            double_sided=True,
        )


class Ruka(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,  # statický obraz co se pohybuje pouze s kamerou, je na ni "nalepený"
            model="assets/arm",
            texture=ruka_textura,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6),
        )

    def aktivita(self):
        self.position = Vec2(0.3, -0.5)

    def nic_nedela(self):
        self.position = Vec2(0.4, -0.6)


for z in range(sirka):
    for x in range(delka):
        nahodny = random.randint(1, 5)

        Voxel(position=(x, 0, z), texture=trava_textura)
        if nahodny == 5:
            Voxel(position=(x, -1, z), texture=kamen_textura)

        else:
            Voxel(position=(x, -1, z), texture=hlina_textura)

        if nahodny == 5 or nahodny == 4:
            Voxel(position=(x, -2, z), texture=kamen_textura)

        else:
            Voxel(position=(x, -2, z), texture=hlina_textura)

        if nahodny == 5:
            Voxel(position=(x, -3, z), texture=hlina_textura)

        else:
            Voxel(position=(x, -3, z), texture=kamen_textura)

        Voxel(position=(x, -4, z), texture=kamen_textura)

hrac = FirstPersonController(position=(4, 0, 4))
# if FirstPersonController(position=(range(sirka), -8, range(delka))):
#    FirstPersonController(position=(4, 0, 4))

obloha = Obloha()
ruka = Ruka()

okno.run()
