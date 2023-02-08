import pygame as pg
import random

OKNO_SIRKA = 1000
OKNO_VYSKA = 800

CERNA = (0, 0, 0)
CERVENA = (255, 0, 0)

GRAVITACE = 1
# ODPOR = 0.02

zrychleni_x = 0

x = random.randint(0, OKNO_SIRKA)
y = random.randint(0, OKNO_VYSKA)
rychlost_x = 3
rychlost_y = 0


class Micek():
    def __init__(self, pozice: list, rychlost: list, hmotnost: int):
        self.pozice = pozice
        self.rychlost = rychlost
        self.hmotnost = hmotnost

    def over_hmotnost(self):
        if self.hmotnost < 5:
            self.hmotnost = 5

    def posun_se(self):
        self.pozice[0] = self.pozice[0] + self.rychlost[0] # počítá pozici na x
        self.pozice[1] = self.pozice[1] + self.rychlost[1] + GRAVITACE # počítá pozici na y

        self.rychlost[0] = self.rychlost[0] # počítá rychlost na x
        self.rychlost[1] = self.rychlost[1] + GRAVITACE  # počítá rychlost na y

        # if self.rychlost[0] <= 0:
        #     self.rychlost[0] = 0
            # zastaví míček aby rychlost nebyla menší než 0

        if self.pozice[0] + self.hmotnost >= OKNO_SIRKA:
            self.rychlost[0] = - self.rychlost[0]
            # odraží míček od stěny

        if self.pozice[0] - self.hmotnost <= 0:
            self.rychlost[0] = - self.rychlost[0]
            # odráží míček od stěny

        if self.pozice[1] + self.hmotnost >= OKNO_VYSKA:
            self.rychlost[1] = - self.rychlost[1]
            # mění směr rychlosti na y, odráží míček od země

    def vykreli(self):
        int(self.pozice[0])
        pg.draw.circle(
            okno, CERVENA, self.pozice, int(self.hmotnost), int(self.hmotnost//5))


pg.init()

hodiny = pg.time.Clock()
fps = 60

pg.display.set_caption("Fyzikální simualce - pygame")
okno = pg.display.set_mode((OKNO_SIRKA, OKNO_VYSKA))

okno.fill(CERNA)

micek = Micek([x, y], [rychlost_x, rychlost_y], 10.3)
micek.over_hmotnost()
micek.vykreli()

running = True
while running:
    klavesa = pg.key.get_pressed()
    udalosti = pg.event.get()
    for event in udalosti:
        if event.type == pg.QUIT:
            running = False

        elif klavesa[pg.K_ESCAPE]:
            running = False

    okno.fill(CERNA)
    micek.posun_se()
    micek.vykreli()

    hodiny.tick(fps)
    pg.display.update()

pg.quit()
